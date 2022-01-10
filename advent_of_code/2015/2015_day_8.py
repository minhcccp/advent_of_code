"""
References:
    https://adventofcode.com/2015/day/8
"""

from beartype import beartype

Data: type[list[str]] = list[str]


@beartype
def part_a(data: Data) -> int:
    return sum(len(line) - len(eval(line)) for line in data)


@beartype
def part_b(data: Data) -> int:
    return sum(sum(map(line.count, r"\"")) + 2 for line in data)


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
