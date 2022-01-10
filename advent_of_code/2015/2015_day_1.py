"""
References:
    https://adventofcode.com/2015/day/1
"""

from beartype import beartype


@beartype
def part_a(data: str) -> int:
    equivalent_pairs: dict[str, int] = {"(": 1, ")": -1}
    return sum(map(equivalent_pairs.get, data))


@beartype
def part_b(data: str) -> int:
    from regex import Pattern, compile

    # https://regex101.com/r/U3214g/2
    pattern: Pattern = compile(r"(\((?>(?R))*\))")

    return pattern.search(data).end() + 1


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
