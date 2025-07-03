from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, TypeAlias, Union

import polars as pl
from polars.plugins import register_plugin_function

if TYPE_CHECKING:
    IntoExpr: TypeAlias = Union[pl.Expr, str, pl.Series]

LIB = Path(__file__).parent


def detect_lang(text: IntoExpr) -> pl.Expr:
    return register_plugin_function(
        args=[text],
        plugin_path=LIB,
        function_name="detect_lang",
        is_elementwise=True,
    )


__version__ = "0.1.0"
