"""
References:
    https://adventofcode.com/2015/day/1
"""
reference: dict[str, int] = {"(": 1, ")": -1}

if __name__ == "__main__":
    print(sum(map(reference.get, open("input.txt").read())))
