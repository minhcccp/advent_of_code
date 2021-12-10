"""
References:
    https://adventofcode.com/2015/day/14
"""
from re import search

total_time: int = 2503


def distance(speed: int, flying_time: int, resting_time: int) -> int:
    cycles: int
    left: int
    cycles, left = divmod(total_time, flying_time + resting_time)

    return speed * (cycles * flying_time + min(left, flying_time))


def main():
    print(
        max(
            distance(*map(int, search(r"(\d+)\D+(\d+)\D+(\d+)\D+", line).groups()))
            for line in open("input.txt")
        )
    )


if __name__ == "__main__":
    main()
