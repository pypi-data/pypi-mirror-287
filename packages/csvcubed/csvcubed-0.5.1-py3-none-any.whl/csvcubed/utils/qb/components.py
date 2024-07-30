"""
Cube Components
---------------

Utilities to help when handling qube components data.
"""

import os
from enum import Enum
from pathlib import Path
from urllib.parse import urlparse

from csvcubed.definitions import QB_MEASURE_TYPE_DIMENSION_URI, SDMX_ATTRIBUTE_UNIT_URI
from csvcubed.models.csvcubedexception import UnsupportedComponentPropertyTypeException
from csvcubed.utils.uri import file_uri_to_path


class ComponentField(Enum):
    """
    The fields of `QubeComponentResult` model that are relevant for filtering the `QubeComponentsResult`.
    """

    Property = "property"

    PropertyType = "property_type"


class ComponentPropertyAttributeURI(Enum):
    """
    The uris of component attributes.
    """

    UnitMeasure = SDMX_ATTRIBUTE_UNIT_URI

    MeasureType = QB_MEASURE_TYPE_DIMENSION_URI


class ComponentPropertyTypeURI(Enum):
    """
    The type uris of component properties.
    """

    Dimension = "http://purl.org/linked-data/cube#DimensionProperty"
    """ The component is of type qb:Dimension. """

    Attribute = "http://purl.org/linked-data/cube#AttributeProperty"
    """ The component is of type qb:Attribute. """

    Measure = "http://purl.org/linked-data/cube#MeasureProperty"
    """ The component is of type qb:Measure. """


class ComponentPropertyType(Enum):
    """
    The type of component properties.
    """

    Dimension = "Dimension"
    """ The component is of type qb:Dimension. """

    Attribute = "Attribute"
    """ The component is of type qb:Attribute. """

    Measure = "Measure"
    """ The component is of type qb:Measure. """


class EndUserColumnType(Enum):
    """These are the column types tha a User is familiar form the qube-config.json"""

    Dimension = "Dimension"
    """ The column holds values for a Dimension """

    Attribute = "Attribute"
    """ The column holds values for an Attribute """

    Measures = "Measures"
    """ The column holds the measure for each Observation """

    Units = "Units"
    """ The column holds the unit for each Observation """

    Observations = "Observations"
    """ The column holds the Observed values """

    Suppressed = "Suppressed"
    """ The column holds values which are not part of the cube"""


def get_component_property_type(property_type: str) -> str:
    """
    Produces the user-friendly name of component property type.

    Member of :file:`./utils/qb/components.py`

    :return: `str` - user-friendly name of component property type.
    """
    if ComponentPropertyTypeURI.Dimension.value == property_type:
        return ComponentPropertyType.Dimension.value
    elif ComponentPropertyTypeURI.Attribute.value == property_type:
        return ComponentPropertyType.Attribute.value
    elif ComponentPropertyTypeURI.Measure.value == property_type:
        return ComponentPropertyType.Measure.value
    else:
        raise UnsupportedComponentPropertyTypeException(property_type=property_type)


def get_component_property_as_relative_path(
    input_file_path: Path, component_property: str
) -> str:
    """
    Produces the user-friendly property of the component property.

    Member of :file:`./utils/qb/components.py`

    :return: `str` - url or relative path
    """
    if not component_property.startswith("file://"):
        return component_property

    if not input_file_path.is_absolute():
        input_file_path = input_file_path.absolute()

    try:
        return _relative_path(component_property, input_file_path.parent)
    except Exception:
        return component_property


def _relative_path(path_uri: str, relative_to: Path) -> str:
    """
    Unfortunately, `os.path.relpath` on Windows alters any `/` chars in the fragment part of a URI to the backslash
     char.

    This function ensures that we don't pass the fragment part of the URI to `os.path.relpath` so it never gets mangled.
    """
    url = urlparse(path_uri)

    if len(url.fragment) > 0:
        fragment_part = "#" + url.fragment
        file_path = file_uri_to_path(path_uri.removesuffix(fragment_part))
        relative_file_path: str = os.path.relpath(file_path, relative_to)
        return relative_file_path + fragment_part

    return os.path.relpath(path_uri, relative_to)
