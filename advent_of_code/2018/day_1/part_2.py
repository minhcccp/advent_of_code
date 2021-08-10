"""
References:
    https://adventofcode.com/2018/day/1#part2
"""
from itertools import accumulate, cycle


def main():
    record: set[int] = {0}
    current: int
    for current in accumulate(cycle(map(int, open("input.txt")))):
        if current in record:
            print(current)
            exit()

        record.add(current)


if __name__ == "__main__":
    main()
