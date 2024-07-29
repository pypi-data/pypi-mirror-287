from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

from narwhals.dependencies import get_dask_expr

if TYPE_CHECKING:
    from narwhals._dask.dataframe import DaskLazyFrame


def maybe_evaluate(df: DaskLazyFrame, obj: Any) -> Any:
    from narwhals._dask.expr import DaskExpr

    if isinstance(obj, DaskExpr):
        results = obj._call(df)
        if len(results) != 1:  # pragma: no cover
            msg = "Multi-output expressions not supported in this context"
            raise NotImplementedError(msg)
        result = results[0]
        if not get_dask_expr()._expr.are_co_aligned(
            df._native_dataframe._expr, result._expr
        ):  # pragma: no cover
            # are_co_aligned is a method which cheaply checks if two Dask expressions
            # have the same index, and therefore don't require index alignment.
            # If someone only operates on a Dask DataFrame via expressions, then this
            # should always be the case: expression outputs (by definition) all come from the
            # same input dataframe, and Dask Series does not have any operations which
            # change the index. Nonetheless, we perform this safety check anyway.

            # However, we still need to carefully vet which methods we support for Dask, to
            # avoid issues where `are_co_aligned` doesn't do what we want it to do:
            # https://github.com/dask/dask-expr/issues/1112.
            msg = "Implicit index alignment is not support for Dask DataFrame in Narwhals"
            raise NotImplementedError(msg)
        return result
    return obj


def parse_exprs_and_named_exprs(
    df: DaskLazyFrame, *exprs: Any, **named_exprs: Any
) -> dict[str, Any]:
    results = {}
    for expr in exprs:
        _results = expr._call(df)
        for _result in _results:
            results[_result.name] = _result
    for name, value in named_exprs.items():
        _results = value._call(df)
        if len(_results) != 1:  # pragma: no cover
            msg = "Named expressions must return a single column"
            raise AssertionError(msg)
        results[name] = _results[0]
    return results
