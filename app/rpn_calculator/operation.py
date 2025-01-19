import math
from abc import ABC, abstractmethod
from typing import List


class Operation(ABC):
    @abstractmethod
    def execute(self, stack: List[float]) -> None:
        """Executes the operation and updates the stack."""
        pass


class AddOperation(Operation):
    def execute(self, stack: List[float]) -> None:
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)


class SubtractOperation(Operation):
    def execute(self, stack: List[float]) -> None:
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)


class MultiplyOperation(Operation):
    def execute(self, stack: List[float]) -> None:
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)


class DivideOperation(Operation):
    def execute(self, stack: List[float]) -> None:
        b = stack.pop()
        a = stack.pop()
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        stack.append(a / b)


class SquareRootOperation(Operation):
    def execute(self, stack: List[float]) -> None:
        a = stack.pop()
        if a < 0:
            raise ValueError("Cannot compute the square root of a negative number.")
        stack.append(math.sqrt(a))
