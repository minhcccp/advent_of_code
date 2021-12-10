"""
References:
    https://adventofcode.com/2021/day/6
"""

from advent_of_code import IntList, submitter
from beartype import beartype


@beartype
def population_projection(data: IntList, days: int) -> int:
    from collections import Counter, deque

    # The lantern fish populace is grouped by their internal timers
    timers_counter: Counter[int] = Counter(data)
    states_count: int = 9
    populace: deque[int] = deque(map(timers_counter.__getitem__, range(states_count)))

    passed_days: int = 0
    while passed_days < days:
        children: int = next(filter(bool, populace))
        delta_time: int = populace.index(children) + 1

        # As a new generation of lantern fishes is born, the populace's timer groups are shifted in the direction of
        # decreasing timers, except the timer group of 6 which is incremented by the number of parent fishes.
        populace.rotate(-delta_time)
        populace[6] += children

        passed_days += delta_time

    return sum(populace)


@beartype
def part_a(data: IntList) -> int:
    return population_projection(data, 80)


@beartype
def part_b(data: IntList) -> int:
    return population_projection(data, 256)


def main():
    from aocd import get, get_data

    day: int
    year: int
    day, year = get.get_day_and_year()
    data: IntList = [*map(int, get_data(day=day, year=year).split(","))]

    submitter(
        day=day, year=year, data=data, part_a_function=part_a, part_b_function=part_b
    )


if __name__ == "__main__":
    main()
