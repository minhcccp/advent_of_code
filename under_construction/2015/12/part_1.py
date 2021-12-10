"""
References:
    https://adventofcode.com/2015/day/12
"""
from re import findall


def main():
    print(sum(map(int, findall(r"-?\d+", open("input.txt").read()))))


if __name__ == "__main__":
    main()
