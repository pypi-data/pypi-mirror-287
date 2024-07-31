"""Roles."""

from __future__ import annotations

import functools
from typing import TYPE_CHECKING, Any

from docutils.nodes import reference
from docutils.utils import unescape
from sphinx.util.nodes import split_explicit_title

from ._case_insensitive_mapping import CaseInsensitiveMapping
from .constants import COMMON_LINKS

if TYPE_CHECKING:
    from collections.abc import Sequence

    from docutils.nodes import Node, system_message
    from docutils.parsers.rst.states import Inliner
    from sphinx.util.typing import RoleFunction


@functools.cache
def _find_uri(links: CaseInsensitiveMapping, target: str) -> str:
    """Find URI with caching."""
    return links[target]


def links_role(user_links: dict[str, str] | None = None) -> RoleFunction:
    """Generate link role function, injecting user provided collection of links."""
    links = CaseInsensitiveMapping(COMMON_LINKS, **user_links if user_links else {})

    def role_func(
        role: str,  # noqa: ARG001
        rawtext: str,  # noqa: ARG001
        text: str,
        lineno: int,  # noqa: ARG001
        inliner: Inliner,  # noqa: ARG001
        options: dict[str, Any] | None = None,  # noqa: ARG001
        content: Sequence[str] = (),  # noqa: ARG001
    ) -> tuple[list[Node], list[system_message]]:
        """Implement role."""
        _has_explicit_title, title, target = split_explicit_title(unescape(text))
        node: Node = reference(
            title, title, internal=False, refuri=_find_uri(links, target.lower())
        )
        return [node], []

    return role_func
