from hashlib import md5
from itertools import count

key: str = "yzbqklnj"


def finder(length: int) -> int:
    return next(
        value
        for value in count(1)
        if md5((key + str(value)).encode()).hexdigest().startswith("0" * length)
    )
