"""
References:
    https://adventofcode.com/2015/day/7
"""
from collections.abc import Callable
from functools import cache


class Machine:
    opcode_equivalent: dict[str, Callable[[int, int], int]] = {
        "AND": int.__and__,
        "OR": int.__or__,
        "LSHIFT": int.__lshift__,
        "RSHIFT": int.__rshift__,
    }

    def __init__(self, input_file: str):
        self.memory: dict[str, str] = {}

        line: str
        for line in open(input_file):
            value: str
            key: str
            value, key = line.strip().split(" -> ")
            self.memory[key] = value

    @cache
    def value_equivalent(self, gate: str) -> int:
        if gate.isdecimal():
            return int(gate)

        command: str = self.memory[gate]
        if " " not in command:
            return self.value_equivalent(command)

        split_command: list[str] = command.split()

        first: str
        second: str
        first, second = split_command[:2]
        if first == "NOT":
            return ~self.value_equivalent(second)

        return self.opcode_equivalent[second](
            self.value_equivalent(first),
            self.value_equivalent(split_command[2]),
        )
