"""
References:
    https://adventofcode.com/2019/day/2#part2
"""
from itertools import product

from codetiming import Timer
from common import Computer


def main():
    with Timer(text="\n{} seconds"):
        computer: Computer = Computer("input.txt")

        noun: int
        verb: int

        noun, verb = next(
            pair
            for pair in product(range(100), repeat=2)
            if computer.simulation(*pair) == 19690720
        )

    print(100 * noun + verb)


if __name__ == "__main__":
    main()
