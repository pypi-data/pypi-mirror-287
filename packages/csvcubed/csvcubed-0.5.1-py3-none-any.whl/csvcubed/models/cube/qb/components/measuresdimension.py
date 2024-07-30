"""
Measures Dimension
------------------

Define a measure dimension in an RDF Data Cube.
"""

from dataclasses import dataclass
from typing import Dict, List

import pandas as pd
import uritemplate

from csvcubed.inputs import PandasDataTypes, pandas_input_to_columnar_str
from csvcubed.models.validationerror import (
    ValidateModelPropertiesError,
    ValidationError,
)
from csvcubed.utils import validations as v
from csvcubed.utils.qb.validation.uri_safe import ensure_no_uri_safe_conflicts
from csvcubed.utils.validations import ValidationFunction

from .datastructuredefinition import QbColumnStructuralDefinition
from .measure import ExistingQbMeasure, NewQbMeasure, QbMeasure
from .validationerrors import UndefinedMeasureUrisError


@dataclass
class QbMultiMeasureDimension(QbColumnStructuralDefinition):
    """
    Represents the measure types permitted in a multi-measure cube.
    """

    measures: List[QbMeasure]

    @staticmethod
    def new_measures_from_data(data: PandasDataTypes) -> "QbMultiMeasureDimension":
        columnar_data = pandas_input_to_columnar_str(data)
        qb_measures: List[QbMeasure] = [
            NewQbMeasure(m) for m in sorted(set(columnar_data))
        ]
        return QbMultiMeasureDimension(qb_measures)

    @staticmethod
    def existing_measures_from_data(
        data: PandasDataTypes, csvw_column_name: str, csv_column_uri_template: str
    ) -> "QbMultiMeasureDimension":
        columnar_data = pandas_input_to_columnar_str(data)
        return QbMultiMeasureDimension(
            [
                ExistingQbMeasure(
                    uritemplate.expand(csv_column_uri_template, {csvw_column_name: m})
                )
                for m in sorted(set(columnar_data))
            ]
        )

    def validate_data(
        self,
        data: pd.Series,
        csvw_column_name: str,
        csv_column_uri_template: str,
        column_csv_title: str,
    ) -> List[ValidationError]:
        if len(self.measures) > 0:
            unique_values = set(data.unique())

            map_label_to_new_uri_value = {}
            for u in self.measures:
                if isinstance(u, NewQbMeasure):
                    map_label_to_new_uri_value.update({u.label: u.uri_safe_identifier})

            if map_label_to_new_uri_value:
                unique_values = {
                    map_label_to_new_uri_value.get(v, v) for v in unique_values
                }

            unique_expanded_uris = {
                uritemplate.expand(csv_column_uri_template, {csvw_column_name: s})
                for s in unique_values
            }

            expected_uris = set()
            for measure in self.measures:
                if isinstance(measure, ExistingQbMeasure):
                    expected_uris.add(measure.measure_uri)
                elif isinstance(measure, NewQbMeasure):
                    expected_uris.add(
                        uritemplate.expand(
                            csv_column_uri_template,
                            {csvw_column_name: measure.uri_safe_identifier},
                        )
                    )
                else:
                    raise Exception(f"Unhandled measure type {type(measure)}")

            undefined_uris = unique_expanded_uris - expected_uris
            if len(undefined_uris) > 0:
                return [UndefinedMeasureUrisError(self, undefined_uris)]

        return []

    def _get_validations(self) -> Dict[str, ValidationFunction]:
        return {
            "measures": v.all_of(
                v.list(v.validated_model(QbMeasure)),
                self._validate_measures_non_conflicting,
            )
        }

    @staticmethod
    def _validate_measures_non_conflicting(
        measures: List[QbMeasure], property_path: List[str]
    ) -> List[ValidateModelPropertiesError]:
        """
        Ensure that there are no collisions where multiple new measures map to the same URI-safe value.
        """
        return ensure_no_uri_safe_conflicts(
            [
                (meas.label, meas.uri_safe_identifier)
                for meas in measures
                if isinstance(meas, NewQbMeasure)
            ],
            QbMultiMeasureDimension,
            property_path,
            measures,
        )
