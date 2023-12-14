from dataclasses import dataclass
from typing import Generic, Iterable, TypeVar

T = TypeVar("T")


@dataclass
class Array2D(Generic[T]):
    values: list[T]
    width: int
    height: int

    def __post_init__(self):
        # 4 x (width*height) array, stores linear indices for each rotation
        self.rotated_linear_indices = []
        for rot_cw in range(4):
            rotated_linear_indices = []
            for i, j, _ in self.iter_values():
                width, height = self.width, self.height
                for _ in range(rot_cw % 4):
                    i, j = width - j - 1, i
                    width, height = height, width
                rotated_linear_indices.append(i * width + j)
            self.rotated_linear_indices.append(rotated_linear_indices)

    def iter_values(self) -> Iterable[tuple[int, int, T]]:
        i, j = 0, 0
        for value in self.values:
            yield i, j, value
            j += 1
            if j == self.width:
                i += 1
                j = 0

    def _linear_idx(self, i: int, j: int, rot_cw: int) -> int:
        return self.rotated_linear_indices[rot_cw][i * self.width + j]

    def get(self, i: int, j: int, rot_cw: int) -> T:
        return self.values[self._linear_idx(i, j, rot_cw)]

    def set(self, i: int, j: int, rot_cw: int, value: T) -> None:
        self.values[self._linear_idx(i, j, rot_cw)] = value


@dataclass
class State:
    static: Array2D[bool]
    rolling: Array2D[bool]

    def rolling_rocks_hash(self) -> int:
        return hash(tuple(self.rolling.values))

    def __str__(self) -> str:
        lines: list[str] = []
        for i in range(self.static.height):
            chars: list[str] = []
            for j in range(self.static.width):
                if self.static.get(i, j, 0):
                    chars.append("#")
                elif self.rolling.get(i, j, 0):
                    chars.append("O")
                else:
                    chars.append(".")
            lines.append("".join(chars))
        return "\n".join(lines)

    def tilt(self, rot_cw: int) -> None:
        for j in range(self.static.width):
            stop_i = -1
            rolled_count = 0
            for i in range(self.static.height + 1):
                if i == self.static.height or self.static.get(i, j, rot_cw):
                    if rolled_count:
                        for i_rolled in range(stop_i + 1, stop_i + rolled_count + 1):
                            self.rolling.set(i_rolled, j, rot_cw, True)
                        rolled_count = 0
                    stop_i = i
                elif self.rolling.get(i, j, rot_cw):
                    rolled_count += 1
                    self.rolling.set(i, j, rot_cw, False)

    def north_support_load(self) -> int:
        result = 0
        for i, _, has_rolling_rock in self.rolling.iter_values():
            if has_rolling_rock:
                result += self.rolling.height - i
        return result


def parse_initial_state(inp: str) -> State:
    lines = inp.splitlines()
    width = len(lines[0])
    height = len(lines)
    static = Array2D([False] * width * height, width, height)
    rolling = Array2D([False] * width * height, width, height)

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            match char:
                case "#":
                    static.set(i, j, 0, True)
                case "O":
                    rolling.set(i, j, 0, True)
    return State(static, rolling)


def part_1(inp: str, debug: bool):
    state = parse_initial_state(inp)
    state.tilt(0)
    if debug:
        print(state)
    print(state.north_support_load())


def part_2(inp: str, debug: bool):
    state = parse_initial_state(inp)
    load_history: list[int] = []
    state_history: dict[int, int] = {}
    total_cycles = 1_000_000_000
    for cycle_idx in range(1, total_cycles + 1):
        for rot in range(4):
            state.tilt(rot)
        if debug:
            print(state)
            print()

        if loop_start_cycle_idx := state_history.get(state.rolling_rocks_hash()):
            print(f"Found loop {loop_start_cycle_idx} - {cycle_idx}!")
            loop_length = cycle_idx - loop_start_cycle_idx
            phase = (total_cycles - loop_start_cycle_idx) % loop_length
            print(load_history[loop_start_cycle_idx + phase - 1])
            break
        else:
            state_history[state.rolling_rocks_hash()] = cycle_idx
            load_history.append(state.north_support_load())
