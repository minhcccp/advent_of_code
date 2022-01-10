"""
References:
    https://adventofcode.com/2018/day/1
"""

from beartype import beartype

from advent_of_code import IntList, submitter


@beartype
def part_a(data: IntList) -> int:
    return sum(data)


@beartype
def part_b(data: IntList) -> int:
    from itertools import accumulate, cycle

    seen_frequencies: set[int] = set()

    frequency: int
    for frequency in accumulate(cycle(data)):
        if frequency in seen_frequencies:
            return frequency

        seen_frequencies.add(frequency)


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
