"""
References:
    https://adventofcode.com/2015/day/7#part2
"""
from common import Machine


def main():
    machine: Machine = Machine("input.txt")

    machine.memory["b"] = str(machine.value_equivalent("a"))
    machine.value_equivalent.cache_clear()

    print(machine.value_equivalent("a"))


if __name__ == "__main__":
    main()
