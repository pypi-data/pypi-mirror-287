from __future__ import annotations

import copy
from typing import Any, Optional, TypeVar, Union

from griffe import Class, Expr, Object

from griffe_generics.types import Expression

T = TypeVar("T")


def canonical_path_of(expression: Union[Expression, Object]) -> str:
    return expression.canonical_path if isinstance(expression, (Expr, Object)) else expression


def type_path_of(expression: Expression, cls: Class) -> str:
    return f"{canonical_path_of(expression)}@{cls.canonical_path}"


def deepcopy(instance: T, shared: Optional[set[str]] = None) -> T:
    memo: dict[int, Any] = {}
    if shared is not None:
        for attribute in shared:
            value = getattr(instance, attribute)
            memo[id(value)] = value

    return copy.deepcopy(instance, memo=memo)
