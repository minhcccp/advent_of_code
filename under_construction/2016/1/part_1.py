"""
References:
    https://adventofcode.com/2016/day/1
"""
from codetiming import Timer

from common import Interpreter


@Timer(text="\n{} seconds")
def main():
    interpreter: Interpreter = Interpreter()

    for _ in interpreter.location_iterator(open("input.txt").readline()):
        ...

    print(interpreter.taxicab_metric())


def test_part_1():
    commands: str
    expected: int
    for commands, expected in [
        ("R2, L3", 5),
        ("R2, R2, R2", 2),
        ("R5, L5, R5, R3", 12),
    ]:
        test_interpreter: Interpreter = Interpreter()
        for _ in test_interpreter.location_iterator(commands):
            ...

        assert test_interpreter.taxicab_metric() == expected


if __name__ == "__main__":
    main()
