"""
Code List Config
----------------

Models for representing code list config.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from csvcubedmodels.dataclassbase import DataClassBase

from csvcubed.models.codelistconfig.code_list_config_sort import (
    CodeListConfigSort,
    apply_sort_to_child_concepts,
    sort_concepts,
)
from csvcubed.models.cube.qb.catalog import CatalogMetadata
from csvcubed.models.cube.qb.components.concept import DuplicatedQbConcept, NewQbConcept
from csvcubed.readers.catalogmetadata.v1.catalog_metadata_reader import (
    metadata_from_dict,
)
from csvcubed.utils.json import load_json_document

CODE_LIST_CONFIG_V1_DEFAULT_URL = "https://purl.org/csv-cubed/code-list-config/v1"


@dataclass
class CodeListConfigConceptV1(DataClassBase):
    """Model for representing a code list concept in code list config."""

    label: str
    notation: str
    description: Optional[str] = field(default=None)
    sort_order: Optional[int] = field(default=None)
    same_as: Optional[str] = field(default=None)
    children: List["CodeListConfigConceptV1"] = field(default_factory=list)
    uri_safe_identifier_override: Optional[str] = field(default=None)


@dataclass
class CodeListConfigV1(DataClassBase):
    """Model for representing a code list config."""

    sort: Optional[CodeListConfigSort] = field(default=None)
    concepts: List[CodeListConfigConceptV1] = field(default_factory=list)
    schema: str = field(default=CODE_LIST_CONFIG_V1_DEFAULT_URL)
    # Using CatalogMetadata in the dataclass requires providing default_factory as otherwise, the metadata itself needs to be provided. Since we want have the metadata at initialisation, the default_factory below is defined.
    metadata: CatalogMetadata = field(
        default_factory=lambda: CatalogMetadata("Metadata")
    )

    def __post_init__(self):
        # Sorting top-level concepts.
        self.concepts = sort_concepts(self.concepts, self.sort)
        apply_sort_to_child_concepts(self.concepts, self)

    @classmethod
    def from_json_file(cls, file_path: Path) -> Tuple["CodeListConfigV1", Dict]:
        """
        Converts code list config json to `CodeListConfig`.
        """
        code_list_dict = load_json_document(file_path)
        schema = code_list_dict.get("$schema", CODE_LIST_CONFIG_V1_DEFAULT_URL)

        code_list_config = cls.from_dict(code_list_dict)
        code_list_config.schema = schema
        code_list_config.metadata = metadata_from_dict(code_list_dict)

        return (code_list_config, code_list_dict)

    @classmethod
    def from_dict(cls, code_list_dict: Dict) -> "CodeListConfigV1":
        """
        Converts code list config dict to `CodeListConfig`.
        """
        schema = code_list_dict.get("$schema", CODE_LIST_CONFIG_V1_DEFAULT_URL)

        code_list_config = super().from_dict(code_list_dict)
        code_list_config.schema = schema
        code_list_config.metadata = metadata_from_dict(code_list_dict)

        return code_list_config

    @property
    def new_qb_concepts(self) -> list[NewQbConcept]:
        """
        Converts concepts of type CodeListConfigConcept to concepts of type NewQbConcept whilst maintaining the hierarchy.
        """

        new_qb_concepts: list[NewQbConcept] = []
        if self.concepts:
            concepts_with_maybe_parent: list[
                Tuple[CodeListConfigConceptV1, Optional[CodeListConfigConceptV1]]
            ] = [(c, None) for c in self.concepts]

            for concept, maybe_parent_concept in concepts_with_maybe_parent:
                parent_code = (
                    maybe_parent_concept.notation if maybe_parent_concept else None
                )
                if concept.same_as:
                    new_qb_concepts.append(
                        DuplicatedQbConcept(
                            label=concept.label,
                            code=concept.notation,
                            parent_code=parent_code,
                            sort_order=concept.sort_order,
                            description=concept.description,
                            uri_safe_identifier_override=concept.uri_safe_identifier_override,
                            existing_concept_uri=concept.same_as,
                        )
                    )
                else:
                    new_qb_concepts.append(
                        NewQbConcept(
                            label=concept.label,
                            code=concept.notation,
                            parent_code=parent_code,
                            sort_order=concept.sort_order,
                            description=concept.description,
                            uri_safe_identifier_override=concept.uri_safe_identifier_override,
                        )
                    )
                if any(concept.children):
                    concepts_with_maybe_parent += [
                        (child, concept) for child in concept.children
                    ]

        return new_qb_concepts
