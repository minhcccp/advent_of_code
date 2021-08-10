"""
References:
    https://adventofcode.com/2016/day/1#part2
"""
from common import Interpreter, PositionType


def main():
    interpreter: Interpreter = Interpreter()
    seen: set[PositionType] = {(0,) * 2}

    current: PositionType
    for current in interpreter.location_iterator(open("input.txt").readline(), True):
        if current in seen:
            break

        seen.add(current)

    print(interpreter.taxicab_metric())


if __name__ == "__main__":
    main()
