class Calculator:
    def __init__(self, name: str, *values) -> None:
        self.name = name
        self.values = list(values)

    def execute(self):
        raise NotImplementedError("Subclasses must implement execute()")

    def __str__(self) -> str:
        return f"{self.name} -> {self.values}"


class Addition(Calculator):
    def __init__(self, *values) -> None:
        super().__init__("addition", *values)

    def execute(self):
        total = 0
        for val in self.values:
            total += val
        return total


class Subtraction(Calculator):
    def __init__(self, first, second) -> None:
        super().__init__("subtraction", first, second)

    def execute(self):
        return self.values[0] - self.values[1]


class Division(Calculator):
    def __init__(self, dividend, divisor) -> None:
        super().__init__("division", dividend, divisor)

    def execute(self) -> float:
        if self.values[1] == 0:
            raise ValueError("Cannot divide by zero")
        return self.values[0] / self.values[1]


class Multiplication(Calculator):
    def __init__(self, *values) -> None:
        super().__init__("multiplication", *values)

    def execute(self):
        product = 1
        for val in self.values:
            product *= val
        return product


class OperationHistory:
    def __init__(self) -> None:
        self.entries = []

    def add(self, operation: Calculator, result) -> None:
        self.entries.append({
            "operation": str(operation),
            "result": result,
        })

    def get_latest(self, count: int = 5) -> list:
        return self.entries[-count:]


class Calculator:
    def __init__(self) -> None:
        self.history = OperationHistory()

    def execute(self, operation: Calculator):
        res = operation.execute()
        self.history.add(operation, res)
        return res

    def print_history(self) -> None:
        for entry in self.history.entries:
            print(f"{entry['operation']} = {entry['result']}")


if __name__ == "__main__":
    calc = Calculator()

    add_res = calc.execute(Addition(4, 6, 10))
    sub_res = calc.execute(Subtraction(25, 9))
    div_res = calc.execute(Division(36, 6))
    mul_res = calc.execute(Multiplication(2, 3, 7))

    print("4 + 6 + 10 =", add_res)
    print("25 - 9 =", sub_res)
    print("36 / 6 =", div_res)
    print("2 * 3 * 7 =", mul_res)

    print("\nOperation history:")
    calc.print_history()