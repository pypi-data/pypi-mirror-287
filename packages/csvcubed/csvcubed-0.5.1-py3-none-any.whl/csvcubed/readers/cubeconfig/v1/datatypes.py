from pathlib import Path
from typing import Dict, List, Optional, Union

import pandas as pd

from csvcubed.models.csvcubedexception import UnsupportedColumnDefinitionException
from csvcubed.models.cube.qb.components.constants import ACCEPTED_DATATYPE_MAPPING
from csvcubed.readers.cubeconfig.v1.mapcolumntocomponent import (
    _from_column_dict_to_schema_model,
    schema,
)
from csvcubed.readers.preconfiguredtemplates import (
    apply_preconfigured_values_from_template,
)

from .constants import CONVENTION_NAMES


def _is_conventional_measures_column(column_label: str) -> bool:
    """
    Does the column label signify a measure column using the configuration
    by convention approach.
    """
    return column_label in CONVENTION_NAMES["measures"]


def _is_conventional_observations_column(column_label: str) -> bool:
    """
    Does the column label signify an observation column using the configuration
    by convention approach.
    """
    return column_label in CONVENTION_NAMES["observations"]


def _is_conventional_units_column(column_label: str) -> bool:
    """
    Does the column label signify a units column using the configuration by
    convention approach.
    """
    return column_label in CONVENTION_NAMES["units"]


def pandas_datatypes_from_columns_config(
    columns_config: Dict[str, Union[Dict, bool]]
) -> Dict[str, str]:
    """
    Given a dictionary of column config in the form:

    "Column Name": {
        <COLUMN CONFIG DICT>
    }

    Returns a dictionary mapping column names to pandas
    datatypes (which are declared via strings)
    """

    dtype = {}
    for column_label, column_config in columns_config.items():
        """
        If the column is suppressed using below notation, it will be ignored.

        {"column_name": false}
        """
        if type(column_config) is bool and not column_config:
            # This column is being suppressed. Hence, the contents from the config is kept as is.
            dtype[column_label] = "string"
        elif isinstance(column_config, dict):
            apply_preconfigured_values_from_template(column_config, column_label)
            known_schema: schema.SchemaBaseClass = _from_column_dict_to_schema_model(
                column_label, column_config
            )
            dtype[column_label] = pandas_dtype_from_schema(known_schema)
        else:
            raise UnsupportedColumnDefinitionException(column_title=column_label)

    return dtype


def pandas_dtype_from_schema(known_schema: schema.SchemaBaseClass) -> str:
    """
    Given a schema, return the appropriate pandas datatype
    """

    if isinstance(
        known_schema,
        (
            schema.NewAttributeLiteral,
            schema.ExistingAttributeLiteral,
            schema.ObservationValue,
        ),
    ):
        return ACCEPTED_DATATYPE_MAPPING[known_schema.data_type]

    return "string"


def get_pandas_datatypes(
    csv_path: Path, config: Optional[dict] = None
) -> Dict[str, str]:
    """
    Creates a dictionary of column_label:datatype for all columns in the dataframe.
    """

    dtype = {}  # Mapping of column name to pandas datatype

    # Columns defined by explicit configuration
    if config:
        if "columns" in config:
            dtype = pandas_datatypes_from_columns_config(config["columns"])

    # Columns configured by convention
    column_list: List[str] = pd.read_csv(csv_path, nrows=0).columns.tolist()  # type: ignore
    untyped_column_list: List[str] = [x for x in column_list if x not in dtype]
    for uc in untyped_column_list:
        if _is_conventional_measures_column(uc.lower()):
            dtype[uc] = ACCEPTED_DATATYPE_MAPPING["string"]
        elif _is_conventional_units_column(uc.lower()):
            dtype[uc] = ACCEPTED_DATATYPE_MAPPING["string"]
        elif _is_conventional_observations_column(uc.lower()):
            dtype[uc] = ACCEPTED_DATATYPE_MAPPING["decimal"]
        else:
            # therefore, is a dimension
            dtype[uc] = ACCEPTED_DATATYPE_MAPPING["string"]

    return dtype
