from os import linesep
from typing import Dict, List

from pandas import DataFrame

from csvcubed.models.csvcubedexception import FailedToConvertDataFrameToStringException


def get_printable_list_str(items: List) -> str:
    """
    Converts the given list of items into a printable string representation.

    Member of :file:`./utils/printable`.

    :return: `str` - string representation of the given list
    """
    if len(items) == 0 or len(items[0]) == 0:
        return "None"

    output_str = ""
    for item in items:
        output_str = f"{output_str}{linesep}\t\t-- {item}"
    return output_str


def get_printable_tabular_str_from_list(items: List[Dict], column_names=None) -> str:
    """
    Converts the given list of items of {key, value} into a printable tabular.

    Member of :file:`./utils/printable`.

    :return: `str` - string representation of the given list
    """
    if len(items) == 0:
        return "None"

    df = DataFrame(items)
    if column_names:
        df.columns = column_names
    output_str = df.to_string(index=False)
    if output_str:
        return output_str
    raise FailedToConvertDataFrameToStringException()
