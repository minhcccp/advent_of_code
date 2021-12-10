"""
References:
    https://adventofcode.com/2015/day/6#part2
"""
from common import CommandType, LightBoard


def machine(command: CommandType, data: int) -> int:
    if command == "toggle":
        return data + 2

    if command == "turn on":
        return data + 1

    if command == "turn off" and data:
        return data - 1

    return data


def main():
    new_board: LightBoard = LightBoard(machine)
    print(new_board.result())


if __name__ == "__main__":
    main()
