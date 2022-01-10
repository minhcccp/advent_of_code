"""
References:
    https://adventofcode.com/2015/day/4
"""

from beartype import beartype


@beartype
def number_finder(key_starter: str, length: int) -> int:
    from hashlib import md5
    from itertools import count

    target_starter: str = "0" * length

    value: int
    for value in count(1):
        if md5(f"{key_starter}{value}".encode()).hexdigest().startswith(target_starter):
            return value


@beartype
def part_a(data: str) -> int:
    return number_finder(data, 5)


@beartype
def part_b(data: str) -> int:
    return number_finder(data, 6)


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
