"""case-insensitive :class:`collections.abc.Mapping`."""

from __future__ import annotations

import re
from collections import OrderedDict
from collections.abc import Mapping
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


class CaseInsensitiveMapping(Mapping[str, str]):
    """A case-insensitive :class:`collections.abc.Mapping` object."""

    def __init__(self, data: Mapping[str, str] | None = None, **kwargs: str) -> None:
        """Instantiate class."""
        data = {} if data is None else {k.lower(): v for k, v in data.items()}
        self._store = OrderedDict(data)
        self._store.update(**{k.lower(): v for k, v in kwargs.items()})

    def __getitem__(self, key: str) -> str:
        """Get value from object, ignoring case."""
        return self._store[key.lower()]

    def __hash__(self) -> int:
        """Make the object hashable."""
        return hash(frozenset(self.items()))

    def __iter__(self) -> Generator[str, str, None]:
        """Iterate over object."""
        yield from iter(self._store)

    def __len__(self) -> int:
        """Length of object."""
        return len(self._store)

    def find_value(self, value: re.Pattern[str] | str) -> CaseInsensitiveMapping:
        """Find value."""
        value_pattern = re.compile(re.escape(value)) if isinstance(value, str) else value
        rv: OrderedDict[str, str] = OrderedDict()
        for k, v in self.items():
            if value_pattern.match(v):
                rv[k] = v
        return CaseInsensitiveMapping(rv)
