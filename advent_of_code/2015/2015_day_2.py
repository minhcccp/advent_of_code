"""
References:
    https://adventofcode.com/2015/day/2
"""

from collections.abc import Iterable
from math import prod

from beartype import beartype

Data: type[list[str]] = list[str]


@beartype
def dimensions(row: str) -> list[int]:
    return sorted(map(int, row.split("x")))


@beartype
def part_a(data: Data) -> int:
    from itertools import combinations

    return sum(
        prod(pair, start=2 + (not index))
        for row in data
        for index, pair in enumerate(combinations(dimensions(row), 2))
    )


@beartype
def part_b(data: Data) -> int:
    rows: Iterable[list[int]] = map(dimensions, data)
    return sum(2 * sum(row[:2]) + prod(row) for row in rows)


def main():
    from aocd import get, get_data
    from aocd.transforms import lines

    from advent_of_code import submitter

    day: int
    year: int
    day, year = get.get_day_and_year()
    data: Data = lines(get_data(day=day, year=year))

    submitter(
        day=day, year=year, data=data, part_a_function=part_a, part_b_function=part_b
    )


if __name__ == "__main__":
    main()
