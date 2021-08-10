"""
References:
    https://adventofcode.com/2015/day/2#part2
"""
from math import prod


def mapper(row: str) -> int:
    formatted: list[int] = sorted(map(int, row.split("x")))
    return 2 * sum(formatted[:2]) + prod(formatted)


def main():
    print(sum(map(mapper, open("input.txt"))))


if __name__ == "__main__":
    main()
