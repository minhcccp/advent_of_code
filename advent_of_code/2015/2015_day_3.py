"""
References:
    https://adventofcode.com/2015/day/3
"""

from collections.abc import Iterable

from beartype import beartype


@beartype
def location_set(instructions: Iterable[str]) -> set[complex]:
    from itertools import accumulate

    reference: dict[str, complex] = {">": 1, "<": -1, "^": 1j, "v": -1j}
    return {0, *accumulate(map(reference.get, instructions))}


@beartype
def part_a(data: str) -> int:
    return len(location_set(data))


@beartype
def part_b(data: str) -> int:
    from more_itertools import distribute

    return len(set.union(*map(location_set, distribute(2, data))))


def main():
    from aocd import get, get_data

    from advent_of_code import submitter

    day: int
    year: int
    day, year = get.get_day_and_year()
    data: str = get_data(day=day, year=year)

    submitter(
        day=day, year=year, data=data, part_a_function=part_a, part_b_function=part_b
    )


if __name__ == "__main__":
    main()
