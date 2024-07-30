"""
CSV-W
-----

Utils for working with CSV-Ws.
"""
import json
import logging
from pathlib import Path
from typing import List, Set, Union

from csvcubed.utils.rdf import parse_graph_retain_relative

from .uri import looks_like_uri

_logger = logging.getLogger(__name__)


def get_dependent_local_files(csvw_metadata_file: Path) -> Set[Path]:
    """
    N.B. this is a bit of a rough-and-ready function and may not catch *all* dependencies listed.
    However, it should work for the style of CSV-Ws that we currently generate.

    :return: a list of all of the local dependencies specified in a CSV-W file.
    """
    _logger.debug("Searching for local dependencies in CSV-W at %s", csvw_metadata_file)
    table_group = _load_table_group(csvw_metadata_file)

    base_path = _get_base_path(csvw_metadata_file.parent, table_group)
    if not isinstance(base_path, Path):
        _logger.debug(
            "CSV-W base path is a URI '%s'. There are no relatively defined local dependent files.",
            base_path,
        )
        return set()

    dependent_local_files: Set[Path] = _get_url_and_table_schema_path_for_table(
        base_path, table_group
    )

    tables: List[dict] = table_group.get("tables", [])
    for table in tables:
        dependent_local_files |= _get_url_and_table_schema_path_for_table(
            base_path, table
        )

    _logger.debug("Found dependent local files %s", dependent_local_files)
    return dependent_local_files


def _load_table_group(csvw_metadata_file: Path) -> dict:
    with open(csvw_metadata_file, "r") as f:
        table_group = json.load(f)
        assert isinstance(table_group, dict)
    return table_group


def _get_url_and_table_schema_path_for_table(base_path: Path, table: dict) -> Set[Path]:
    dependent_local_files = set()

    table_url = table.get("url")
    table_schema = table.get("tableSchema")

    if table_url is not None and str(table_url).strip() != "":
        table_url = str(table_url).strip()
        _logger.debug("Found CSV dependency (%s) in 'url' field.", table_url)
        if not looks_like_uri(table_url):
            dependent_local_files.add(base_path / table_url)
    if table_schema is not None and isinstance(table_schema, str):
        table_schema_path = table_schema.strip()
        _logger.debug(
            "Found table schema dependency (%s) in 'tableSchema' field.",
            table_schema_path,
        )
        if not looks_like_uri(table_schema_path):
            dependent_local_files.add(base_path / table_schema_path)

    return dependent_local_files


def _get_base_path(preliminary_base_path: Path, table_group: dict) -> Union[Path, str]:
    """
    :return: :obj:`pathlib.Path` (local file path) OR :obj:`str` (URI path)
    """
    context = table_group["@context"]
    if isinstance(context, list) and len(context) > 1:
        context_obj = context[1]
        assert isinstance(context_obj, dict)
        base = context_obj.get("@base")
        if base is not None and isinstance(base, str) and len(base.strip()) > 0:
            if looks_like_uri(base):
                # base path is a URI, so none of the files will be local.
                return base
            base_path = Path(base)
            if base_path.is_absolute():
                return base_path
            else:
                return preliminary_base_path / base
    return preliminary_base_path
