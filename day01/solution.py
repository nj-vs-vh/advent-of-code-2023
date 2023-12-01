import re
from typing import Callable


def extract_digits(
    inp: str,
    digit_re: re.Pattern,
    digit_parser: Callable[[str], int],
    debug: bool,
) -> list[int]:
    first_last_digits: list[int] = []
    for line in inp.splitlines():
        digits_matched: list[str] = []
        for pos in range(len(line)):
            m = digit_re.match(line, pos)
            if m:
                digits_matched.append(m.group())
        if not digits_matched:
            raise ValueError(f"failed to parse line: {line}")
        digits = [digit_parser(ds) for ds in digits_matched]
        first_last_digit_num = int(str(digits[0]) + str(digits[-1]))
        if debug:
            print(f"{line} -> {digits_matched} -> {digits} -> {first_last_digit_num}")
        first_last_digits.append(first_last_digit_num)
    return first_last_digits


def part_1(inp: str, debug: bool):
    calibration_values = extract_digits(
        inp, digit_re=re.compile(r"\d"), digit_parser=int, debug=debug
    )
    if debug:
        print(calibration_values)
    print(sum(calibration_values))


def part_2(inp: str, debug: bool):
    digit_spelling = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    digit_spelling_to_value = {spelling: idx + 1 for idx, spelling in enumerate(digit_spelling)}
    calibration_values = extract_digits(
        inp,
        digit_re=re.compile("(" + "|".join([r"\d"] + digit_spelling) + ")"),
        digit_parser=lambda digit: digit_spelling_to_value.get(digit) or int(digit),
        debug=debug,
    )
    if debug:
        print(calibration_values)
    print(sum(calibration_values))
