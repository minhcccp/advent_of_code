"""
References:
    https://adventofcode.com/2019/day/2
"""
from codetiming import Timer

from common import Computer


def main():
    with Timer(text="\n{} seconds"):
        print(Computer("input.txt").simulation(12, 2))


if __name__ == "__main__":
    main()
