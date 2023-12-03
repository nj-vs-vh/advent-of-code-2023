import operator
import re
from dataclasses import dataclass
from enum import Enum, auto
from functools import reduce


@dataclass(frozen=True)
class NumberOnLine:
    value: int
    start: int
    length: int


@dataclass(frozen=True)
class SymbolOnLine:
    char: str
    index: int


def parse_input(inp: str) -> tuple[list[list[NumberOnLine]], list[list[SymbolOnLine]]]:
    numbers_on_lines: list[list[NumberOnLine]] = []
    symbols_on_lines: list[list[SymbolOnLine]] = []

    number_re = re.compile(r"\d+")
    symbol_re = re.compile(r"[^\d\.]")
    blank_re = re.compile(r"\.+")

    for line in inp.splitlines():
        numbers: list[NumberOnLine] = []
        symbols: list[SymbolOnLine] = []
        pos = 0
        while pos < len(line):
            if number_match := number_re.match(line, pos=pos):
                number_str = number_match.group()
                numbers.append(
                    NumberOnLine(
                        value=int(number_str),
                        start=pos,
                        length=len(number_str),
                    )
                )
                pos += len(number_str)
            elif symbol_match := symbol_re.match(line, pos=pos):
                symbols.append(
                    SymbolOnLine(
                        char=symbol_match.group(),
                        index=pos,
                    )
                )
                pos += 1
            elif blank_match := blank_re.match(line, pos=pos):
                pos += len(blank_match.group())
            else:
                raise ValueError(f"Unexpected symbol at {pos}: {line!r}")
        numbers_on_lines.append(numbers)
        symbols_on_lines.append(symbols)

    return numbers_on_lines, symbols_on_lines


class RelativeSegmentPosition(Enum):
    LEFT = auto()
    RIGHT = auto()
    OVERLAP = auto()

    @classmethod
    def compute(cls, a: tuple[int, int], b: tuple[int, int]) -> "RelativeSegmentPosition":
        if a[1] < b[0]:
            return RelativeSegmentPosition.LEFT
        elif a[0] > b[1]:
            return RelativeSegmentPosition.RIGHT
        else:
            return RelativeSegmentPosition.OVERLAP


def vicinity_clamped(center: int, halfrange: int, min: int, max: int) -> list[int]:
    deltas = range(-halfrange, halfrange + 1)
    return [idx for idx in (center + delta for delta in deltas) if min <= idx <= max]


def part_1(inp: str, debug: bool):
    numbers, symbols = parse_input(inp)
    if debug:
        print(inp)
        print(*numbers, sep="\n")
        print(*symbols, sep="\n")

    line_count = len(numbers)
    part_number_sum = 0
    for line_idx, numbers_on_line in enumerate(numbers):
        for number in numbers_on_line:
            nearby_symbol_found = False
            for line_idx_to_check in vicinity_clamped(
                center=line_idx, halfrange=1, min=0, max=line_count - 1
            ):
                for symbol in symbols[line_idx_to_check]:
                    match RelativeSegmentPosition.compute(
                        (symbol.index, symbol.index),
                        (number.start - 1, number.start + number.length),
                    ):
                        case RelativeSegmentPosition.OVERLAP:
                            nearby_symbol_found = True
                            break
                        case RelativeSegmentPosition.RIGHT:
                            break
                if nearby_symbol_found:
                    break
            if nearby_symbol_found:
                part_number_sum += number.value
    print(part_number_sum)


def part_2(inp: str, debug: bool):
    numbers, symbols = parse_input(inp)
    line_count = len(symbols)
    gear_ratios_sum = 0
    for line_idx, symbols_on_line in enumerate(symbols):
        for symbol in symbols_on_line:
            if symbol.char != "*":
                continue
            adjascent_number: list[NumberOnLine] = []
            for line_idx_to_check in vicinity_clamped(
                center=line_idx, halfrange=1, min=0, max=line_count
            ):
                for number in numbers[line_idx_to_check]:
                    match RelativeSegmentPosition.compute(
                        (number.start, number.start + number.length - 1),
                        (symbol.index - 1, symbol.index + 1),
                    ):
                        case RelativeSegmentPosition.OVERLAP:
                            adjascent_number.append(number)
                        case RelativeSegmentPosition.RIGHT:
                            break
            if len(adjascent_number) == 2:
                gear_ratios_sum += adjascent_number[0].value * adjascent_number[1].value

    print(gear_ratios_sum)
