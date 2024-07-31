"""Constants."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping


COMMON_LINKS: Mapping[str, str] = {
    "apache": "http://www.apache.org",
    "apple": "http://www.apple.com/",
    "black": "https://github.com/psf/black",
    "couchdb": "http://couchdb.apache.org/",
    "css": "http://www.w3.org/Style/CSS/",
    "debian": "https://www.debian.org/",
    "docker hub": "https://hub.docker.com/",
    "docker": "http://docker.io/",
    "gist": "https://gist.github.com/",
    "gitlab": "https://gitlab.com/",
    "google": "https://google.com/",
    "jinja": "http://jinja.pocoo.org/",
    "jinja2": "http://jinja.pocoo.org/",
    "linux": "https://www.kernel.org/",
    "macos": "http://www.apple.com/osx/",
    "microsoft": "http://microsoft.com/",
    "nginx": "http://nginx.org",
    "nix": "http://nixos.org/nix/",
    "npm": "https://www.npmjs.com/",
    "poetry": "https://github.com/python-poetry/poetry",
    "postgres": "http://www.postgresql.org/",
    "postgresql": "http://www.postgresql.org/",
    "pre-commit": "https://github.com/pre-commit/pre-commit",
    "pydantic": "https://github.com/pydantic/pydantic",
    "pypi": "https://pypi.org/",
    "pyright": "https://github.com/microsoft/pyright",
    "pytest": "https://github.com/pytest-dev/pytest/",
    "python": "https://www.python.org/",
    "rdt": "https://readthedocs.com/",
    "readthedocs": "https://readthedocs.com/",
    "restructuredtext": "https://docutils.sourceforge.io/rst.html",
    "rich": "https://github.com/Textualize/rich",
    "rst": "https://docutils.sourceforge.io/rst.html",
    "ruff": "https://github.com/astral-sh/ruff",
    "sphinx": "https://github.com/sphinx-doc/sphinx",
    "sqlite": "http://www.sqlite.org/",
    "test pypi": "https://test.pypi.org/",
    "typeshed": "https://github.com/python/typeshed",
    "ubuntu": "http://www.ubuntu.com/",
    "visual studio code": "https://code.visualstudio.com/",
    "vscode": "https://code.visualstudio.com/",
    "w3c": "http://www.w3.org/",
    "windows": "http://windows.microsoft.com/",
}
"""Mapping of common links."""
