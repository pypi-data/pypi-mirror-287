from __future__ import annotations

from collections import deque
from dataclasses import fields
from typing import Callable, Iterable, Optional, Sequence, Type, TypeVar, Union

from griffe import Alias, Expr, Object

from griffe_generics.types import Expression

T = TypeVar("T")
O = TypeVar("O", bound=Object)  # noqa: E741
E = TypeVar("E", bound=Expression)


def iter_children_from_object(object: Object) -> Iterable[tuple[str, Object]]:
    for key in object.members.keys():
        value = object.get_member(key)

        if isinstance(value, Alias):
            continue

        yield key, value


def iter_children_from_expression(
    expression: Expression,
) -> Iterable[tuple[str, Union[Expression, Sequence[Expression]]]]:
    if not isinstance(expression, Expr):
        return

    for field in fields(expression):
        if field.name == "parent":
            continue

        value = getattr(expression, field.name)
        if isinstance(value, (str, Expr, Sequence)):
            yield field.name, value


def walk(
    node: T,
    iter_children: Callable[[T], Iterable[tuple[str, Union[T, Sequence[T]]]]],
) -> Iterable[T]:
    queue: deque[T] = deque([node])

    while queue:
        left = queue.popleft()

        for _, child in iter_children(left):
            if isinstance(child, Sequence):
                queue.extend(child)
            else:
                queue.append(child)

        yield left


def walk_objects(object: Object, type: Type[O]) -> Iterable[O]:
    for node in walk(object, iter_children_from_object):
        if isinstance(node, type):
            yield node


def walk_expressions(expression: Expression, type: Type[E]) -> Iterable[E]:
    for node in walk(expression, iter_children_from_expression):
        if isinstance(node, type):
            yield node


def descendant(expression: Expression, type: Type[E]) -> Optional[E]:
    try:
        return next(iter(walk_expressions(expression, type)))
    except StopIteration:
        return None
