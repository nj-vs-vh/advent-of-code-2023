import itertools
from enum import Enum, auto
from typing import Any, Generator, Literal, Optional, TypeVar


class Direction(Enum):
    N = auto()
    S = auto()
    E = auto()
    W = auto()

    def inverse(self) -> "Direction":
        match self:
            case Direction.N:
                return Direction.S
            case Direction.S:
                return Direction.N
            case Direction.E:
                return Direction.W
            case Direction.W:
                return Direction.E

    def delta(self) -> tuple[int, int]:
        match self:
            case Direction.N:
                return (-1, 0)
            case Direction.S:
                return (1, 0)
            case Direction.E:
                return (0, 1)
            case Direction.W:
                return (0, -1)


class Pipe(Enum):
    VERT = auto()
    HORIZ = auto()

    # angle numbering by quadrants
    ANGLE_1 = auto()
    ANGLE_2 = auto()
    ANGLE_3 = auto()
    ANGLE_4 = auto()

    def connected_directions(self) -> set[Direction]:
        match self:
            case Pipe.VERT:
                return {Direction.N, Direction.S}
            case Pipe.HORIZ:
                return {Direction.W, Direction.E}
            case Pipe.ANGLE_1:
                return {Direction.N, Direction.E}
            case Pipe.ANGLE_2:
                return {Direction.N, Direction.W}
            case Pipe.ANGLE_3:
                return {Direction.S, Direction.W}
            case Pipe.ANGLE_4:
                return {Direction.S, Direction.E}

    def __str__(self) -> str:
        match self:
            case Pipe.VERT:
                return "┃"
            case Pipe.HORIZ:
                return "━"
            case Pipe.ANGLE_1:
                return "┗"
            case Pipe.ANGLE_2:
                return "┛"
            case Pipe.ANGLE_3:
                return "┓"
            case Pipe.ANGLE_4:
                return "┏"

    def __repr__(self) -> str:
        return f"Pipe({str(self)})"

    @classmethod
    def parse(cls, char: str) -> "Pipe":
        match char:
            case "|":
                return Pipe.VERT
            case "-":
                return Pipe.HORIZ
            case "L":
                return Pipe.ANGLE_1
            case "J":
                return Pipe.ANGLE_2
            case "7":
                return Pipe.ANGLE_3
            case "F":
                return Pipe.ANGLE_4
        raise ValueError(f"Not a valid pipe character: {char}")

    @classmethod
    def infer_from_neighborhood(
        cls,
        north: Optional["Pipe"],
        south: Optional["Pipe"],
        east: Optional["Pipe"],
        west: Optional["Pipe"],
    ) -> "Pipe":
        inferred_directions: set[Direction] = set()
        for pipe, required_direction in zip(
            (north, south, east, west), (Direction.S, Direction.N, Direction.W, Direction.E)
        ):
            if pipe is not None and required_direction in pipe.connected_directions():
                inferred_directions.add(required_direction.inverse())
        for pipe_variant in Pipe:
            if pipe_variant.connected_directions() == inferred_directions:
                return pipe_variant
        else:
            raise ValueError(
                f"Unable to infer pipe orientation from neighboring pipes: {north, south, east, west}"
            )


def arr_size(map: list[list[Any]]) -> tuple[int, int]:
    return len(map), len(map[0])


T = TypeVar("T")


def neighborhood(
    arr: list[list[T]], i: int, j: int
) -> tuple[Optional[T], Optional[T], Optional[T], Optional[T]]:
    height, width = arr_size(arr)
    return (
        arr[i - 1][j] if i > 0 else None,  # north
        arr[i + 1][j] if i < height - 1 else None,  # south
        arr[i][j + 1] if j < width - 1 else None,  # east
        arr[i][j - 1] if j > 0 else None,  # west
    )


Map = list[list[Pipe | None]]


def parse_pipe_map(inp: str) -> tuple[Map, tuple[int, int]]:
    map: Map = []
    start_position: tuple[int, int] | None = None
    for i, line in enumerate(inp.splitlines()):
        map_line: list[Pipe | None] = []
        for j, char in enumerate(line):
            match char:
                case ".":
                    map_line.append(None)
                case "S":
                    map_line.append(None)  # inferred later
                    start_position = (i, j)
                case _:
                    map_line.append(Pipe.parse(char))
        map.append(map_line)

    if start_position is None:
        raise ValueError("No start position found")

    start_pipe = Pipe.infer_from_neighborhood(
        *neighborhood(map, i=start_position[0], j=start_position[1])
    )
    map[start_position[0]][start_position[1]] = start_pipe

    return map, start_position


def follow_pipe(
    map: Map, start_pos: tuple[int, int], start_dir: Direction
) -> Generator[tuple[int, int], None, None]:
    start_pipe = map[start_pos[0]][start_pos[1]]
    assert start_pipe and start_dir in start_pipe.connected_directions()
    position = start_pos
    direction = start_dir
    while True:
        delta = direction.delta()
        position = (position[0] + delta[0], position[1] + delta[1])
        new_pipe = map[position[0]][position[1]]
        if new_pipe is None:
            raise ValueError(f"Arrived at non-pipe cell at {position}")
        direction = next(
            d for d in new_pipe.connected_directions() if d is not direction.inverse()
        )
        yield position


def part_1(inp: str, debug: bool):
    map, start = parse_pipe_map(inp)
    if debug:
        for row in map:
            for cell in row:
                print(cell or " ", end="")
            print()

    start_pipe = map[start[0]][start[1]]
    assert start_pipe
    direction_1, direction_2 = start_pipe.connected_directions()
    for i_step, (p1, p2) in enumerate(
        zip(
            follow_pipe(map, start, direction_1),
            follow_pipe(map, start, direction_2),
        )
    ):
        if p1 == p2:
            print(i_step + 1)
            break


def part_2(inp: str, debug: bool):
    map, start = parse_pipe_map(inp)
    height, width = arr_size(map)

    is_loop = [[False] * width for _ in range(height)]
    is_inside = [[False] * width for _ in range(height)]

    start_pipe = map[start[0]][start[1]]
    assert start_pipe
    direction = next(iter(start_pipe.connected_directions()))
    for pos in follow_pipe(map, start, direction):
        is_loop[pos[0]][pos[1]] = True
        if pos == start:
            break

    for i, row in enumerate(map):
        crossings = 0
        for j, cell in enumerate(row):
            if cell is None or not is_loop[i][j]:
                is_inside[i][j] = crossings % 2 == 1
            elif cell in {Pipe.VERT, Pipe.ANGLE_1, Pipe.ANGLE_2}:
                crossings += 1

    if debug:
        for i, row in enumerate(map):
            for j, cell in enumerate(row):
                print(cell if is_loop[i][j] else ("X" if is_inside[i][j] else " "), end="")
            print()

    print(sum(sum(row) for row in is_inside))

    return map, is_loop, is_inside
