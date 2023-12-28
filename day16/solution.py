import itertools
from typing import Literal

from utils import format_map

Mirror = Literal["/", "\\"]
BeamSplitter = Literal["|", "-"]
Contraption = list[list[Mirror | BeamSplitter | None]]


def parse_contraption(inp: str) -> Contraption:
    return [[char if char != "." else None for char in line] for line in inp.splitlines()]  # type: ignore


LightDirectionCode = Literal[0, 1, 2, 4, 8]


class LightDirection:  # similar to enum.IntFlag, but faster
    Up: LightDirectionCode = 1
    Right: LightDirectionCode = 2
    Left: LightDirectionCode = 4
    Down: LightDirectionCode = 8


def delta(dir: LightDirectionCode) -> tuple[int, int]:
    match dir:
        case LightDirection.Up:
            return -1, 0
        case LightDirection.Right:
            return 0, 1
        case LightDirection.Down:
            return 1, 0
        case LightDirection.Left:
            return 0, -1
        case _:
            raise RuntimeError()


def reflect_from(dir: LightDirectionCode, mirror: Mirror) -> "LightDirectionCode":
    match mirror:
        case "\\":
            match dir:
                case LightDirection.Up:
                    return LightDirection.Left
                case LightDirection.Left:
                    return LightDirection.Up
                case LightDirection.Down:
                    return LightDirection.Right
                case LightDirection.Right:
                    return LightDirection.Down
        case "/":
            match dir:
                case LightDirection.Up:
                    return LightDirection.Right
                case LightDirection.Right:
                    return LightDirection.Up
                case LightDirection.Down:
                    return LightDirection.Left
                case LightDirection.Left:
                    return LightDirection.Down
    raise RuntimeError()


LightMap = list[list[LightDirectionCode]]


def fill_lightmap(
    contraption: Contraption,
    lightmap: LightMap,
    start: tuple[int, int],
    direction: LightDirectionCode,
) -> int:
    i, j = start
    di, dj = delta(direction)
    energization = 0
    while (
        0 <= i < len(contraption)
        and 0 <= j < len(contraption[i])
        and lightmap[i][j] & direction == 0
    ):
        if lightmap[i][j] == 0:
            energization += 1
        lightmap[i][j] |= direction  # type: ignore
        if part := contraption[i][j]:
            match part:
                case "\\" | "/":
                    direction = reflect_from(direction, part)
                    di, dj = delta(direction)
                case "-":
                    if direction in {LightDirection.Up, LightDirection.Down}:
                        energization += fill_lightmap(
                            contraption, lightmap, (i, j), LightDirection.Left
                        )
                        energization += fill_lightmap(
                            contraption, lightmap, (i, j), LightDirection.Right
                        )
                        break
                case "|":
                    if direction in {LightDirection.Left, LightDirection.Right}:
                        energization += fill_lightmap(
                            contraption, lightmap, (i, j), LightDirection.Up
                        )
                        energization += fill_lightmap(
                            contraption, lightmap, (i, j), LightDirection.Down
                        )
                        break
        i += di
        j += dj

    return energization


def empty_lightmap(contraption: Contraption) -> LightMap:
    return [[0] * len(row) for row in contraption]


def part_1(inp: str, debug: bool):
    contraption = parse_contraption(inp)
    if debug:
        print(format_map(contraption, lambda p: p if p is not None else " "))
    lightmap = empty_lightmap(contraption)
    result = fill_lightmap(
        contraption,
        lightmap,
        start=(0, 0),
        direction=LightDirection.Right,
    )
    if debug:
        print(format_map(lightmap, lambda p: str(p) if p else " "))
    print(result)


def part_2(inp: str, debug: bool):
    contraption = parse_contraption(inp)
    height = len(contraption)
    width = len(contraption[1])
    results: list[int] = []
    for i, j, direction in itertools.chain(
        [(i, 0, LightDirection.Right) for i in range(height)],
        [(i, width - 1, LightDirection.Left) for i in range(height)],
        [(0, j, LightDirection.Down) for j in range(width)],
        [(height - 1, j, LightDirection.Up) for j in range(width)],
    ):
        lightmap = empty_lightmap(contraption)
        results.append(
            fill_lightmap(
                contraption,
                lightmap,
                start=(i, j),
                direction=direction,
            )
        )
    print(max(results))
