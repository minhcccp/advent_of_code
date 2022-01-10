from collections.abc import Iterator
from re import findall
from turtle import Turtle
from typing import Literal, Type

PositionType: Type[tuple[float, float]] = tuple[float, float]


class Interpreter:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.setheading(90)

    def taxicab_metric(self) -> int:
        return int(sum(map(abs, self.turtle.pos())))

    def location_iterator(self, commands: str) -> Iterator[PositionType]:
        turn: Literal["L", "R"]
        amplitude: str
        for turn, amplitude in findall(r"([LR])(\d+)", commands):
            # noinspection PyArgumentList
            (self.turtle.right if turn == "R" else self.turtle.left)(90)

            value: int = int(amplitude)
            for _ in range(value):
                self.turtle.forward(1)
                yield self.turtle.pos()
