import collections
import itertools
import sys
from dataclasses import dataclass
from typing import Iterable, Literal, NamedTuple, cast

from utils import Map, dimensions, format_map, parse_simple_map, sparse_to_dense_map

Forest = Literal["#"]
Path = Literal["."]
Slope = Literal[">", "<", "v", "^"]
Cell = Forest | Path | Slope
Coords = tuple[int, int]


def slope_direction(slope: Cell) -> Coords:
    match slope:
        case ">":
            return (0, 1)
        case "<":
            return (0, -1)
        case "v":
            return (1, 0)
        case "^":
            return (-1, 0)
        case _:
            return (0, 0)


Coords = tuple[int, int]
Path = list[Coords]


@dataclass
class GraphNode:
    coords: Coords
    connections: list[tuple[Coords, Path]]


def hikes_graph(
    map: Map[Cell],
    start: Coords,
    target: Coords,
    follow_slopes: bool,
) -> list[GraphNode]:
    height, width = dimensions(map)
    direct_adjascent: dict[Coords, list[Coords]] = dict()
    to_check: set[Coords] = {start}
    while to_check:
        next_to_check: set[Coords] = set()
        for current in to_check:
            i, j = current
            adjascent_to_current = [
                (i_new, j_new)
                for (di, dj, i_new, j_new) in (
                    (-1, 0, i - 1, j),
                    (1, 0, i + 1, j),
                    (0, -1, i, j - 1),
                    (0, 1, i, j + 1),
                )
                if (
                    0 <= i_new < height
                    and 0 <= j_new < width
                    and map[i_new][j_new] != "#"
                    and (
                        not follow_slopes
                        or (map[i][j] == "." or (di, dj) == slope_direction(map[i][j]))
                    )
                )
            ]
            direct_adjascent[current] = adjascent_to_current
            next_to_check.update(c for c in adjascent_to_current if c not in direct_adjascent)
        to_check = next_to_check

    graph_node_coords = {
        coords for coords, adjascent in direct_adjascent.items() if len(adjascent) > 2
    }
    graph_node_coords.add(start)
    graph_node_coords.add(target)
    graph_nodes: list[GraphNode] = []
    for node_coords in graph_node_coords:
        node = GraphNode(node_coords, [])
        graph_nodes.append(node)
        for path_start in direct_adjascent[node_coords]:
            path_coords = path_start
            path = []
            while True:
                path.append(path_coords)
                if path_coords in graph_node_coords:
                    node.connections.append((path_coords, path))
                    break
                else:
                    prev_path_coords = path[-2] if len(path) > 1 else node_coords
                    next_path_coords = [
                        c for c in direct_adjascent[path_coords] if c != prev_path_coords
                    ]
                    if not next_path_coords:
                        break  # dead end
                    else:
                        assert (
                            len(next_path_coords) == 1
                        ), f"Ambiguous next path coords: {next_path_coords!r}"
                        path_coords = next(iter(next_path_coords))

    return graph_nodes


def longest_path_length(
    nodes: dict[Coords, GraphNode],
    from_: Coords,
    to: Coords,
    _visited: set[Coords] | None = None,
) -> int | None:
    if from_ == to:
        return 0
    else:
        _visited = _visited.copy() if _visited else set()
        _visited.add(from_)
        path_lengths: list[int] = []
        for adjascent, path in nodes[from_].connections:
            if adjascent in _visited:
                continue
            subpath_length = longest_path_length(
                nodes,
                from_=adjascent,
                to=to,
                _visited=_visited,
            )
            if subpath_length is not None:
                path_lengths.append(len(path) + subpath_length)

        return max(path_lengths) if path_lengths else None


def find_start_and_target(map: Map[Cell]) -> tuple[Coords, Coords]:
    height, _ = dimensions(map)
    return (
        (0, next(i for i, c in enumerate(map[0]) if c == ".")),
        (height - 1, next(i for i, c in enumerate(map[height - 1]) if c == ".")),
    )


def part_1(inp: str, debug: bool):
    map: Map[Cell] = parse_simple_map(inp)

    if debug:
        print(format_map(map, cell_width=2))

    start, target = find_start_and_target(map)
    nodes = {n.coords: n for n in hikes_graph(map, start, target, follow_slopes=True)}
    print(longest_path_length(nodes, from_=start, to=target))


def part_2(inp: str, debug: bool):
    map: Map[Cell] = parse_simple_map(inp)
    start, target = find_start_and_target(map)
    nodes = {n.coords: n for n in hikes_graph(map, start, target, follow_slopes=False)}
    print(longest_path_length(nodes, start, target))
