from collections.abc import Callable
from typing import Optional, TypeVar

from beartype import beartype

IntList: type[list[int]] = list[int]

T = TypeVar("T")


@beartype
def submitter(
    day: int,
    year: int,
    data: T,
    part_a_function: Callable[[T], int],
    part_b_function: Optional[Callable[[T], int]] = None,
) -> None:
    from aocd import submit

    part_a_answer: int = part_a_function(data)
    submit(part_a_answer, part="a", day=day, year=year)

    if part_b_function:
        part_b_answer: int = part_b_function(data)
        submit(part_b_answer, part="b", day=day, year=year)
