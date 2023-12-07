#!/usr/bin/env python3
"""add type annotations to the function"""

from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Get the value associated with the key in the dictionary,
    or return the default if key is not present."""
    if key in dct:
        return dct[key]
    else:
        return default
