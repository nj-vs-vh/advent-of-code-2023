import functools
import operator
import re
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Number:
    value: int
    row: int
    col: int

    def __str__(self) -> str:
        return str(self.value)


def parse_input(inp: str) -> list[list[Number | str | None]]:
    number_re = re.compile(r"\d+")
    symbol_re = re.compile(r"[^\d\.]")
    blank_re = re.compile(r"\.+")

    res: list[list[Number | str | None]] = []
    for row, line in enumerate(inp.splitlines()):
        res_line: list[Number | str | None] = []
        col = 0
        while col < len(line):
            if number_match := number_re.match(line, pos=col):
                number_str = number_match.group()
                res_line.extend(
                    [Number(value=int(number_str), row=row, col=col)] * len(number_str)
                )
                col += len(number_str)
            elif symbol_match := symbol_re.match(line, pos=col):
                res_line.append(symbol_match.group())
                col += 1
            elif blank_match := blank_re.match(line, pos=col):
                res_line.extend([None] * len(blank_match.group()))
                col += len(blank_match.group())
            else:
                raise ValueError(f"Unexpected symbol at ({row}, {col}): {line!r}")
        res.append(res_line)

    return res


def neighborhood(i: int, j: int, width: int, height: int) -> Iterable[tuple[int, int]]:
    delta = 1
    for i_neighbor in range(max(i - delta, 0), min(i + delta + 1, height)):
        for j_neighbor in range(max(j - delta, 0), min(j + delta + 1, width)):
            if not (i_neighbor == i and j_neighbor == j):
                yield (i_neighbor, j_neighbor)


def part_1(inp: str, debug: bool):
    schematic = parse_input(inp)
    if debug:
        print(inp)
        for row in schematic:
            print("|", end="")
            for item in row:
                print(f"{str(item or ' '): ^5}|", end="")
            print()

    height = len(schematic)
    width = len(schematic[0])
    parts: set[Number] = set()
    for i, row in enumerate(schematic):
        for j, item in enumerate(row):
            if isinstance(item, str):
                for i_n, j_n in neighborhood(i, j, width, height):
                    neighbor = schematic[i_n][j_n]
                    if isinstance(neighbor, Number):
                        if debug:
                            print("Found part ", neighbor)
                        parts.add(neighbor)

    print(sum(p.value for p in parts))


def part_2(inp: str, debug: bool):
    schematic = parse_input(inp)
    if debug:
        print(inp)
        for row in schematic:
            print("|", end="")
            for item in row:
                print(f"{str(item or ' '): ^5}|", end="")
            print()

    height = len(schematic)
    width = len(schematic[0])
    total_gear_ratio = 0
    for i, row in enumerate(schematic):
        for j, item in enumerate(row):
            if item == "*":
                adjacent_parts: set[Number] = set()
                for i_n, j_n in neighborhood(i, j, width, height):
                    neighbor = schematic[i_n][j_n]
                    if isinstance(neighbor, Number):
                        if debug:
                            print("Found part ", neighbor)
                        adjacent_parts.add(neighbor)
                if len(adjacent_parts) == 2:
                    total_gear_ratio += functools.reduce(
                        operator.mul, (p.value for p in adjacent_parts), 1
                    )

    print(total_gear_ratio)
