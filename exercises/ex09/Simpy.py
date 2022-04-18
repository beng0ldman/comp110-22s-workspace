"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730359525"


class Simpy:
    """Simpy class."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Initializing simpy object."""
        self.values = values
    
    def __str__(self) -> str:
        """Creating str representation of object."""
        return f"Simpy({self.values})"

    def fill(self, fill_value: float, quantity: int) -> None:
        """Filling simpy object with inputted float value quantity times."""
        self.values = []
        while quantity > 0:
            self.values.append(fill_value)
            quantity -= 1
        return

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Placing a range of float values in a simpy object with an interval of step."""
        assert step != 0
        self.values = []
        while abs(start) < abs(stop):
            self.values.append(start)
            start += step
        return

    def sum(self) -> float:
        """Adding together values in the simpy object."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adding together either two simpy objects or a float uniformally across a simpy object."""
        answer: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                answer.values.append(value + rhs)
            return answer
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                answer.values.append(self.values[i] + rhs.values[i])
                i += 1
            return answer

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Applying an exponent uniformally to a simpy object, or putting a simpy object to the power of the corresponding values of another simpy object."""
        answer: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                answer.values.append(value ** rhs)
            return answer
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                answer.values.append(self.values[i] ** rhs.values[i])
                i += 1
            return answer

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Creating a list of bools regarding the equal value of corresponding values in two simpy objects."""
        answer: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                if value == rhs:
                    answer.append(True)
                else:
                    answer.append(False)
            return answer
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    answer.append(True)
                    i += 1
                else:
                    answer.append(False)
                    i += 1
            return answer
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Evaluating whether or not a value in a simpy object is > another value. The other value is either uniform or the corresponding value from another simpy object."""
        answer: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                if value > rhs:
                    answer.append(True)
                else:
                    answer.append(False)
            return answer
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    answer.append(True)
                    i += 1
                else:
                    answer.append(False)
                    i += 1
            return answer

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Operator overload allowing for subscription notation (indexing) and allowing for selection of simpy object values based on a corresponding list of bools."""
        if isinstance(rhs, int):
            list: list[float] = []
            for value in self.values:
                list.append(value)
            answer: float = list[rhs]
            return answer
        else:
            answer2: Simpy = Simpy([])
            assert len(self.values) == len(rhs)
            i: int = 0
            for value in self.values:
                if rhs[i] is True:
                    answer2.values.append(value)
                i += 1
            return answer2