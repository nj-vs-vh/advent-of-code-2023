import collections
import itertools
import random

Graph = dict[str, set[str]]


def parse_graph(inp: str) -> Graph:
    res: Graph = collections.defaultdict(set)
    for line in inp.splitlines():
        node, connections = line.split(": ")
        connections = [n.strip() for n in connections.split()]
        res[node].update(connections)
        for connected in connections:
            res[connected].add(node)
    return res


def shortest_paths_from_node(graph: Graph, start: str) -> list[list[str]]:
    path_to: dict[str, list[str]] = dict()
    path_to[start] = [start]
    to_visit = {start}
    while to_visit:
        to_visit_next = set()
        for current in to_visit:
            for next in graph[current]:
                if next in path_to:
                    continue
                to_visit_next.add(next)
                path_to[next] = path_to[current] + [next]
        to_visit = to_visit_next
    return list(path_to.values())


Edge = tuple[str, str]


def to_edge(u: str, v: str) -> Edge:
    return (u, v) if u < v else (v, u)


def calculate_edge_usage(graph: Graph, node_fraction: float = 1.0) -> dict[Edge, int]:
    res: dict[Edge, int] = collections.defaultdict(lambda: 0)
    for node in graph:
        if random.random() > node_fraction:
            continue
        for path in shortest_paths_from_node(graph, start=node):
            for u, v in itertools.pairwise(path):
                res[to_edge(u, v)] += 1
    return res


def disconnected_subgraph_sizes(
    graph: Graph, removed_edges: tuple[Edge, Edge, Edge]
) -> tuple[int, int] | None:
    visited: set[str] = set()
    to_visit = {next(iter(graph))}
    while to_visit:
        to_visit_next: set[str] = set()
        for current in to_visit:
            visited.add(current)
            for next_ in graph[current]:
                if next_ in visited or to_edge(current, next_) in removed_edges:
                    continue
                to_visit_next.add(next_)
        to_visit = to_visit_next
    if len(visited) == len(graph):
        return None
    else:
        return len(graph) - len(visited), len(visited)


def part_1(inp: str, debug: bool):
    graph = parse_graph(inp)
    edge_usage = calculate_edge_usage(
        graph,
        node_fraction=0.05,
    )
    max_usage = max(edge_usage.values())
    min_usage = min(edge_usage.values())
    assumed_cut_usage_frac = 0.3  # assume cut edges are whithin this frac of max usage
    threshold_usage = min_usage + (max_usage - min_usage) * (1 - assumed_cut_usage_frac)
    cut_candidates = [e for e, usage in edge_usage.items() if usage > threshold_usage]
    for cut_1 in cut_candidates:
        for cut_2 in cut_candidates:
            for cut_3 in cut_candidates:
                if cut_1 == cut_2 or cut_2 == cut_3 or cut_1 == cut_2:
                    continue

                if sizes := disconnected_subgraph_sizes(graph, (cut_1, cut_2, cut_3)):
                    print("cuts:", cut_1, cut_2, cut_3)
                    print(sizes[0] * sizes[1])
                    return
    raise RuntimeError("Cut not found!")


def part_2(inp: str, debug: bool):
    pass
