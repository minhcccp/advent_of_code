"""
References:
    https://adventofcode.com/2019/day/2#part2

Notes:
    This approach is possible thanks to the fact that:
    None of the opcodes change to the halt opcode 99 because of their previous operations
"""
from itertools import count

from sympy import simplify
from sympy.parsing.sympy_parser import parse_expr

from common import Computer

computer: Computer = Computer("input.txt")


# As the first 4 operations save the result in the 3rd position of memory and the value there isn't used after those
# operations, the operations won't be considered when constructing the polynomial
start_index: int = 4

testing_index: int
halt_index: int = next(
    testing_index
    for testing_index in count(0, 4)
    if computer.initializer[testing_index] == 99
)


affected_indices: set = {1, 2}

current_statement: str = ""
previous_statement: str = ""


def get_value(index: int) -> str:
    return (
        f"computer.initializer[{index}]"
        if index in affected_indices
        else str(computer.initializer[index])
    )


while start_index < halt_index:
    first: int
    second: int
    third: int
    first, second, third = computer.initializer[start_index + 1 : start_index + 4]

    if (first in affected_indices or second in affected_indices) and third:
        affected_indices.add(third)

    previous_statement, current_statement = current_statement, (
        (" + " if computer.initializer[start_index] == 1 else " * ").join(
            sorted([get_value(first), get_value(second)], key=len)
        )
        + " = "
        + get_value(third)
    )
    if previous_statement:
        new: str
        old: str
        new, old = previous_statement.split(" = ")
        current_statement = current_statement.replace(old, f"({new})")

    start_index += 4

pattern: str
variable: str
for pattern, variable in [
    ["computer.initializer[day_1]", "x"],
    ["computer.initializer[2]", "y"],
]:
    current_statement = current_statement.replace(pattern, variable)

print(current_statement)
print(
    simplify(
        parse_expr(
            current_statement[: current_statement.index("=")],
        )
    )
)


def main():
    ...


if __name__ == "__main__":
    main()
