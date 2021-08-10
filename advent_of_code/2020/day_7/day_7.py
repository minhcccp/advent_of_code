"""
Count for shiny gold option
"""


if __name__ == "__main__":
    working_detail: str = "origin"
    with open(f"{working_detail}_shorten_7.txt") as base, open(
        f"{working_detail}_input_7.txt"
    ) as full, open(f"{working_detail}_result_7.txt", "w") as result:

        owner_slave: dict[str, tuple[str]] = dict(
            (k_in, tuple(sorted(eval(proto_v_out))))
            for k_in, proto_v_out in [
                item.split(": ") for item in base.read()[:-1].split("\n")
            ]
        )

        flat_out: list[str] = ["shiny gold"]
        new = tuple(flat_out)
        while True:
            new = tuple(
                result
                for color in new
                for result in owner_slave[color]
                if result != "absent" and result not in flat_out
            )

            if not new:
                break

            flat_out = list(new) + flat_out

        # result.writelines(f"{level}\n" for level in flat_out)

        instructions: list[str] = full.read()[:-1].split("\n")
        sum_dict: dict[str, int] = dict()

        for member in flat_out.copy():
            for line in instructions:
                if line.startswith(member) and "no" in line:

                    sum_dict[member] = 1
                    flat_out.remove(member)
                    break

        print(sum_dict)
        while any(key not in sum_dict for key in flat_out):
            for member in flat_out:
                print(member)
                for line in instructions:
                    if line.startswith(member):
                        try:
                            sum_dict[member] = (
                                sum(
                                    int(multiplier) * sum_dict[argument]
                                    for multiplier, argument in (
                                        part[: part.find(" bag")].split(" ", 1)
                                        for part in line[
                                            line.find("contain ") + 8 : -1
                                        ].split(", ")
                                    )
                                )
                                + 1
                            )
                        except KeyError:
                            pass

                        break

        print(sum_dict["shiny gold"] - 1)
