"""External link checker."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from docutils.nodes import paragraph, reference, substitution_reference
from docutils.utils import new_document
from sphinx.transforms import SphinxTransform
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging
from sphinx.util.docutils import LoggingReporter

from ._case_insensitive_mapping import CaseInsensitiveMapping
from .constants import COMMON_LINKS

if TYPE_CHECKING:
    from docutils.nodes import Node, document

LOGGER = logging.getLogger(__name__)


class ExternalLinkChecker(SphinxPostTransform):
    """Check each external link to see if it can be replaced with a reference."""

    _external_links: CaseInsensitiveMapping
    default_priority = 501

    def run(self, **_kwargs: object) -> None:
        """Main method of post transforms."""
        if not self.config.external_links_detect_hardcoded_links:
            return

        self._external_links = CaseInsensitiveMapping(
            COMMON_LINKS, **self.app.config.external_links
        )
        for refnode in self.document.findall(reference):
            self.check_reference(refnode)

    def check_reference(self, ref_node: reference) -> None:
        """Check if the reference can be replaced.

        Args:
            links: Mapping of referencable links.
            ref_node: The reference node to check.

        """
        if "internal" in ref_node or "refuri" not in ref_node:
            return

        matches = self._external_links.find_value(
            re.compile(re.escape(ref_node["refuri"]) + r"?(/)$")
        )
        if not matches:
            return

        LOGGER.warning(
            'hardcoded link "%s" to %s could be replaced by a reference (%s)',
            ref_node.astext(),
            ref_node["refuri"],
            ", ".join(self.make_suggestions(matches, ref_node)),
            location=ref_node,
        )

    def make_suggestions(self, matches: CaseInsensitiveMapping, ref_node: reference) -> list[str]:
        """Make suggestions based on matches."""
        title = ref_node.astext()
        rv: list[str] = []
        for k in matches:
            if not ref_node["refuri"].startswith(title) and title == k:
                rv.append(f":link:`{k}`")
            else:
                rv.append(f":link:`{title} <{k}>`")
        return rv


class GlobalSubstitutions(SphinxTransform):
    """Transform for global substitutions."""

    default_priority = 211

    def __init__(self, document: document, startnode: Node | None = None) -> None:
        super().__init__(document, startnode)
        self.parser = self.app.registry.create_source_parser(self.app, "rst")

    def apply(self) -> None:
        """Apply substitutions."""
        settings, source = self.document.settings, self.document["source"]
        subs = self.document.settings.env.config.external_links_substitutions
        to_handle = set(subs.keys()) - set(self.document.substitution_defs)

        for ref in self.document.findall(substitution_reference):
            refname = ref["refname"]
            if refname in to_handle:
                text = subs[refname]

                doc = new_document(source, settings)
                doc.reporter = LoggingReporter.from_reporter(doc.reporter)
                self.parser.parse(text, doc)

                substitution = doc.next_node()
                # Remove encapsulating paragraph
                if isinstance(substitution, paragraph):
                    substitution = substitution.next_node()
                ref.replace_self(substitution)
