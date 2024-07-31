"""Type definitions."""

from __future__ import annotations

from typing import TypedDict


class ExtensionMetadata(TypedDict, total=False):
    """The metadata returned by an extension's ``setup()`` function.

    Copy/paste for early use as it's staged for release in sphinx >7.2.6.

    """

    version: str
    """The extension version (default: ``'unknown version'``)."""

    env_version: int
    """An integer that identifies the version of env data added by the extension."""

    parallel_read_safe: bool
    """Indicate whether parallel reading of source files is supported
    by the extension.

    """

    parallel_write_safe: bool
    """Indicate whether parallel writing of output files is supported
    by the extension (default: ``True``).

    """
