"""
References:
    https://adventofcode.com/2020/day/4
"""
from re import findall

required: set[str] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def main():
    print(
        sum(
            required.issubset(findall(r"\S{3}(?=:\S+)", passport))
            for passport in open("input.txt").read().split("\n\n")
        )
    )


if __name__ == "__main__":
    main()
