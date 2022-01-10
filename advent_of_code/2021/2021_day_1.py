"""
References:
    https://adventofcode.com/2021/day/1
"""

from collections.abc import Iterable

from beartype import beartype

from advent_of_code import IntList, submitter


@beartype
def increment_counter(data: Iterable[int]) -> int:
    from itertools import pairwise, starmap

    return sum(starmap(int.__lt__, pairwise(data)))


@beartype
def part_a(data: IntList) -> int:
    return increment_counter(data)


@beartype
def part_b(data: IntList) -> int:
    from more_itertools import windowed

    combined_windows: map[int] = map(sum, windowed(data, 3))
    return increment_counter(combined_windows)


def main():
    from aocd import get, get_data, transforms

    day: int
    year: int
    day, year = get.get_day_and_year()
    data: IntList = transforms.numbers(get_data(day=day, year=year))

    submitter(
        day=day, year=year, data=data, part_a_function=part_a, part_b_function=part_b
    )


if __name__ == "__main__":
    main()
