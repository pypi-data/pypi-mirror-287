from __future__ import annotations

from typing import Callable, Optional, Sequence, Type, TypeVar

from typing_extensions import TypeGuard

from griffe_generics.traversal import iter_children_from_expression
from griffe_generics.types import Expression

T = TypeVar("T")
E = TypeVar("E", bound=Expression)


def transform_expression(
    expression: Expression,
    predicate: Callable[[Expression], TypeGuard[E]],
    func: Callable[[E], Optional[Expression]],
) -> Expression:
    if predicate(expression):
        transformed = func(expression)
        if transformed is not None:
            expression = transformed

    for key, node in iter_children_from_expression(expression):
        if isinstance(node, Sequence):
            if isinstance(node, str):
                continue

            setattr(expression, key, [transform_expression(child, predicate=predicate, func=func) for child in node])
        else:
            setattr(expression, key, transform_expression(node, predicate=predicate, func=func))

    return expression


def transform_expression_of(
    expression: Expression,
    type: Type[E],
    func: Callable[[E], Optional[Expression]],
) -> Expression:
    def predicate(expression: Expression) -> TypeGuard[E]:
        return isinstance(expression, type)

    return transform_expression(expression, predicate=predicate, func=func)
