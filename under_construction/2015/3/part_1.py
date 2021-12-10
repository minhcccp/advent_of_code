"""
References:
    https://adventofcode.com/2015/day/3
"""
from common import accumulator


def main():
    print(len({0j}.union(accumulator(open("input.txt").read()))))


if __name__ == "__main__":
    main()
