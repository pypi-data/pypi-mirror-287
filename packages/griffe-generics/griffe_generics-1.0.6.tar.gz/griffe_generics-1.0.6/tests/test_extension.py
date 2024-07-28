from __future__ import annotations

from griffe import Extensions, temporary_visited_package
from utils import annotations_from_function

from griffe_generics import GenericsExtension


def test_generics_extension() -> None:
    with temporary_visited_package(
        "package",
        modules={
            "__init__.py": """
                from typing import Generic, TypeVar

                A = TypeVar("A")
                B = TypeVar("B")
                C = TypeVar("C")


                class Parent(Generic[A, B, C]):
                    def p1(self, a: A) -> A:
                        return a

                    def p2(self, b: B) -> B:
                        return b

                    def p3(self, c: C) -> C:
                        return c


                class Intermediate(Parent[int, float, A], Generic[A]):
                    def i1(self, a: A) -> A:
                        return a


                class Child(Intermediate[Parent[int, float, int]]):
                    pass
            """,
        },
        extensions=Extensions(GenericsExtension()),
    ) as package:
        Parent = package["Parent"]
        assert tuple(annotations_from_function(Parent["p1"])) == ("None", "A", "A")
        assert tuple(annotations_from_function(Parent["p2"])) == ("None", "B", "B")
        assert tuple(annotations_from_function(Parent["p3"])) == ("None", "C", "C")

        Intermediate = package["Intermediate"]
        assert tuple(annotations_from_function(Intermediate["p1"])) == ("None", "int", "int")
        assert tuple(annotations_from_function(Intermediate["p2"])) == ("None", "float", "float")
        assert tuple(annotations_from_function(Intermediate["p3"])) == ("None", "A", "A")
        assert tuple(annotations_from_function(Intermediate["i1"])) == ("None", "A", "A")

        Child = package["Child"]
        assert tuple(annotations_from_function(Child["p1"])) == ("None", "int", "int")
        assert tuple(annotations_from_function(Child["p2"])) == ("None", "float", "float")
        assert tuple(annotations_from_function(Child["p3"])) == (
            "None",
            "Parent[int, float, int]",
            "Parent[int, float, int]",
        )
        assert tuple(annotations_from_function(Child["i1"])) == (
            "None",
            "Parent[int, float, int]",
            "Parent[int, float, int]",
        )
