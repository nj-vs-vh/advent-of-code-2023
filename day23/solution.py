import collections
from dataclasses import dataclass
from typing import Literal

from utils import Map, dimensions, format_map, parse_simple_map

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
GraphNodeId = int


@dataclass
class GraphNode:
    id: GraphNodeId
    coords: Coords
    connections: list[tuple[Coords, int]]


HikesGraph = dict[Coords, GraphNode]

_Connections = list[tuple[GraphNodeId, int]]
ListHikesGraph = list[_Connections]


def to_list_graph(g: HikesGraph) -> ListHikesGraph:
    """A compressed graph representation to optimize hot DFS code"""
    res: ListHikesGraph = []
    for node in sorted(g.values(), key=lambda gn: gn.id):
        assert node.id == len(res)
        res.append([(g[adj].id, path_len) for adj, path_len in node.connections])
    return res


def hikes_graph(
    map: Map[Cell],
    start: Coords,
    target: Coords,
    follow_slopes: bool,
) -> HikesGraph:
    height, width = dimensions(map)

    # first, creating "direct graph", tracking what cells are accesible from each cell
    direct_adjacent: dict[Coords, list[Coords]] = dict()
    to_check: set[Coords] = {start}
    while to_check:
        next_to_check: set[Coords] = set()
        for current in to_check:
            i, j = current
            adjacent_to_current = [
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
            direct_adjacent[current] = adjacent_to_current
            next_to_check.update(c for c in adjacent_to_current if c not in direct_adjacent)
        to_check = next_to_check

    graph_node_coords = {
        coords for coords, adjacent in direct_adjacent.items() if len(adjacent) > 2
    }
    graph_node_coords.add(start)
    graph_node_coords.add(target)
    graph_nodes: list[GraphNode] = []
    for node_id, node_coords in enumerate(graph_node_coords):
        node = GraphNode(id=node_id, coords=node_coords, connections=[])
        graph_nodes.append(node)
        for path_start in direct_adjacent[node_coords]:
            path_coords = path_start
            path = []
            while True:
                path.append(path_coords)
                if path_coords in graph_node_coords:
                    node.connections.append((path_coords, len(path)))
                    break
                else:
                    prev_path_coords = path[-2] if len(path) > 1 else node_coords
                    next_path_coords = [
                        c for c in direct_adjacent[path_coords] if c != prev_path_coords
                    ]
                    if not next_path_coords:
                        break  # dead end
                    else:
                        assert (
                            len(next_path_coords) == 1
                        ), f"Ambiguous next path coords: {next_path_coords!r}"
                        path_coords = next(iter(next_path_coords))

    return {gn.coords: gn for gn in graph_nodes}


def longest_path_length_recursive(
    graph: ListHikesGraph,
    start: GraphNodeId,
    target: GraphNodeId,
    visited_mask: int = 0,
    path_acc: int = 0,
) -> int:
    if start == target:
        return path_acc
    visited_mask |= 1 << start
    max_path_len = 0
    for next_, edge_len in graph[start]:
        if not visited_mask & 1 << next_:
            path_len = longest_path_length_recursive(
                graph,
                next_,
                target,
                visited_mask,
                path_acc + edge_len,
            )
            if path_len > max_path_len:
                max_path_len = path_len
    return max_path_len


def longest_path_length_iterative(
    nodes: ListHikesGraph,
    start: GraphNodeId,
    target: GraphNodeId,
) -> int | None:
    stack = list[tuple[GraphNodeId, int, int]]()
    stack.append((start, 0, 0))
    max_path_length: int | None = None
    while stack:
        current, visited, path_len = stack.pop()
        if current == target and (max_path_length is None or path_len > max_path_length):
            max_path_length = path_len
        new_visited = visited | 1 << current
        stack.extend(
            (adjacent, new_visited, path_len + connection_len)
            for adjacent, connection_len in nodes[current]
            if (new_visited & 1 << adjacent) == 0
        )
    return max_path_length


longest_path_length = longest_path_length_recursive


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

    start_coords, target_coords = find_start_and_target(map)
    graph = hikes_graph(map, start_coords, target_coords, follow_slopes=True)
    print(
        longest_path_length(
            to_list_graph(graph),
            start=graph[start_coords].id,
            target=graph[target_coords].id,
        )
    )


def part_2(inp: str, debug: bool):
    map: Map[Cell] = parse_simple_map(inp)
    start_coords, target_coords = find_start_and_target(map)
    graph = hikes_graph(map, start_coords, target_coords, follow_slopes=False)
    print(
        longest_path_length(
            to_list_graph(graph),
            start=graph[start_coords].id,
            target=graph[target_coords].id,
        )
    )
