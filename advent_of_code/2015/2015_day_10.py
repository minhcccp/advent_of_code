"""
References:
    https://adventofcode.com/2015/day/10
"""

from beartype import beartype


@beartype
def look_and_say(sequence: str, turns_left: int) -> int:
    from itertools import groupby

    return (
        look_and_say(
            "".join(f"{len([*group])}{key}" for key, group in groupby(sequence)),
            turns_left - 1,
        )
        if turns_left
        else len(sequence)
    )


@beartype
def part_a(data: str) -> int:
    return look_and_say(data, 40)


@beartype
def part_b(data: str) -> int:
    return look_and_say(data, 50)


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
