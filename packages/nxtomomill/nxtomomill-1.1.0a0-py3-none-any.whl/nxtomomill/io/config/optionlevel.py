from __future__ import annotations

from copy import copy
from typing import Any
from silx.utils.enum import Enum as _Enum


class OptionLevel(_Enum):
    REQUIRED = "required"
    ADVANCED = "advanced"


def filter_options_level_items(
    dict_: dict[str, Any], level: OptionLevel, level_ref: dict[str, OptionLevel]
) -> dict[str, Any]:
    """
    Filer items in dict_ from there configuration level.

    :param dict_: dict that we want to filter. All possible keys must contained in `level_ref`. Else a KEyError exception will be raised.
    :param level: the OptionLevel we want to get. All keys which an higher option level will be removed from the dictionary
    :param level_ref: dict containing all possible dict_ keys with associated option level
    """
    res = copy(dict_)
    keys = tuple(res.keys())
    for key in keys:
        if level == OptionLevel.REQUIRED and level_ref[key] == OptionLevel.ADVANCED:
            del res[key]
    return res
