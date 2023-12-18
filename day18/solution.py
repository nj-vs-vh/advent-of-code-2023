import itertools
import re
from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Optional

from utils import format_map


class Dir(Enum):
    U = "U"
    R = "R"
    D = "D"
    L = "L"

    def delta(self) -> tuple[int, int]:
        match self:
            case Dir.U:
                return (-1, 0)
            case Dir.R:
                return (0, 1)
            case Dir.D:
                return (1, 0)
            case Dir.L:
                return (0, -1)

    def inverse(self) -> "Dir":
        match self:
            case Dir.U:
                return Dir.D
            case Dir.R:
                return Dir.L
            case Dir.D:
                return Dir.U
            case Dir.L:
                return Dir.R


@dataclass
class DigInstruction:
    direction: Dir
    steps: int


def iter_dig_instructions(inp: str, from_color: bool) -> Iterable[DigInstruction]:
    regex = re.compile(r"(U|R|D|L) (\d+) \(#([\d\w]+)\)")
    for m in regex.finditer(inp):
        color_code = m.group(3)
        if from_color:
            direction_encoding = {"0": Dir.R, "1": Dir.D, "2": Dir.L, "3": Dir.U}
            yield DigInstruction(
                direction=direction_encoding[color_code[-1]],
                steps=int(color_code[:5], base=16),
            )
        else:
            yield DigInstruction(
                direction=Dir(m.group(1)),
                steps=int(m.group(2)),
            )


@dataclass
class Vertex:
    i: int
    j: int
    connects: set[Dir]


def interval_intersection_len(s1: tuple[int, int], s2: tuple[int, int]) -> int:
    intersection_start = max(s1[0], s2[0])
    intersection_end = min(s1[1], s2[1])
    return max(0, intersection_end - intersection_start + 1)


def solve(inp: str, debug: bool, instructions_from_color: bool):
    current = Vertex(0, 0, connects=set())
    vertices: list[Vertex] = [current]
    for instruction in iter_dig_instructions(inp, from_color=instructions_from_color):
        current.connects.add(instruction.direction)
        di, dj = instruction.direction.delta()
        current = Vertex(
            i=current.i + instruction.steps * di,
            j=current.j + instruction.steps * dj,
            connects={instruction.direction.inverse()},
        )
        vertices.append(current)
    start = vertices[0]
    end = vertices[-1]
    if start.i == end.i and start.j == end.j:
        start.connects.update(end.connects)
        vertices.pop(-1)

    if debug:
        print("\nVertices")
        print(*vertices, sep="\n")

    i_slice_edges = sorted({vertex.i for vertex in vertices})

    # subdivide vertical edges at slice edges
    additional_vertices: list[Vertex] = []
    for edge_start, edge_end in itertools.pairwise(vertices + [vertices[0]]):
        if edge_start.j == edge_end.j:  # = is edge vertical
            i_edge_min = min(edge_start.i, edge_end.i)
            i_edge_max = max(edge_start.i, edge_end.i)
            for i_break in i_slice_edges:
                if i_edge_min < i_break < i_edge_max:
                    additional_vertices.append(
                        Vertex(i=i_break, j=edge_start.j, connects={Dir.U, Dir.D})
                    )
                elif i_break >= i_edge_max:
                    break

    if debug:
        print("\nAdditional vertices")
        print(*additional_vertices, sep="\n")

    if debug:
        i_min = min(v.i for v in vertices)
        i_max = max(v.i for v in vertices)
        j_min = min(v.j for v in vertices)
        j_max = max(v.j for v in vertices)
        print(f"\nTop-left corner = ({i_min}, {j_min})")
        map_ = [["."] * (j_max - j_min + 1) for _ in range(i_max - i_min + 1)]
        for v_start, v_end in itertools.pairwise(vertices + [vertices[0]]):
            for i_edge in range(min(v_start.i, v_end.i), max(v_start.i, v_end.i) + 1):
                for j_edge in range(min(v_start.j, v_end.j), max(v_start.j, v_end.j) + 1):
                    map_[i_edge - i_min][j_edge - j_min] = "•"
            map_[v_start.i - i_min][v_start.j - j_min] = "O"
        map_[vertices[0].i - i_min][vertices[0].j - j_min] = "O"
        for v in additional_vertices:
            map_[v.i - i_min][v.j - j_min] = "X"
        print(format_map(map_))

    # go from slice to slice and calculate areas, subtracting row overlap
    all_vertices = sorted(itertools.chain(vertices, additional_vertices), key=lambda vert: vert.j)
    total_area = 0
    prev_j_intervals: Optional[list[tuple[int, int]]] = None
    for i_start, i_end in itertools.pairwise(i_slice_edges):
        slice_height = 1 + i_end - i_start

        j_edges = [
            vertex.j for vertex in all_vertices if vertex.i == i_start and Dir.D in vertex.connects
        ]
        # assert len(j_edges) % 2 == 0, j_edges
        j_intervals = [(j_start, j_end) for j_start, j_end in zip(j_edges[::2], j_edges[1::2])]
        slice_width_total = sum(1 + j_end - j_start for j_start, j_end in j_intervals)

        horizontal_intervals_overlap = (
            sum(
                sum(
                    interval_intersection_len(interval, prev_interval)
                    for prev_interval in prev_j_intervals
                )
                for interval in j_intervals
            )
            if prev_j_intervals is not None
            else 0
        )
        prev_j_intervals = j_intervals

        slice_area = slice_height * slice_width_total - horizontal_intervals_overlap
        if debug:
            print(
                f"{i_start = }, {i_end = }, {j_edges = }, "
                + f"{j_intervals = }, {slice_height = }, {slice_width_total = }, "
                + f"{horizontal_intervals_overlap = }, {slice_area = }"
            )
        total_area += slice_area

    print(total_area)


def part_1(inp: str, debug: bool):
    solve(inp, debug, instructions_from_color=False)


def part_2(inp: str, debug: bool):
    solve(inp, debug, instructions_from_color=True)
