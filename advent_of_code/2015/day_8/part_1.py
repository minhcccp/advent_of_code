"""
References:
    https://adventofcode.com/2015/day/8
"""


def main():
    total: int = 0
    for line in open("input.txt"):
        line = line.strip()
        total += len(line) - len(eval(line))

    print(total)


if __name__ == "__main__":
    main()
