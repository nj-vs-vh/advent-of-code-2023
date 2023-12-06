import functools
import math
import operator
from dataclasses import dataclass


@dataclass
class Record:
    time: int
    distance: int

    def ways_to_beat(self, debug: bool) -> int:
        D = self.time**2 - 4 * self.distance
        t_c_tie_min = (self.time - math.sqrt(D)) / 2
        t_c_tie_max = (self.time + math.sqrt(D)) / 2

        t_c_win_min = math.ceil(t_c_tie_min)
        if t_c_win_min == t_c_tie_min:
            t_c_win_min += 1

        t_c_win_max = math.floor(t_c_tie_max)
        if t_c_win_max == t_c_tie_max:
            t_c_win_max -= 1

        ways_to_beat = t_c_win_max - t_c_win_min + 1
        if debug:
            print(
                f"t_c to tie: {t_c_tie_min:.4f}, {t_c_tie_max:.4f}; "
                + f"t_c to win: [{t_c_win_min}, {t_c_win_max}]; "
                + f"ways to beat the record: {ways_to_beat}"
            )
        return ways_to_beat


def parse_input_pt1(inp: str) -> list[Record]:
    lines = inp.splitlines()
    times = [int(t) for t in lines[0].removeprefix("Time:").strip().split()]
    distances = [int(d) for d in lines[1].removeprefix("Distance:").strip().split()]
    return [Record(t, d) for t, d in zip(times, distances)]


def parse_input_pt2(inp: str) -> Record:
    lines = inp.splitlines()
    return Record(
        time=int(lines[0].removeprefix("Time:").replace(" ", "")),
        distance=int(lines[1].removeprefix("Distance:").replace(" ", "")),
    )


def part_1(inp: str, debug: bool):
    records = parse_input_pt1(inp)
    if debug:
        print(records)

    ways_to_beat_records: list[int] = []
    for record in records:
        ways_to_beat_records.append(record.ways_to_beat(debug))
    print(functools.reduce(operator.mul, ways_to_beat_records, 1))


def part_2(inp: str, debug: bool):
    record = parse_input_pt2(inp)
    print(record.ways_to_beat(debug))
