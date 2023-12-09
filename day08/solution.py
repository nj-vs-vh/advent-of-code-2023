import itertools
import math
import re
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Generator, Optional

Network = dict[str, tuple[str, str]]

NODE_LINE_REGEX = re.compile(r"(\w+) = \((\w+), (\w+)\)")

def parse_network(input: str) -> Network:
    res: Network = {}
    for line in input.splitlines():
        m = NODE_LINE_REGEX.match(line)
        if not m:
            continue
        res[m.group(1)] = (m.group(2), m.group(3))
    return res


class Turn(Enum):
    L = "L"
    R = "R"

    def __str__(self) -> str:
        return self.value


Directions = list[Turn]


def parse_directions(inp: str) -> Directions:
    first_line = inp.split("\n", 1)[0]
    return [Turn(char) for char in first_line]


def follow_directions(network: Network, start_node: str, directions: Directions) -> Generator[str, None, None]:
    current = start_node
    for turn in itertools.cycle(directions):
        yield current
        match turn:
            case Turn.L:
                current = network[current][0]
            case Turn.R:
                current = network[current][1]


def part_1(inp: str, debug: bool):
    directions = parse_directions(inp)
    network =parse_network(inp)
    if debug:
        print(*directions, sep=", ")
        for n in network:
            print(n)
    for idx, node in enumerate(follow_directions(network, start_node="AAA", directions=directions)):
        if debug:
            print("Current node: ", node)
        if node == "ZZZ":
            print(idx)
            return


@dataclass
class ZNodeCycle:
    period: int
    start_offset: int
    end_node_phase: int


def end_node_indices(nodes: list[str]) -> list[int]:
    return [idx for idx, node in enumerate(nodes) if node.endswith("Z")]


def part_2(inp: str, debug: bool):
    directions = parse_directions(inp)
    network = parse_network(inp)

    start_nodes = [node for node in network if node.endswith("A")]
    cycles: list[ZNodeCycle] = []
    # looking for cycles = arriving at the same node on the same directions cycle phase
    for start_node in start_nodes:
        trace: list[str] = []
        period: Optional[int] = None
        for node in follow_directions(network, start_node, directions):
            trace.append(node)
            for cycle_multiplier in range(1, len(trace) // len(directions) + 1):
                test_cycle_length = cycle_multiplier * len(directions)
                if test_cycle_length >= len(trace):
                    continue
                if trace[-1] is trace[-1 - test_cycle_length]:
                    period = cycle_multiplier * len(directions)
                    break
            if period is not None:
                break

        assert period
        cycle_start_offset = len(trace) - period - 1

        if debug:
            print(f"{cycle_start_offset = }, {period = }, {end_node_indices(trace) = }")

        cycles.append(
            ZNodeCycle(
                period=period,
                # NOTE: this relies on the assumption that there is only one Z node in the cycle,
                # which is true for my input, but is not explicitly written into the problem statement
                start_offset=cycle_start_offset,
                end_node_phase=end_node_indices(trace[cycle_start_offset:])[0],
            )
        )

    if debug:
        print(*cycles, sep="\n")

    for c in cycles:
        # special condition for challenge inputs that allows the use of LCM
        assert c.start_offset + c.end_node_phase == c.period

    print(math.lcm(*[c.period for c in cycles]))
