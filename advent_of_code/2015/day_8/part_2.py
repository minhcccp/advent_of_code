"""
References:
    https://adventofcode.com/2015/day/8#part2
"""


def main():
    total: int = 0
    for line in open("input.txt"):
        line = line.strip()
        total += sum(map(line.count, '"\\')) + 2

    print(total)


if __name__ == "__main__":
    main()
