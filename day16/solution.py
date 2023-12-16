import itertools
from enum import IntFlag, auto
from typing import Callable, Literal, TypeVar

Mirror = Literal["/", "\\"]
BeamSplitter = Literal["|", "-"]
Contraption = list[list[Mirror | BeamSplitter | None]]


def parse_contraption(inp: str) -> Contraption:
    return [[char if char != "." else None for char in line] for line in inp.splitlines()]  # type: ignore


T = TypeVar("T")


def format_map(
    map: list[list[T]], formatter: Callable[[T], str] = str, cell_width: int = 1
) -> str:
    horizontal_bound = " " + "-" * len(map[0]) * cell_width + " "
    return "\n".join(
        [horizontal_bound]
        + [
            "".join(["|"] + [formatter(cell).center(cell_width, " ") for cell in row] + ["|"])
            for row in map
        ]
        + [horizontal_bound]
    )


class LightDirection(IntFlag):
    Up = auto()
    Right = auto()
    Down = auto()
    Left = auto()

    def __str__(self) -> str:
        return {
            LightDirection.Up: "^",
            LightDirection.Right: ">",
            LightDirection.Down: "V",
            LightDirection.Left: "<",
            LightDirection.Up | LightDirection.Down: "⇅",
            LightDirection.Left | LightDirection.Right: "⇆",
        }.get(self, str(self.bit_count()))

    def delta(self) -> tuple[int, int]:
        match self:
            case LightDirection.Up:
                return -1, 0
            case LightDirection.Right:
                return 0, 1
            case LightDirection.Down:
                return 1, 0
            case LightDirection.Left:
                return 0, -1

    def reflect_from(self, mirror: Mirror) -> "LightDirection":
        match mirror:
            case "\\":
                match self:
                    case LightDirection.Up:
                        return LightDirection.Left
                    case LightDirection.Left:
                        return LightDirection.Up
                    case LightDirection.Down:
                        return LightDirection.Right
                    case LightDirection.Right:
                        return LightDirection.Down
            case "/":
                match self:
                    case LightDirection.Up:
                        return LightDirection.Right
                    case LightDirection.Right:
                        return LightDirection.Up
                    case LightDirection.Down:
                        return LightDirection.Left
                    case LightDirection.Left:
                        return LightDirection.Down


LightMap = list[list[LightDirection]]
ECache = list[list[list[int]]]  # [i][j][direction.bit_length()] = energization caused by the beam


def fill_lightmap(
    contraption: Contraption,
    lightmap: LightMap,
    ecache: ECache,
    start: tuple[int, int],
    direction: LightDirection,
) -> int:
    i, j = start
    e_tracked = 0
    di, dj = direction.delta()
    track: list[tuple[int, int, LightDirection]] = []
    while 0 <= i < len(contraption) and 0 <= j < len(contraption[i]):
        if direction in lightmap[i][j]:
            break
        if lightmap[i][j] == 0:
            e_tracked += 1
        track.append((i, j, direction))
        lightmap[i][j] |= direction
        if part := contraption[i][j]:
            match part:
                case "\\" | "/":
                    direction = direction.reflect_from(part)
                    di, dj = direction.delta()
                case "-":
                    if direction in {LightDirection.Up, LightDirection.Down}:
                        e_tracked += fill_lightmap(
                            contraption, lightmap, ecache, (i, j), LightDirection.Left
                        )
                        e_tracked += fill_lightmap(
                            contraption, lightmap, ecache, (i, j), LightDirection.Right
                        )
                        break
                case "|":
                    if direction in {LightDirection.Left, LightDirection.Right}:
                        e_tracked += fill_lightmap(
                            contraption, lightmap, ecache, (i, j), LightDirection.Up
                        )
                        e_tracked += fill_lightmap(
                            contraption, lightmap, ecache, (i, j), LightDirection.Down
                        )
                        break
        i += di
        j += dj

    # if we have found a loop - need to add it's energization to the current track
    # if 0 <= i < len(contraption) and 0 <= j < len(contraption[i]):
    #     e_total += ecache[i][j][direction.bit_length() - 1]

    # if the current function found some new track, we need to fill it with energization levels
    # for track_idx, (i, j, direction) in enumerate(track):
    #     ecache[i][j][direction.bit_length() - 1] = e_tracked - track_idx
    return e_tracked


def part_1(inp: str, debug: bool):
    contraption = parse_contraption(inp)
    if debug:
        print(format_map(contraption, lambda p: p if p is not None else " "))
    lightmap: LightMap = [[LightDirection(0)] * len(row) for row in contraption]
    ecache = [[[0] * 4 for _ in range(len(row))] for row in contraption]
    result = fill_lightmap(
        contraption,
        lightmap,
        ecache,
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
    ecache = [[[0] * 4 for _ in range(len(row))] for row in contraption]
    results = []
    for i, j, direction in itertools.chain(
        [(i, 0, LightDirection.Right) for i in range(height)],
        [(i, width - 1, LightDirection.Left) for i in range(height)],
        [(0, j, LightDirection.Down) for j in range(width)],
        [(height - 1, j, LightDirection.Up) for j in range(width)],
    ):
        lightmap: LightMap = [[LightDirection(0)] * len(row) for row in contraption]
        results.append(
            fill_lightmap(
                contraption,
                lightmap,
                ecache,
                start=(i, j),
                direction=direction,
            )
        )
    print(max(results))
