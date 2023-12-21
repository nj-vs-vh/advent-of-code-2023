import enum
import itertools
from typing import Any, Iterable, Literal, Mapping

from utils import dimensions, format_map, init_map_like, sparse_to_dense_map

Cell = Literal[".", "#"]
EMPTY: Cell = "."
ROCK: Cell = "#"
Map = list[list[Cell]]


def parse_input(inp: str) -> tuple[Map, tuple[int, int]]:
    map_: Map = []
    start: tuple[int, int] | None = None
    for i, line in enumerate(inp.splitlines()):
        row: list[Cell] = []
        map_.append(row)
        for j, char in enumerate(line):
            match char:
                case "S":
                    row.append(".")
                    start = (i, j)
                case ".":
                    row.append(".")
                case "#":
                    row.append("#")
                case _:
                    raise ValueError("Unexpected char")
    assert start is not None, "No start found"
    return map_, start


class Tiling(enum.IntFlag):
    UP = enum.auto()
    RIGHT = enum.auto()
    DOWN = enum.auto()
    LEFT = enum.auto()


def distance_map(
    map: Map,
    start: tuple[int, int],
    steps: int | None = None,
    tiling: Tiling = Tiling(0),
) -> dict[tuple[int, int], int]:
    if tiling != Tiling(0) and steps is None:
        raise ValueError("Max steps argument is required with tiling")

    height, width = dimensions(map)

    def can_go_to(i: int, j: int) -> bool:
        if (i < 0 and Tiling.UP in tiling) or (i >= height and Tiling.DOWN in tiling):
            i = i % height
        if (j < 0 and Tiling.LEFT in tiling) or (j >= width and Tiling.RIGHT in tiling):
            j = j % height
        return 0 <= i < height and 0 <= j < width and map[i][j] == "."

    res = dict[tuple[int, int], int]()
    to_check = [start]
    for step in range(steps + 1) if steps is not None else itertools.count():
        to_check_next: list[tuple[int, int]] = []
        for i, j in to_check:
            if (i, j) in res:
                continue
            res[(i, j)] = step
            to_check_next.extend(
                (i_next, j_next)
                for i_next, j_next in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
                if can_go_to(i_next, j_next)
            )
        if to_check_next:
            to_check = to_check_next
        else:
            break

    return res


def count_dists(
    ds: Mapping[Any, int],
    parity: bool = True,
    max_dist: int | None = None,
) -> int:
    return sum(1 for d in ds.values() if d % 2 != parity and (max_dist is None or d <= max_dist))


def print_distance_map(sparse_map: dict[tuple[int, int], int], side: int):
    dense, _ = sparse_to_dense_map(sparse_map, default=None)
    print(format_map(dense, cell_width=4, rulers_each=side))


def part_1(inp: str, debug: bool):
    map, start = parse_input(inp)
    if debug:
        print(format_map(map, cell_width=3))

    distance = distance_map(map, start, steps=64)
    if debug:
        print_distance_map(distance, side=len(map))

    print(count_dists(distance, max_dist=64))


def part_2(inp: str, debug: bool):
    map, start = parse_input(inp)
    height, width = dimensions(map)

    # simplifies the problem a bit
    assert width == height
    side = width
    if debug:
        print(format_map(map, cell_width=3))

    total_steps = 26501365
    global_parity = total_steps % 2 == 0

    # simplifies edge line positioning
    assert (total_steps - side // 2) % side == 0
    tiles_radius = 1 + (total_steps - side // 2) // side
    if debug:
        print("tiles radius: ", tiles_radius)

    center_distance_map = distance_map(map, start)
    if debug:
        print_distance_map(center_distance_map, side=side)

    for i_range, j_range in (
        (range(0, side), range(0, 1)),
        (range(0, side), range(side - 1, side)),
        (range(0, 1), range(0, side)),
        (range(side - 1, side), range(0, side)),
    ):
        # validate that the map hase clear "lanes" at the center
        # also, that it can be travrsed at it's outer edge, which lets us build "meta-map" later
        edge = [center_distance_map[i, j] for (i, j) in itertools.product(i_range, j_range)]
        assert edge == list(range(side - 1, side // 2, -1)) + list(range(side // 2, side))

    # going over the map edge doesn't change the parity = we can always count even dist coords
    assert (side // 2 + 1) % 2 == 0

    inner_tiles = 1 + 2 * (tiles_radius - 1) * (tiles_radius - 2)
    even_inner_tiles = (1 + ((tiles_radius - 2) // 2) * 2) ** 2
    odd_inner_tiles = (((tiles_radius - 1) // 2) * 2) ** 2
    if debug:
        print("inner tile count:", inner_tiles)
        print("... of them even:", even_inner_tiles)
        print("...          odd:", odd_inner_tiles)

    inner_even = (even_inner_tiles), count_dists(center_distance_map, parity=global_parity)
    inner_odd = (odd_inner_tiles), count_dists(center_distance_map, parity=not global_parity)

    vertice_parity = global_parity ^ (tiles_radius - 1) % 2 == 0
    downmost = count_dists(
        distance_map(map, (0, side // 2)), parity=vertice_parity, max_dist=side - 1
    )
    leftmost = count_dists(
        distance_map(map, (side // 2, side - 1)), parity=vertice_parity, max_dist=side - 1
    )
    uppermost = count_dists(
        distance_map(map, (side - 1, side // 2)), parity=vertice_parity, max_dist=side - 1
    )
    rightmost = count_dists(
        distance_map(map, (side // 2, 0)), parity=vertice_parity, max_dist=side - 1
    )
    edge_parity = not vertice_parity
    edge_length = tiles_radius - 2
    iedge_local_dist = side - 1 + side // 2
    rd_edge_inner = count_dists(
        distance_map(map, (0, 0)), parity=edge_parity, max_dist=iedge_local_dist
    )
    ru_edge_inner = count_dists(
        distance_map(map, (side - 1, 0)), parity=edge_parity, max_dist=iedge_local_dist
    )
    ld_edge_inner = count_dists(
        distance_map(map, (0, side - 1)), parity=edge_parity, max_dist=iedge_local_dist
    )
    lu_edge_inner = count_dists(
        distance_map(map, (side - 1, side - 1)), parity=edge_parity, max_dist=iedge_local_dist
    )
    oedge_local_dist = side // 2 - 1
    rd_edge_outer = count_dists(
        distance_map(map, (0, 0)), parity=not edge_parity, max_dist=oedge_local_dist
    )
    ru_edge_outer = count_dists(
        distance_map(map, (side - 1, 0)), parity=not edge_parity, max_dist=oedge_local_dist
    )
    ld_edge_outer = count_dists(
        distance_map(map, (0, side - 1)), parity=not edge_parity, max_dist=oedge_local_dist
    )
    lu_edge_outer = count_dists(
        distance_map(map, (side - 1, side - 1)), parity=not edge_parity, max_dist=oedge_local_dist
    )
    if debug:
        print("inner even", inner_even)
        print("inner odd", inner_odd)

        print("vertice parity", vertice_parity)
        print("down", downmost, "left", leftmost, "up", uppermost, "right", rightmost)

        print(
            "INNER\nedge parity",
            edge_parity,
            "| length",
            edge_length,
            "| local dist",
            iedge_local_dist,
        )
        print("RD", rd_edge_inner, "RU", ru_edge_inner, "LD", ld_edge_inner, "LU", lu_edge_inner)
        print(
            "OUTER\nedge parity",
            not edge_parity,
            "| length",
            1 + edge_length,
            "| local dist",
            oedge_local_dist,
        )
        print("RD", rd_edge_outer, "RU", ru_edge_outer, "LD", ld_edge_outer, "LU", lu_edge_outer)

    def multiply(nums: tuple[int, int]):
        return nums[0] * nums[1]

    answer = (
        multiply(inner_even)
        + multiply(inner_odd)
        + downmost
        + leftmost
        + uppermost
        + rightmost
        + edge_length * (ru_edge_inner + lu_edge_inner + rd_edge_inner + ld_edge_inner)
        + (edge_length + 1) * (ru_edge_outer + lu_edge_outer + rd_edge_outer + ld_edge_outer)
    )

    print(answer)

    if debug:
        full_map = distance_map(
            map,
            start,
            steps=total_steps,
            tiling=Tiling.UP | Tiling.RIGHT | Tiling.DOWN | Tiling.LEFT,
        )
        # print_distance_map(full_map, side=side)
        answer_control = count_dists(full_map, parity=global_parity)
        print(answer_control)
        assert answer == answer_control
