"""
References:
    https://adventofcode.com/2017/day/2
"""

from beartype import beartype

from advent_of_code import IntList, submitter

Data = list[IntList]


@beartype
def part_a(data: Data) -> int:
    from more_itertools import minmax

    return sum(-int.__sub__(*minmax(row)) for row in data)


@beartype
def row_mapper(row: IntList) -> int:
    from itertools import combinations

    row.sort(reverse=True)

    numbers_pair: tuple[int, int]
    for numbers_pair in combinations(row, 2):
        div: int
        mod: int
        div, mod = divmod(*numbers_pair)
        if not mod:
            return div


@beartype
def part_b(data: Data) -> int:
    return sum(map(row_mapper, data))


def main():
    from aocd import get, get_data
    from aocd.transforms import lines

    day: int
    year: int
    day, year = get.get_day_and_year()

    data: Data = [
        [*map(int, row.split())] for row in lines(get_data(day=day, year=year))
    ]

    submitter(
        day=day, year=year, data=data, part_a_function=part_a, part_b_function=part_b
    )


if __name__ == "__main__":
    main()
