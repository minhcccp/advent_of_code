"""
References:
    https://adventofcode.com/2015/day/3#part2
"""
from common import accumulator


def main():
    given: str = open("input.txt").read()
    print(len({0j}.union(*(accumulator(given[start::2]) for start in range(2)))))


if __name__ == "__main__":
    main()
