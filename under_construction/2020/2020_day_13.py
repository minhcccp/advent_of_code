# TODO: Rewrite this script
from sympy.ntheory.modular import crt


def main():
    timeline: str = "29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,631,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,23,x,x,x,x,x,x,x,383,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"

    moduli: list[int] = []
    residues: list[int] = []

    delay: int
    route: str
    for delay, route in enumerate(timeline.split(",")):
        if route != "x":
            divisor: int = int(route)
            moduli.append(divisor)
            residues.append((divisor - delay) % divisor)

    print(crt(moduli, residues)[0])


if __name__ == "__main__":
    main()
