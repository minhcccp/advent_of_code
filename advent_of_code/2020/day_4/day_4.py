from re import match

if __name__ == "__main__":

    with open("result_4b.txt", "w") as result, open("input_4.txt") as source:

        def validator(checking_number: int, checking_passport: str) -> bool:
            passport_dict: dict[str, str] = dict(
                info.split(":") for info in checking_passport.replace("\n", " ").split()
            )
            passport_dict["hgt"] = passport_dict.get("hgt", "0cm")

            result.write(f"\nPassport #{checking_number}\n")

            def field_get(name: str) -> str:
                nonlocal passport_dict
                info: str = passport_dict.get(name, "0")

                result.write(f"{name}: {info}\n")

                return info

            def test_1() -> bool:
                for field_number, boundary in {
                    "byr": (1920, 2002),
                    "iyr": (2010, 2020),
                    "eyr": (2020, 2030),
                }.items():
                    mark_1: bool = int(field_get(field_number)) in range(
                        boundary[0], boundary[1] + 1
                    )
                    result.write(f"Test: {mark_1}\n")

                    if not mark_1:
                        return False

                return True

            def test_2() -> bool:
                for field_string, pattern in {
                    "hcl": "^#(\d|[a-f]){6,6}$",
                    "pid": "^\d{9,9}$",
                }.items():
                    mark_2: bool = bool(match(pattern, field_get(field_string)))
                    result.write(f"Test: {mark_2}\n")

                    if not mark_2:
                        return False

                return True

            def test_3() -> bool:
                unit: str = passport_dict["hgt"][-2:]
                if any(not char.isalpha() for char in unit):
                    return False

                is_cm: bool = unit == "cm"
                mark_3: bool = int(field_get("hgt")[:-2]) in range(
                    150 if is_cm else 59,
                    (193 if is_cm else 76) + 1,
                )
                result.write(f"Test: {mark_3}\n")

                return mark_3

            def test_4() -> bool:
                mark_4: bool = field_get("ecl") in "amb blu brn gry grn hzl oth".split()
                result.write(f"Test: {mark_4}\n")
                return mark_4

            verdict: bool = all([test_1(), test_2(), test_3(), test_4()])
            result.write(f"Finally pass: {verdict}\n")
            return verdict

        spliter: str = "\n\n"
        result.write(
            f"""\nTotal passed passports: {sum(validator(*info_pair) for info_pair in enumerate(source.read().split(spliter)))}"""
        )
