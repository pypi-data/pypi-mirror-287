from __future__ import annotations

from typing import Optional

from griffe import Attribute, Class, ExprName, Extension, Function, Module

from griffe_generics.inspector import BoundTypes, GenericsContext, GenericsInspector
from griffe_generics.transforms import transform_expression_of
from griffe_generics.traversal import walk_objects
from griffe_generics.types import Expression
from griffe_generics.utils import deepcopy


class GenericsExtension(Extension):
    _context: GenericsContext

    def on_package_loaded(self, *, pkg: Module) -> None:
        self._context = GenericsInspector().inspect(pkg)

        for cls in walk_objects(pkg, Class):
            self._handle_class(cls)

    def _handle_class(self, cls: Class) -> None:
        bound_types = self._context.bound_types_from_class(cls)

        for base_cls in reversed(cls.mro()):
            for key, member in base_cls.members.items():
                if key in cls.members:
                    continue

                if isinstance(member, Function):
                    member = self._transform_function(member, base_cls, bound_types=bound_types)
                elif isinstance(member, Attribute):
                    member = self._transform_attribute(member, base_cls, bound_types=bound_types)

                cls.set_member(key, member)

    def _transform_function(self, function: Function, cls: Class, bound_types: BoundTypes) -> Function:
        function = deepcopy(function, shared={"parent"})

        for parameter in function.parameters:
            parameter.annotation = self._resolve_annotation(parameter.annotation, cls, bound_types)

        function.returns = self._resolve_annotation(function.returns, cls, bound_types)

        return function

    def _transform_attribute(self, attribute: Attribute, cls: Class, bound_types: BoundTypes) -> Attribute:
        attribute = deepcopy(attribute, shared={"parent"})
        attribute.annotation = self._resolve_annotation(attribute.annotation, cls, bound_types)
        return attribute

    def _resolve_annotation(
        self,
        annotation: Optional[Expression],
        cls: Class,
        bound_types: BoundTypes,
    ) -> Optional[Expression]:
        if annotation is None:
            return None

        return transform_expression_of(
            annotation,
            type=ExprName,
            func=lambda name: bound_types.resolve(name, cls),
        )
