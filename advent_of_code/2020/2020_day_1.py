"""
References:
    https://adventofcode.com/2020/day/1
"""

from advent_of_code import IntList, submitter
from beartype import beartype


@beartype
def product_finder(
    entries: IntList,
    target_sum: int,
    entries_needed: int,
) -> int:
    from bisect import bisect
    from itertools import combinations
    from math import prod

    max_allowed_value = target_sum - sum(entries[: entries_needed - 1])
    del entries[bisect(entries, max_allowed_value) :]

    combination: tuple[int, ...]
    for combination in combinations(entries, r=entries_needed):
        if sum(combination) == target_sum:
            return prod(combination)


@beartype
def part_a(data: IntList) -> int:
    return product_finder(data, 2020, 2)


@beartype
def part_b(data: IntList) -> int:
    return product_finder(data, 2020, 3)


def main():
    from aocd import get, get_data, transforms

    day: int
    year: int
    day, year = get.get_day_and_year()

    data: IntList = transforms.numbers(get_data(day=day, year=year))
    data.sort()

    submitter(
        day=day, year=year, data=data, part_a_function=part_a, part_b_function=part_b
    )


if __name__ == "__main__":
    main()
