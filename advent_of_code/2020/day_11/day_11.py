from typing import TextIO

from numpy import array, count_nonzero, ndarray, ndenumerate, zeros_like

if __name__ == "__main__":
    FLOOR: int = ord(".")
    EMPTY: int = ord("L")
    OCCUPIED: int = ord("#")

    source: TextIO
    with open("input_11.txt") as source:
        line: str
        previous: ndarray = array(
            [list(map(ord, line)) for line in source.read()[:-1].split("\n")]
        )

    row: int
    column: int
    row, column = previous.shape

    def count_hashtag(data_array: ndarray) -> int:
        return count_nonzero(data_array == OCCUPIED)

    current_count: int = count_hashtag(previous)
    stabilized: bool = False

    while not stabilized:
        follow: ndarray = zeros_like(previous)

        value: int
        for index, value in ndenumerate(previous):
            first: int
            second: int
            first, second = index

            # * This array provides the seating situation looking from the chosen location
            # * Currently it only shows the adjacent locations
            # TODO: Rewrite so that it can show the seats from lines in cardinal and intercardinal directions
            eyesight: ndarray = previous[
                first - 1 if first else None : first + 2 if first + 1 < row else None,
                second - 1
                if second
                else None : second + 2
                if second + 1 < column
                else None,
            ]

            around: int = count_hashtag(eyesight) - (value == OCCUPIED)

            if value == EMPTY and not around:
                follow[first, second] = OCCUPIED
            elif value == OCCUPIED and around >= 4:
                follow[first, second] = EMPTY
            else:
                follow[first, second] = value

        current_count = count_hashtag(follow)

        stabilized = current_count == count_hashtag(previous)

        previous = follow.copy()

    print(current_count)
