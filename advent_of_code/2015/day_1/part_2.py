"""
References:
    https://adventofcode.com/2015/day/1#part2
    https://stackoverflow.com/questions/64623841/regex-to-get-the-size-of-capturing-group
"""
from regex import search

if __name__ == "__main__":
    print(search(r"(\((?>(?1))*\))", open("input.txt").read()).end() + 1)
