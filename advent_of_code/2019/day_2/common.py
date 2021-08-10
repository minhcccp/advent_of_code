from typing import Union

from sympy.abc import x, y
from sympy.polys.polytools import Poly


class Computer:
    def __init__(self, init_memory: str):
        self.initializer: tuple[int, ...] = tuple(
            map(int, open(init_memory).read().split(","))
        )
        self.memory: list[Union[int, Poly]] = [*self.initializer]

    def simulation(
        self, noun: Union[int, Poly] = Poly(x), verb: Union[int, Poly] = Poly(y)
    ) -> int:

        self.memory[1:3] = noun, verb

        start: int = 4
        while True:
            opcode: int
            inputs: list[int]
            output: int
            opcode, *inputs, output = self.memory[start : start + 4]

            if opcode == 99:
                break

            self.memory[output] = (int.__add__ if opcode == 1 else int.__mul__)(
                *map(self.memory.__getitem__, inputs)
            )

            start += 4

        return self.memory[0]


def main():
    computer: Computer = Computer("input.txt")
    print(computer.simulation())


if __name__ == "__main__":
    main()
