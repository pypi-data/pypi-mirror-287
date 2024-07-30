"""
Models
------

config.json v1.* column mapping models.

If you change the shape of any model in this file, you **must** create a newly versioned JSON schema reflecting said changes.
"""

import logging
from abc import ABC
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple, TypeVar, Union

import uritemplate
from csvcubedmodels.dataclassbase import DataClassBase

from csvcubed.cli.codelist.build_code_list import get_code_list_versioned_deserialiser
from csvcubed.inputs import PandasDataTypes, pandas_input_to_columnar_optional_str
from csvcubed.models.cube.cube import CatalogMetadata
from csvcubed.models.cube.qb.components.attribute import (
    ExistingQbAttribute,
    ExistingQbAttributeLiteral,
    NewQbAttribute,
    NewQbAttributeLiteral,
    QbAttribute,
)
from csvcubed.models.cube.qb.components.codelist import (
    CompositeQbCodeList,
    DuplicatedQbConcept,
    ExistingQbCodeList,
    NewQbCodeList,
    QbCodeList,
)
from csvcubed.models.cube.qb.components.concept import NewQbConcept
from csvcubed.models.cube.qb.components.dimension import (
    ExistingQbDimension,
    NewQbDimension,
)
from csvcubed.models.cube.qb.components.measure import ExistingQbMeasure, NewQbMeasure
from csvcubed.models.cube.qb.components.measuresdimension import QbMultiMeasureDimension
from csvcubed.models.cube.qb.components.observedvalue import QbObservationValue
from csvcubed.models.cube.qb.components.unit import ExistingQbUnit, NewQbUnit
from csvcubed.models.cube.qb.components.unitscolumn import QbMultiUnits
from csvcubed.models.jsonvalidationerrors import JsonSchemaValidationError
from csvcubed.readers.codelistconfig.codelist_schema_versions import (
    LATEST_V1_CODELIST_SCHEMA_URL,
    LATEST_V2_CODELIST_SCHEMA_URL,
)
from csvcubed.utils.file import code_list_config_json_exists
from csvcubed.utils.uri import csvw_column_name_safe, looks_like_uri

_logger = logging.getLogger(__name__)

T = TypeVar("T", bound=object)

EXISTING_UNIT_DEFAULT_SCALING_FACTOR = 1.0


@dataclass
class SchemaBaseClass(DataClassBase, ABC):
    ...


@dataclass
class NewDimension(SchemaBaseClass):
    """
    Schema property - but removed for json to dataclass mapping
      type: # str = "dimension"
    """

    label: Optional[str] = None
    description: Optional[str] = None
    definition_uri: Optional[str] = None
    code_list: Union[str, bool, dict, None] = True
    from_existing: Optional[str] = None
    cell_uri_template: Optional[str] = None

    def map_to_new_qb_dimension(
        self,
        csv_column_title: str,
        data: PandasDataTypes,
        cube_config_minor_version: Optional[int],
        config_path: Optional[Path] = None,
    ) -> Tuple[NewQbDimension, List[JsonSchemaValidationError]]:
        if self.cell_uri_template and self.code_list:
            # Checking to see if the code_list provided is a code-list-config.json.
            # If so, then the code_list provided is not a boolean value or looks like an uri.
            if not isinstance(self.code_list, bool):
                if looks_like_uri(str(self.code_list)) == False:
                    raise ValueError(
                        "Setting the code_list to be a code-list-config.json is not doable when also provided with a cell_uri_template."
                    )

        new_dimension = NewQbDimension.from_data(
            label=self.label or csv_column_title,
            csv_column_title=csv_column_title,
            data=data,
            description=self.description,
            parent_dimension_uri=self.from_existing,
            source_uri=self.definition_uri,
            cell_uri_template=self.cell_uri_template,
        )
        # The NewQbCodeList and Concepts are populated in the NewQbDimension.from_data() call
        # the _get_code_list method overrides the code_list if required.
        (
            new_dimension.code_list,
            code_list_schema_validation_errors,
        ) = self._get_code_list(
            new_dimension,
            csv_column_title,
            cube_config_minor_version,
            cube_config_path=config_path,
        )

        return (new_dimension, code_list_schema_validation_errors)

    def _get_code_list(
        self,
        new_dimension: NewQbDimension,
        csv_column_title: str,
        cube_config_minor_version: Optional[int],
        cube_config_path: Optional[Path],
    ) -> Tuple[Optional[QbCodeList], List[JsonSchemaValidationError]]:
        if isinstance(self.code_list, str):
            if looks_like_uri(self.code_list):
                return (ExistingQbCodeList(self.code_list), [])
            # The following elif is for cube config v1.1. This also requires the user to define the configuration in the build command, and therefore cube_config_path.
            elif (
                cube_config_minor_version
                and cube_config_minor_version >= 1
                and cube_config_minor_version < 5
                and cube_config_path
                and code_list_config_json_exists(
                    Path(self.code_list), cube_config_path.parent
                )
            ):
                code_list_path = Path(self.code_list)
                code_list_config_path = (
                    code_list_path
                    if code_list_path.is_absolute()
                    else (cube_config_path.parent / code_list_path).resolve()
                )
                _logger.info(
                    f"Loading code list from local file path: {code_list_config_path}"
                )

                deserialiser = get_code_list_versioned_deserialiser(
                    code_list_config_path,
                    default_schema_uri=LATEST_V1_CODELIST_SCHEMA_URL,
                )

                (
                    new_code_list,
                    json_schema_validation_errors,
                    _,
                ) = deserialiser(code_list_config_path)

                return (new_code_list, json_schema_validation_errors)
            elif (
                cube_config_minor_version
                and cube_config_minor_version >= 5
                and cube_config_path
                and code_list_config_json_exists(
                    Path(self.code_list), cube_config_path.parent
                )
            ):
                code_list_path = Path(self.code_list)
                code_list_config_path = (
                    code_list_path
                    if code_list_path.is_absolute()
                    else (cube_config_path.parent / code_list_path).resolve()
                )
                _logger.info(
                    f"Loading code list from local file path: {code_list_config_path}"
                )

                deserialiser = get_code_list_versioned_deserialiser(
                    code_list_config_path,
                    default_schema_uri=LATEST_V2_CODELIST_SCHEMA_URL,
                )

                (
                    new_code_list,
                    json_schema_validation_errors,
                    _,
                ) = deserialiser(code_list_config_path)

                return (new_code_list, json_schema_validation_errors)
            else:
                raise ValueError(
                    "Code List contains a string that cannot be recognised as a URI or a valid File Path"
                )

        elif isinstance(self.code_list, bool):
            if self.code_list is False:
                return (None, [])
            elif (
                new_dimension.parent_dimension_uri
                == "http://purl.org/linked-data/sdmx/2009/dimension#refPeriod"
                and self.cell_uri_template is not None
                and self.cell_uri_template.lower().startswith(
                    "http://reference.data.gov.uk/id/"
                )
            ):
                # This is a special case where we build up a code-list of the date/time values.
                return (
                    self._get_date_time_code_list_for_dimension(
                        new_dimension, self.cell_uri_template, csv_column_title
                    ),
                    [],
                )
            else:
                return (new_dimension.code_list, [])

        # The following elif is for cube config v1.1 and when the code list is defined inline.
        elif (
            cube_config_minor_version
            and cube_config_minor_version >= 1
            and isinstance(self.code_list, dict)
        ):
            deserialiser = get_code_list_versioned_deserialiser(
                self.code_list,
                default_schema_uri=LATEST_V1_CODELIST_SCHEMA_URL
                if cube_config_minor_version < 5
                else LATEST_V2_CODELIST_SCHEMA_URL,
            )

            (
                new_code_list,
                json_schema_validation_errors,
                _,
            ) = deserialiser(self.code_list)

            return (new_code_list, json_schema_validation_errors)
        else:
            raise ValueError(f"Unmatched code_list value {self.code_list}")

    @staticmethod
    def _get_date_time_code_list_for_dimension(
        new_dimension: NewQbDimension, cell_uri_template: str, csv_column_title: str
    ) -> CompositeQbCodeList:
        csvw_safe_column_title = csvw_column_name_safe(csv_column_title)
        assert isinstance(new_dimension.code_list, NewQbCodeList)

        return CompositeQbCodeList(
            CatalogMetadata(new_dimension.label),
            [
                DuplicatedQbConcept(
                    existing_concept_uri=uritemplate.expand(
                        cell_uri_template,
                        {csvw_safe_column_title: c.label},
                    ),
                    label=c.label,
                    code=c.code,
                )
                for c in new_dimension.code_list.concepts
                if isinstance(c, NewQbConcept)
            ],
        )


@dataclass
class ExistingDimension(SchemaBaseClass):
    from_existing: str
    cell_uri_template: Optional[str] = None

    def map_to_existing_qb_dimension(self) -> ExistingQbDimension:
        return ExistingQbDimension(dimension_uri=self.from_existing)


@dataclass
class AttributeValue(SchemaBaseClass):
    label: str
    description: Optional[str] = None
    from_existing: Optional[str] = None
    definition_uri: Optional[str] = None


@dataclass
class ExistingAttributeLiteral(SchemaBaseClass):
    data_type: str
    from_existing: str
    required: bool = False
    describes_observations: Optional[str] = None

    def map_to_existing_qb_attribute(self) -> ExistingQbAttributeLiteral:
        return ExistingQbAttributeLiteral(
            attribute_uri=self.from_existing,
            is_required=self.required,
            data_type=self.data_type,
            observed_value_col_title=self.describes_observations,
        )


@dataclass
class ExistingAttributeResource(SchemaBaseClass):
    from_existing: str
    values: Union[bool, List[AttributeValue]] = True
    required: bool = False
    cell_uri_template: Optional[str] = None
    describes_observations: Optional[str] = None

    def map_to_qb_attribute(
        self, data: PandasDataTypes, column_title: str
    ) -> QbAttribute:
        if self.cell_uri_template:
            if isinstance(self.values, bool):
                _logger.warning(
                    "Attribute values for %s will not be created as `cell_uri_template` is set",
                    column_title,
                )
                return ExistingQbAttribute(
                    attribute_uri=self.from_existing,
                    is_required=self.required,
                    observed_value_col_title=self.describes_observations,
                )
            raise ValueError(
                "Conflict between `cell_uri_template` and list of attribute values provided for %s",
                column_title,
            )
        else:
            if isinstance(self.values, bool) and not self.values:
                raise ValueError(
                    "`values` should be set to `true` or defined inline, or `cell_uri_template` should be provided for %s",
                    column_title,
                )
            # `values` defaults to `true` so if it isn't defined in the column config, an ExistingAttributeResource is mapped to a NewQbAttribute with a codelist generated from the column data
            elif isinstance(self.values, bool) and self.values:
                return NewQbAttribute.from_data(
                    label=column_title,
                    csv_column_title=column_title,
                    data=data,
                    values=_get_new_attribute_values(
                        data=data, new_attribute_values=self.values
                    ),
                    parent_attribute_uri=self.from_existing,
                    is_required=self.required,
                    observed_value_col_title=self.describes_observations,
                )
            else:
                # `values` is a list of AttributeValue objects
                return NewQbAttribute(
                    label=column_title,
                    code_list=NewQbCodeList(
                        CatalogMetadata(column_title),
                        concepts=_get_new_attribute_values(data, self.values),
                    ),
                    parent_attribute_uri=self.from_existing,
                    is_required=self.required,
                    observed_value_col_title=self.describes_observations,
                )


@dataclass
class NewAttributeLiteral(SchemaBaseClass):
    data_type: str
    from_existing: Optional[str] = None
    required: bool = False
    describes_observations: Optional[str] = None
    label: Optional[str] = None
    description: Optional[str] = None
    definition_uri: Optional[str] = None

    def map_to_new_qb_attribute(self, column_title: str) -> NewQbAttributeLiteral:
        label = self.label or column_title

        return NewQbAttributeLiteral(
            label=label,
            description=self.description,
            data_type=self.data_type,
            parent_attribute_uri=self.from_existing,
            source_uri=self.definition_uri,
            is_required=self.required,
            observed_value_col_title=self.describes_observations,
        )


@dataclass
class NewAttributeResource(SchemaBaseClass):
    label: Optional[str] = None
    description: Optional[str] = None
    definition_uri: Optional[str] = None
    from_existing: Optional[str] = None
    values: Union[bool, List[AttributeValue]] = True
    required: bool = False
    cell_uri_template: Optional[str] = None
    describes_observations: Optional[str] = None

    def map_to_new_qb_attribute(
        self, column_title: str, data: PandasDataTypes
    ) -> NewQbAttribute:
        label = self.label or column_title

        if self.cell_uri_template:
            if isinstance(self.values, bool):
                _logger.warning(
                    "Attribute values for %s will not be created as `cell_uri_template` is set",
                    column_title,
                )
                return NewQbAttribute(
                    label=label,
                    description=self.description,
                    parent_attribute_uri=self.from_existing,
                    source_uri=self.definition_uri,
                    is_required=self.required,
                    observed_value_col_title=self.describes_observations,
                )

            raise ValueError(
                "Conflict between `cell_uri_template` and list of attribute values provided for %s",
                column_title,
            )
        else:
            if isinstance(self.values, bool) and not self.values:
                raise ValueError(
                    "`values` should be set to `true` or defined inline, or `cell_uri_template` should be provided for %s",
                    column_title,
                )
            # `values` defaults to `true` so if it isn't defined in the column config, an NewAttributeResource is mapped to a NewQbAttribute with a codelist generated from the column data
            elif isinstance(self.values, bool) and self.values:
                return NewQbAttribute.from_data(
                    label=label,
                    csv_column_title=column_title,
                    data=data,
                    values=_get_new_attribute_values(
                        data=data, new_attribute_values=self.values
                    ),
                    description=self.description,
                    parent_attribute_uri=self.from_existing,
                    source_uri=self.definition_uri,
                    is_required=self.required,
                    observed_value_col_title=self.describes_observations,
                )
            else:
                # `values` is a list of AttributeValue objects
                return NewQbAttribute(
                    label=label,
                    description=self.description,
                    code_list=NewQbCodeList(
                        CatalogMetadata(label),
                        concepts=_get_new_attribute_values(data, self.values),
                    ),
                    parent_attribute_uri=self.from_existing,
                    source_uri=self.definition_uri,
                    is_required=self.required,
                    observed_value_col_title=self.describes_observations,
                )


@dataclass
class Unit(SchemaBaseClass):
    label: str
    description: Optional[str] = None
    from_existing: Optional[str] = None
    definition_uri: Optional[str] = None
    scaling_factor: Optional[float] = None
    si_scaling_factor: Optional[float] = None
    quantity_kind: Optional[str] = None


@dataclass
class ExistingUnits(SchemaBaseClass):
    cell_uri_template: str
    describes_observations: Optional[str] = None

    def map_to_existing_qb_multi_units(
        self, data: PandasDataTypes, column_title: str
    ) -> QbMultiUnits:
        return QbMultiUnits.existing_units_from_data(
            data,
            csvw_column_name_safe(column_title),
            self.cell_uri_template,
            observed_value_col_title=self.describes_observations,
        )


@dataclass
class NewUnits(SchemaBaseClass):
    values: Union[bool, List[Unit]] = True
    describes_observations: Optional[str] = None

    def map_to_new_qb_multi_units(self, data: PandasDataTypes) -> QbMultiUnits:
        if isinstance(self.values, bool) and self.values is True:
            return QbMultiUnits.new_units_from_data(
                data, observed_value_col_title=self.describes_observations
            )

        elif isinstance(self.values, list):
            units = []
            for unit in self.values:
                if not isinstance(unit, Unit):
                    raise ValueError(f"Unexpected unit value: {unit}")

                units.append(_map_unit(unit))

            return QbMultiUnits(units)

        raise ValueError(f"Unhandled units 'values': {self}")


@dataclass
class Measure(SchemaBaseClass):
    label: str
    description: Optional[str] = None
    from_existing: Optional[str] = None
    definition_uri: Optional[str] = None

    def map_to_measure(self) -> NewQbMeasure:
        return NewQbMeasure(
            label=self.label,
            description=self.description,
            parent_measure_uri=self.from_existing,
            source_uri=self.definition_uri,
        )


@dataclass
class NewMeasures(SchemaBaseClass):
    values: Union[bool, List[Measure]] = True

    def map_to_new_multi_measure_dimension(
        self, data: PandasDataTypes
    ) -> QbMultiMeasureDimension:
        # When values is a single bool True then create new Measures from the csv column data
        if self.values is True:
            return QbMultiMeasureDimension.new_measures_from_data(data)

        elif isinstance(self.values, list):
            new_measures = []
            for new_measure in self.values:
                if not isinstance(new_measure, Measure):
                    raise ValueError(f"Unexpected measure: {new_measure}")
                new_measures.append(new_measure.map_to_measure())

            return QbMultiMeasureDimension(new_measures)

        else:
            raise ValueError(f"Unexpected measure 'values': {self.values}")


@dataclass
class ExistingMeasures(SchemaBaseClass):
    cell_uri_template: str

    def map_to_existing_multi_measure_dimension(
        self, column_title: str, data: PandasDataTypes
    ) -> QbMultiMeasureDimension:
        csvw_column_name = csvw_column_name_safe(column_title)
        return QbMultiMeasureDimension.existing_measures_from_data(
            data, csvw_column_name, self.cell_uri_template
        )


@dataclass
class ObservationValue(SchemaBaseClass):
    data_type: str = "decimal"
    unit: Union[None, str, Unit] = None
    measure: Union[None, str, Measure] = None

    def map_to_qb_observation(self) -> QbObservationValue:
        unit = None
        if isinstance(self.unit, str):
            unit = ExistingQbUnit(unit_uri=self.unit)

        elif isinstance(self.unit, Unit):
            unit = _map_unit(self.unit)

        elif self.unit is not None:
            raise ValueError(f"Unexpected unit: {self.unit}")

        if self.measure is None:
            # Standard shape cube
            return QbObservationValue(data_type=self.data_type, unit=unit)
        else:
            # Pivoted shape cube
            measure = None
            if isinstance(self.measure, str):
                measure = ExistingQbMeasure(self.measure)

            elif isinstance(self.measure, Measure):
                measure = _map_measure(self.measure)

            else:
                raise ValueError(f"Unhandled measure type: {self.measure}")

            return QbObservationValue(
                measure=measure, unit=unit, data_type=self.data_type or "decimal"
            )


def _map_unit(resource: Unit) -> NewQbUnit:
    return NewQbUnit(
        label=resource.label,
        description=resource.description,
        source_uri=resource.from_existing,
        base_unit=(
            None
            if resource.from_existing is None
            else ExistingQbUnit(resource.from_existing)
        ),
        base_unit_scaling_factor=_get_unit_scaling_factor(resource),
        qudt_quantity_kind_uri=resource.quantity_kind,
        si_base_unit_conversion_multiplier=resource.si_scaling_factor,
    )


def _map_measure(resource: Measure) -> NewQbMeasure:
    return NewQbMeasure(
        label=resource.label,
        description=resource.description,
        source_uri=resource.definition_uri,
        parent_measure_uri=resource.from_existing,
    )


def _get_unit_scaling_factor(unit: Unit) -> Optional[float]:
    """
    If the user wishes to, they should be able to specify the scaling factor (if relevant),
    but if they don't provide it we should just assume that it is 1
    (i.e. there is a one-to-one relationship between the existing unit and their new more specialised unit).
    If the unit is not derived from an existing unit, there will be not scaling factor.
    """
    if unit.from_existing is None:
        return None
    elif unit.scaling_factor is None:
        return EXISTING_UNIT_DEFAULT_SCALING_FACTOR
    else:
        return unit.scaling_factor


def _map_attribute_values(
    new_attribute_values_from_schema: List[AttributeValue],
) -> List[NewQbConcept]:
    new_attribute_values = []
    for attr_val in new_attribute_values_from_schema:
        if not isinstance(attr_val, AttributeValue):
            raise ValueError(f"Found unexpected attribute value {attr_val}")

        new_attribute_values.append(
            NewQbConcept(
                label=attr_val.label,
                description=attr_val.description,
                parent_code=attr_val.from_existing,
                # attr_val.definition_uri unused here
            )
        )
    return new_attribute_values


def _get_new_attribute_values(
    data: PandasDataTypes,
    new_attribute_values: Union[bool, List[AttributeValue]],
) -> List[NewQbConcept]:
    """
    Returns a list of NewQbConcept objects from a list of AttributeValue objects. If new_attribute_values is True, then the list is created with
    the list comprehension. If new_attribute_values is a list object then use _map_attribute_values.
    """
    if isinstance(new_attribute_values, bool):
        if new_attribute_values:
            columnar_data: List[str] = [
                v for v in pandas_input_to_columnar_optional_str(data) if v is not None
            ]
            return [NewQbConcept(v) for v in sorted(set(columnar_data))]

        return []
    elif isinstance(new_attribute_values, list):
        return _map_attribute_values(new_attribute_values)

    raise ValueError(
        f"Unexpected value for 'newAttributeValues': {new_attribute_values}"
    )
