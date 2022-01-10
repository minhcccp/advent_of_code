"""
References:
    https://adventofcode.com/2015/day/5
"""

from re import Pattern, compile

from beartype import beartype

Data: type[list[str]] = list[str]


@beartype
def part_a(data: Data) -> int:
    vowels: Pattern = compile(r"[aeiou]")
    repeated_letters: Pattern = compile(r"(\w)\1")
    naughty_strings: Pattern = compile(r"(ab|cd|pq|xy)")

    return sum(
        all(
            (
                len(vowels.findall(string)) >= 3,
                repeated_letters.search(string),
                not naughty_strings.search(string),
            )
        )
        for string in data
    )


@beartype
def part_b(data: Data) -> int:
    pair_repeat: Pattern = compile(r"(\w{2}).*\1")
    letter_repeat: Pattern = compile(r"(\w).\1")

    return sum(
        all((pair_repeat.search(string), letter_repeat.search(string)))
        for string in data
    )


def main():
    from aocd import get, get_data
    from aocd.transforms import lines

    from advent_of_code import submitter

    day: int
    year: int
    day, year = get.get_day_and_year()
    data: Data = lines(get_data(day=day, year=year))

    submitter(
        day=day, year=year, data=data, part_a_function=part_a, part_b_function=part_b
    )


if __name__ == "__main__":
    main()
