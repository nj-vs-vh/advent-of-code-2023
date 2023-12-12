from dataclasses import dataclass
from enum import Enum, auto


class Spring(Enum):
    OK = "."
    DMG = "#"
    UNK = "?"

    def __str__(self) -> str:
        return self.value

    __repr__ = __str__


@dataclass
class SpringRow:
    springs: list[Spring]
    damaged_group_sizes: list[int]

    @property
    def total_unknown(self) -> int:
        return sum(1 for s in self.springs if s is Spring.UNK)

    @property
    def unknown_damaged(self) -> int:
        return sum(self.damaged_group_sizes) - sum(1 for s in self.springs if s is Spring.DMG)

    @property
    def unknown_ok(self) -> int:
        return self.total_unknown - self.unknown_damaged

    def __str__(self) -> str:
        return (
            f"{''.join(str(spring) for spring in self.springs)} "
            + f"({','.join(str(size) for size in self.damaged_group_sizes)})"
        )

    @classmethod
    def parse(cls, line: str, unfold_factor: int = 1) -> "SpringRow":
        row, groups = line.split(" ")
        row = "?".join([row] * unfold_factor)
        groups = ",".join([groups] * unfold_factor)
        return SpringRow(
            springs=[Spring(ch) for ch in row],
            damaged_group_sizes=[int(g) for g in groups.split(",")],
        )


def arrangements(
    row: SpringRow,
    ok_unknown: int,
    unknown_indices_assumed_ok: list[int],
    debug: bool,
) -> int:
    assumed_range_end = (
        len(row.springs)  # the whole row
        if len(unknown_indices_assumed_ok) == ok_unknown
        else (
            unknown_indices_assumed_ok[-1] + 1  # past the last assumed idx
            if unknown_indices_assumed_ok
            else 0  # nothing
        )
    )
    # calculating damaged group sizes within the current assumed range
    assumed_damaged_group_sizes: list[int] = []
    current_group_size = 0
    for idx, s in enumerate(row.springs[:assumed_range_end]):
        if s is Spring.OK or (s is Spring.UNK and idx in unknown_indices_assumed_ok):
            if current_group_size:
                assumed_damaged_group_sizes.append(current_group_size)
                current_group_size = 0
        else:
            current_group_size += 1
    if current_group_size:
        assumed_damaged_group_sizes.append(current_group_size)

    # if there are contradictions in the assumed range, there is no need to process the rest of the tree
    if any(
        assumed_group_size != group_size
        for assumed_group_size, group_size in zip(
            assumed_damaged_group_sizes, row.damaged_group_sizes
        )
    ):
        if debug:
            print(f"\tpruning ({unknown_indices_assumed_ok = }, {assumed_damaged_group_sizes = })")
        return 0

    # recursion terminal condition = assumed all ok indices we had
    if len(assumed_damaged_group_sizes) == len(row.damaged_group_sizes):
        if debug:
            print(f"\t\tterminal condition reached, unk-i-ok = {unknown_indices_assumed_ok}")
        return 1

    subarrangements = 0
    for idx in range(assumed_range_end, len(row.springs)):
        if row.springs[idx] is not Spring.UNK:
            continue
        subarrangements += arrangements(
            row,
            ok_unknown,
            unknown_indices_assumed_ok=[*unknown_indices_assumed_ok, idx],
            debug=debug,
        )
    return subarrangements


def part_1(inp: str, debug: bool):
    answer = 0
    for line in inp.splitlines():
        row = SpringRow.parse(line)
        if debug:
            print()
            print(row.damaged_group_sizes)
            char_len = len(str(len(row.springs) - 1))
            fmt_char = lambda x: str(x).center(char_len, " ")
            print(" ".join(fmt_char(spring) for spring in row.springs))
            print(" ".join(fmt_char(i) for i in range(len(row.springs))))
        if row.unknown_damaged == 0:
            answer += 1
            continue
        row_arrangments = arrangements(
            row,
            ok_unknown=row.unknown_ok,
            unknown_indices_assumed_ok=[],
            debug=debug,
        )
        if debug:
            print("Result:", row_arrangments)
        answer += row_arrangments
    print(answer)


def part_2(inp: str, debug: bool):
    answer = 0
    for line in inp.splitlines():
        row = SpringRow.parse(line, unfold_factor=5)
        if row.unknown_damaged == 0:
            answer += 1
            continue
        answer += arrangements(
            row,
            ok_unknown=row.unknown_ok,
            unknown_indices_assumed_ok=[],
            debug=debug,
        )
    print(answer)
