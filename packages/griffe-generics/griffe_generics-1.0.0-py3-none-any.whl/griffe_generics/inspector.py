from __future__ import annotations

from collections import UserDict
from dataclasses import dataclass, field
from typing import Iterable, Union

from griffe import Class, ExprList, ExprName, ExprSubscript, ExprTuple, Module

from griffe_generics.traversal import descendant, walk_expressions, walk_objects
from griffe_generics.types import Expression
from griffe_generics.utils import canonical_path_of, type_path_of


@dataclass(frozen=True, slots=True)
class TypeParameter:
    name: ExprName
    cls: Class

    @property
    def type_path(self) -> str:
        return type_path_of(self.name, self.cls)

    @property
    def path(self) -> str:
        return f"{self.name.path}@{self.cls.name}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(path={self.path!r})"


@dataclass(frozen=True, slots=True)
class BoundType:
    expr: Expression
    cls: Class

    @property
    def type_path(self) -> str:
        return type_path_of(self.expr, self.cls)

    @property
    def path(self) -> str:
        if isinstance(self.expr, str):
            return self.expr

        return f"{self.expr.path}@{self.cls.name}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(path={self.path!r})"


class BoundTypes(UserDict[str, BoundType]):
    def resolve(self, expr: Expression, cls: Class) -> Expression:
        type_path = type_path_of(expr, cls)
        if type_path not in self.data:
            return expr

        while type_path in self.data:
            bound_type = self.data[type_path]
            type_path = bound_type.type_path

        return bound_type.expr


@dataclass(frozen=True, slots=True)
class GenericsContext:
    type_parameters_by_class: dict[str, list[TypeParameter]] = field(default_factory=dict)
    bound_types_by_class: dict[str, dict[str, BoundType]] = field(default_factory=dict)

    def is_generic_class(self, cls: Union[Expression, Class]) -> bool:
        return canonical_path_of(cls) in self.type_parameters_by_class

    def type_parameters_from_class(self, cls: Class) -> Iterable[TypeParameter]:
        for base_cls in [cls, *cls.mro()]:
            yield from self.type_parameters_by_class.get(base_cls.canonical_path, [])

    def bound_types_from_class(self, cls: Class) -> BoundTypes:
        bound_types = BoundTypes()
        for base_cls in [cls, *cls.mro()]:
            bound_types.update(self.bound_types_by_class.get(base_cls.canonical_path, {}).items())

        return bound_types


class GenericsInspector:
    def inspect(self, module: Module) -> GenericsContext:
        context = GenericsContext()

        for cls in walk_objects(module, Class):
            parameters = [*self._inspect_type_parameters(cls)]
            if parameters:
                context.type_parameters_by_class[cls.canonical_path] = [*parameters]

        for cls in walk_objects(module, Class):
            bound_types = dict(self._inspect_bound_types(cls, context))
            if bound_types:
                context.bound_types_by_class[cls.canonical_path] = bound_types

        return context

    def _inspect_type_parameters(self, cls: Class) -> Iterable[TypeParameter]:
        for base in cls.bases:
            for subscript in walk_expressions(base, ExprSubscript):
                if subscript.canonical_name not in {"Generic", "Protocol"}:
                    continue

                for name in walk_expressions(subscript.slice, ExprName):
                    yield TypeParameter(name=name, cls=cls)

    def _inspect_bound_types(self, cls: Class, context: GenericsContext) -> Iterable[tuple[str, BoundType]]:
        for base in cls.bases:
            subscript = descendant(base, ExprSubscript)
            if subscript is None:
                continue

            left, slice = subscript.left, subscript.slice

            path = canonical_path_of(left)
            if not context.is_generic_class(path):
                continue

            bound_types = slice.elements if isinstance(slice, (ExprTuple, ExprList)) else [slice]
            for parameter, bound_type in zip(context.type_parameters_by_class[path], bound_types):
                yield parameter.type_path, BoundType(expr=bound_type, cls=cls)
