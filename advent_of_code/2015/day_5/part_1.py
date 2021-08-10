"""
References:
    https://adventofcode.com/2015/day/5
"""
from re import findall, search

from codetiming import Timer

excluded_strings: list[str] = ["ab", "cd", "pq", "xy"]


def filtration(string: str) -> bool:
    return all(
        (
            len(findall(r"[aeiou]", string)) >= 3,
            search(r"(.)\1", string),
            not any(map(string.__contains__, excluded_strings)),
        )
    )


@Timer()
def main():
    print(sum(map(filtration, open("input.txt"))))


if __name__ == "__main__":
    main()
