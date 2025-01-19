import re
from typing import Dict

from app.rpn_calculator.operation import Operation, AddOperation, SubtractOperation, MultiplyOperation, DivideOperation, SquareRootOperation

class RPNCalculator:
    def __init__(self):
        self.operations: Dict[str, Operation] = {
            "+": AddOperation(),
            "-": SubtractOperation(),
            "*": MultiplyOperation(),
            "/": DivideOperation(),
            "sqrt": SquareRootOperation()
        }

    def calculate(self, expression: str):
        self.validate_expression(expression)
        operands = expression.split()
        stack = []
        for o in operands:
            if o in self.operations:
                operation = self.operations[o]
                self.validate_stack(stack, operation)
                operation.execute(stack)
            else:
                stack.append(float(o))

        if len(stack) != 1:
            raise ValueError("The provided expression is wrong")

        return stack[0]


    def validate_expression(self, expression: str):
        tokens = expression.split()
        for token in tokens:
            try:
                float(token)
            except ValueError:
                if token not in self.operations:
                    raise ValueError(f"Invalid token found: {token}")


    @staticmethod
    def validate_stack(stack: list, operation: Operation):
        required_operands = {
            AddOperation: 2,
            SubtractOperation: 2,
            MultiplyOperation: 2,
            DivideOperation: 2,
            SquareRootOperation: 1
        }
        required = required_operands[type(operation)]
        if len(stack) < required:
            raise ValueError("The provided expression is wrong.")


