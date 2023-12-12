import functools
from dataclasses import dataclass

# turns out python Enums introduce waaaaay too much overhead when hashing,
# which is crucial for memoization performance here
SPRING_OK = "."
SPRING_DMG = "#"
SPRING_UNK = "?"


@dataclass(frozen=True)
class SpringRow:
    # used to be tuple[Spring, ...], but string hashing turns out to be slightly faster
    springs: str
    dmg_group_sizes: tuple[int, ...]

    def __str__(self) -> str:
        return (
            f"{''.join(str(spring) for spring in self.springs)} "
            + f"({','.join(str(size) for size in self.dmg_group_sizes)})"
        )

    @classmethod
    def parse(cls, line: str, unfold_factor: int = 1) -> "SpringRow":
        row, groups = line.split(" ")
        row = "?".join([row] * unfold_factor)
        groups = ",".join([groups] * unfold_factor)
        return SpringRow(
            springs=row,
            dmg_group_sizes=tuple(int(g) for g in groups.split(",")),
        )


@functools.lru_cache(maxsize=1_000_000)
def arrangements(row: SpringRow) -> int:
    if not row.dmg_group_sizes:
        is_valid = not any(spring is SPRING_DMG for spring in row.springs)
        return int(is_valid)

    group_size = row.dmg_group_sizes[0]
    start = next((i for i, spring in enumerate(row.springs) if spring is not SPRING_OK), None)
    if start is None:
        is_valid = not bool(row.dmg_group_sizes)
        return int(is_valid)

    if len(row.springs) < start + sum(row.dmg_group_sizes) + len(row.dmg_group_sizes) - 1:
        return 0

    total = 0

    # branch with the first unknown field being OK
    if row.springs[start] is SPRING_UNK:
        total += arrangements(
            SpringRow(
                springs=row.springs[start + 1 :],
                dmg_group_sizes=row.dmg_group_sizes,
            ),
        )

    # branch with the first unknown field being damaged
    if all(spring is not SPRING_OK for spring in row.springs[start : start + group_size]) and (
        (start + group_size == len(row.springs))
        or (row.springs[start + group_size] is not SPRING_DMG)
    ):
        total += arrangements(
            row=SpringRow(
                springs=row.springs[start + group_size + 1 :],
                dmg_group_sizes=row.dmg_group_sizes[1:],
            ),
        )

    return total


def part_1(inp: str, debug: bool):
    arrangements.cache_clear()
    total = 0
    for line in inp.splitlines():
        row = SpringRow.parse(line)
        if debug:
            print(row)
        row_arrangements = arrangements(row)
        if debug:
            print("Result:", row_arrangements)
        total += row_arrangements
    print(total)


def part_2(inp: str, debug: bool):
    arrangements.cache_clear()
    total = 0
    for line in inp.splitlines():
        row = SpringRow.parse(line, unfold_factor=5)
        total += arrangements(row)
    print(total)
