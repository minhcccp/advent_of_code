"""
References:
    https://adventofcode.com/2017/day/1
"""

from collections.abc import Iterable

from beartype import beartype


@beartype
def pair_sum(pair: Iterable[tuple[str, str]]) -> int:
    return sum(int(first) for first, second in pair if first == second)


@beartype
def part_a(data: str) -> int:
    from more_itertools import pairwise

    return pair_sum(pairwise(data + data[0]))


@beartype
def part_b(data: str) -> int:
    from more_itertools import divide

    return pair_sum(zip(*divide(2, data))) * 2


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
