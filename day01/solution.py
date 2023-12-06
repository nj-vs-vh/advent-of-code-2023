import re
from typing import Callable


def extract_digits(
    inp: str,
    digit_patterns: list[str],
    digit_parser: Callable[[str], int],
    debug: bool,
) -> list[int]:
    fwd_digit_re = re.compile("|".join(re.escape(p) for p in digit_patterns))
    bck_digit_re = re.compile("|".join(re.escape(p[::-1]) for p in digit_patterns))
    first_last_digits: list[int] = []
    for line in inp.splitlines():
        first_digit_match = fwd_digit_re.search(line)
        assert first_digit_match
        last_digit_match = bck_digit_re.search(line[::-1])
        assert last_digit_match
        first_last_digit_num = digit_parser(first_digit_match.group()) * 10 + digit_parser(
            last_digit_match.group()[::-1]
        )
        if debug:
            print(f"{line} -> {first_last_digit_num}")
        first_last_digits.append(first_last_digit_num)
    return first_last_digits


def part_1(inp: str, debug: bool):
    calibration_values = extract_digits(
        inp=inp, digit_patterns=[str(i) for i in range(10)], digit_parser=int, debug=debug
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
        digit_patterns=[str(i) for i in range(10)] + digit_spelling,
        digit_parser=lambda digit: digit_spelling_to_value.get(digit) or int(digit),
        debug=debug,
    )
    if debug:
        print(calibration_values)
    print(sum(calibration_values))
