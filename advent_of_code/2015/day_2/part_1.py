"""
References:
    https://adventofcode.com/2015/day/2
"""
from itertools import combinations
from math import prod

if __name__ == "__main__":
    print(
        sum(
            prod(pair, start=2 + (not index))
            for row in open("input.txt")
            for index, pair in enumerate(
                combinations(sorted(map(int, row.split("x"))), 2)
            )
        )
    )
