"""
References:
    https://adventofcode.com/2015/day/6
"""

from common import CommandType, LightBoard


def machine(command: CommandType, data: int) -> int:
    if command == "toggle":
        return 1 - data

    if command == "turn on":
        return 1

    if command == "turn off":
        return 0

    return data


def main():
    new_board: LightBoard = LightBoard(machine)
    print(new_board.result())


if __name__ == "__main__":
    main()
