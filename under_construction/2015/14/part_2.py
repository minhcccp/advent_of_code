"""
References:
    https://adventofcode.com/2015/day/14#part2
"""
from collections.abc import Iterator
from dataclasses import dataclass
from re import search
from typing import Annotated, Optional

time_type = Annotated[int, "seconds"]


@dataclass
class Reindeer:
    speed: Annotated[int, "km/s"]
    flying_time: time_type
    resting_time: time_type

    def __post_init__(self):
        self.is_flying: bool = True
        self.current_distance: Annotated[int, "km"] = 0
        self.cycle_time: time_type = self.flying_time
        self.points: int = 0

    def update_distance(self) -> int:
        if self.is_flying:
            self.current_distance += self.speed

        self.cycle_time -= 1
        if not self.cycle_time:
            self.is_flying = not self.is_flying
            self.cycle_time = self.flying_time if self.is_flying else self.resting_time

        return self.current_distance

    def return_points(self) -> int:
        return self.points


def contender_gen() -> Iterator[int]:
    yield from (
        Reindeer(*map(int, search(r"(\d+)\D+(\d+)\D+(\d+)\D+", line).groups()))
        for line in open("input.txt")
    )


def main():
    contenders: list[Reindeer] = [*contender_gen()]
    contender_count: int = len(contenders)

    for _ in range(2503):
        best_index: Optional[int]
        best_distance: Optional[int]
        best_index = best_distance = None

        index: int
        for index in range(contender_count):
            distance: int = contenders[index].update_distance()
            if best_index is None or distance > best_distance:
                best_index = index
                best_distance = distance

        contenders[best_index].points += 1

    print(max(map(Reindeer.return_points, contenders)))


if __name__ == "__main__":
    main()
