import heapq
from typing import Literal, Optional

from utils import format_map


def parse_input(inp: str) -> list[list[int]]:
    return [[int(char) for char in line] for line in inp.splitlines()]


Direction = Literal["^", "v", "<", ">"]
DIRECTIONS: list[Direction] = ["^", "v", "<", ">"]
LEFT_TURN: dict[Direction, Direction] = {
    "^": "<",
    "<": "v",
    "v": ">",
    ">": "^",
}
RIGHT_TURN: dict[Direction, Direction] = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}
DELTA_I: dict[Direction, int] = {
    "^": -1,
    ">": 0,
    "v": 1,
    "<": 0,
}
DELTA_J: dict[Direction, int] = {
    "^": 0,
    ">": 1,
    "v": 0,
    "<": -1,
}


#                     i  | j  | dir     |streak|can stop?
DijkstraState = tuple[int, int, Direction, int, bool]


def find_crucible_path(
    inp: str,
    debug: bool,
    max_concecutive_direct_moves: int,
    min_concecutive_direct_moves: int,
):
    city_block_losses = parse_input(inp)
    height = len(city_block_losses)
    width = len(city_block_losses[0])

    initial_states: list[DijkstraState] = [
        (
            0,
            0,
            direction,
            0,
            0 >= min_concecutive_direct_moves,
        )
        for direction in DIRECTIONS
    ]
    heat_loss: dict[DijkstraState, int] = {s: 0 for s in initial_states}
    state_queue: list[tuple[int, DijkstraState]] = [(0, state) for state in initial_states]
    heapq.heapify(state_queue)
    visited: set[DijkstraState] = set()
    previous: dict[DijkstraState, DijkstraState] = dict()
    final_state: Optional[DijkstraState] = None
    while True:  # no need to check queue is full, we expect to break before it's empty
        current_loss, current = heapq.heappop(state_queue)
        visited.add(current)
        (
            current_i,
            current_j,
            current_direction,
            current_concecutive_direct_moves,
            current_can_stop,
        ) = current
        if current_i == height - 1 and current_j == width - 1 and current_can_stop:
            print(current_loss)
            final_state = current
            break

        next_directions: list[Direction] = []
        if current_concecutive_direct_moves >= min_concecutive_direct_moves:
            next_directions.append(RIGHT_TURN[current_direction])
            next_directions.append(LEFT_TURN[current_direction])
        if current_concecutive_direct_moves < max_concecutive_direct_moves:
            next_directions.append(current_direction)
        for next_direction in next_directions:
            next_concecutive_moves = (
                0 if next_direction != current_direction else current_concecutive_direct_moves + 1
            )
            next = (
                current_i + DELTA_I[current_direction],
                current_j + DELTA_J[current_direction],
                next_direction,
                next_concecutive_moves,
                next_concecutive_moves >= min_concecutive_direct_moves,
            )
            if (
                0 <= next[0] < height
                and 0 <= next[1] < width
                and next[3] < max_concecutive_direct_moves
                and next not in visited
            ):
                next_loss = current_loss + city_block_losses[next[0]][next[1]]
                next_loss_so_far = heat_loss.get(next)
                if next_loss_so_far is None or next_loss_so_far > next_loss:
                    heapq.heappush(state_queue, (next_loss, next))
                    heat_loss[next] = next_loss
                    if debug:
                        previous[next] = current

    if debug:
        trace_map = [["."] * width for _ in range(height)]
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
