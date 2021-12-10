from collections.abc import Iterator
from itertools import accumulate

reference: dict[str, complex] = {">": 1, "<": -1, "^": 1j, "v": -1j}


def accumulator(instructions: str) -> Iterator[complex]:
    yield from accumulate(map(reference.get, instructions))
