"""
References:
    https://adventofcode.com/2015/day/5#part2
"""
from re import search


def filtration(string: str) -> bool:
    return all(search(pattern, string) for pattern in (r"(.{2}).*\1", r"(.).\1"))


def main():
    print(sum(map(filtration, open("input.txt"))))


if __name__ == "__main__":
    main()
