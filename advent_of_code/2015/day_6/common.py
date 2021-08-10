"""
References:
    https://adventofcode.com/2015/day/6
"""
from collections.abc import Callable, Iterator
from functools import cache
from itertools import product
from re import VERBOSE, search
from typing import Literal, cast

from numpy import ndarray, sum, zeros

CommandType = Literal["turn on", "turn off", "toggle"]


def inclusive_range(start: int, end: int) -> Iterator[int]:
    yield from range(start, end + 1)


class LightBoard:
    def __init__(self, machine: Callable[[CommandType, int], int]):
        self.board: ndarray = zeros((1_000,) * 2, dtype=int)
        self.cached_machine = cache(machine)

    def result(self) -> int:
        line: str
        for line in open("input.txt"):
            command: Literal["turn on", "turn off", "toggle"]
            coordinates: tuple[str]
            command, *coordinates = search(
                r"""
    (?P<command>turn\ on|turn\ off|toggle)\ 
    (?P<x0>\d{1,3}),(?P<y0>\d{1,3})\ 
    through\ 
    (?P<x1>\d{1,3}),(?P<y1>\d{1,3})
    """,
                line,
                VERBOSE,
            ).groups()

            x0: int
            y0: int
            x1: int
            y1: int
            x0, y0, x1, y1 = map(int, coordinates)

            x: int
            y: int
            for x, y in product(inclusive_range(x0, x1), inclusive_range(y0, y1)):
                self.board[x, y] = self.cached_machine(command, self.board[x, y])

        return cast(int, sum(self.board))
