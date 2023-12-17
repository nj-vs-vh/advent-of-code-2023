from typing import Literal, NamedTuple, Optional
import heapq

from utils import format_map


def parse_input(inp: str) -> list[list[int]]:
    return [[int(char) for char in line] for line in inp.splitlines()]


Direction = Literal["^", "v", "<", ">"]
DIRECTIONS: list[Direction] = ["^", "v", "<", ">"]


def move(i: int, j: int, d: Direction) -> tuple[int, int]:
    match d:
        case "^":
            return (i - 1, j)
        case ">":
            return (i, j + 1)
        case "v":
            return (i + 1, j)
        case "<":
            return (i, j - 1)


def turn_right(d: Direction) -> Direction:
    match d:
        case "^":
            return ">"
        case ">":
            return "v"
        case "v":
            return "<"
        case "<":
            return "^"


def turn_left(d: Direction) -> Direction:
    match d:
        case "^":
            return "<"
        case "<":
            return "v"
        case "v":
            return ">"
        case ">":
            return "^"


class State(NamedTuple):
    i: int
    j: int
    direction: Direction
    concecutive_direct_moves: int
    can_stop: bool


def find_crucible_path(
    inp: str,
    debug: bool,
    max_concecutive_direct_moves: int,
    min_concecutive_direct_moves: int,
):
    city_block_losses = parse_input(inp)
    height = len(city_block_losses)
    width = len(city_block_losses[0])

    initial_states = [
        State(
            i=0,
            j=0,
            direction=direction,
            concecutive_direct_moves=0,
            can_stop=0 >= min_concecutive_direct_moves,
        )
        for direction in DIRECTIONS
    ]
    heat_loss: dict[State, int] = {s: 0 for s in initial_states}
    next_state_queue: list[tuple[int, State]] = [(0, state) for state in initial_states]
    heapq.heapify(next_state_queue)
    visited: set[State] = set()
    previous: dict[State, State] = dict()
    final_state: Optional[State] = None
    while next_state_queue:
        current_loss, current = heapq.heappop(next_state_queue)
        visited.add(current)
        if current.i == height - 1 and current.j == width - 1 and current.can_stop:
            print(current_loss)
            final_state = current
            break

        next_directions: list[Direction] = []
        if current.concecutive_direct_moves >= min_concecutive_direct_moves:
            next_directions.append(turn_right(current.direction))
            next_directions.append(turn_left(current.direction))
        if current.concecutive_direct_moves < max_concecutive_direct_moves:
            next_directions.append(current.direction)
        for next_direction in next_directions:
            next_concecutive_moves = (
                0 if next_direction != current.direction else current.concecutive_direct_moves + 1
            )
            next = State(
                *move(current.i, current.j, next_direction),
                next_direction,
                concecutive_direct_moves=next_concecutive_moves,
                can_stop=next_concecutive_moves >= min_concecutive_direct_moves,
            )
            if (
                0 <= next.i < height
                and 0 <= next.j < width
                and next.concecutive_direct_moves < max_concecutive_direct_moves
                and next not in visited
            ):
                next_loss = current_loss + city_block_losses[next.i][next.j]
                next_loss_so_far = heat_loss.get(next)
                if next_loss_so_far is None or next_loss_so_far > next_loss:
                    heapq.heappush(next_state_queue, (next_loss, next))
                    heat_loss[next] = next_loss
                    previous[next] = current

    if debug:
        trace_map = [["."] * width for _ in range(height)]
        assert final_state
        trace_step = final_state
        while True:
            (i, j, dir_, *_) = trace_step
            trace_map[i][j] = dir_
            if i == 0 and j == 0:
                break
            trace_step = previous[trace_step]
        print(format_map(trace_map, cell_width=2))


def part_1(inp: str, debug: bool):
    find_crucible_path(
        inp,
        debug,
        max_concecutive_direct_moves=3,
        min_concecutive_direct_moves=0,
    )


def part_2(inp: str, debug: bool):
    find_crucible_path(
        inp,
        debug,
        max_concecutive_direct_moves=10,
        min_concecutive_direct_moves=3,
    )
