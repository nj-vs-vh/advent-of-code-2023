import collections
import dataclasses
import functools
import itertools
import re
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Range:
    start: int
    end: int

    def __str__(self) -> str:
        return f"[{self.start}, {self.end})"

    def overlap(self, other: "Range") -> "Range | None":
        start = max(self.start, other.start)
        end = min(self.end, other.end)
        return Range(start, end) if end > start else None


@dataclass
class Block:
    id_: str
    x: Range
    y: Range
    z: Range

    supporting_blocks: list["Block"] = dataclasses.field(default_factory=list)
    supported_blocks: list["Block"] = dataclasses.field(default_factory=list)

    def __hash__(self) -> int:
        return hash(self.id_)

    def __str__(self) -> str:
        return (
            f"Block({self.id_}, x: {self.x}, y: {self.y}, z: {self.z}, "
            + f"supports {[b.id_ for b in self.supported_blocks]}, "
            + f"supported by {[b.id_ for b in self.supporting_blocks]}"
        )

    __repr__ = __str__

    BLOCK_RE: ClassVar = re.compile(r"(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)")

    @classmethod
    def parse(cls, line: str, id_: str) -> "Block":
        m = cls.BLOCK_RE.match(line)
        assert m is not None, repr(line)
        return Block(
            id_=id_,
            x=Range(
                start=int(m.group(1)),
                end=int(m.group(4)) + 1,
            ),
            y=Range(
                start=int(m.group(2)),
                end=int(m.group(5)) + 1,
            ),
            z=Range(
                start=int(m.group(3)),
                end=int(m.group(6)) + 1,
            ),
        )

    @functools.cache
    def causes_to_fall(self) -> set["Block"]:
        if not self.supporting_blocks:
            return set()
        else:
            causes_to_fall: set[Block] | None = None
            # everything that will cause all support to fall
            for supporting in self.supporting_blocks:
                if causes_to_fall is None:
                    causes_to_fall = supporting.causes_to_fall().copy()
                else:
                    causes_to_fall.intersection_update(supporting.causes_to_fall())
                    if not causes_to_fall:
                        break
            assert causes_to_fall is not None
            # if single-support -- it's collapse will also be a cause to fall, so add it
            if len(self.supporting_blocks) == 1:
                causes_to_fall.add(self.supporting_blocks[0])
            return causes_to_fall


def fall(blocks: list[Block]) -> None:
    blocks.sort(key=lambda block: block.z.start)
    for i, falling in enumerate(blocks):
        potential_supports = [
            block
            for block in blocks[:i]
            if block.z.end <= falling.z.start and falling.x.overlap(block.x) and falling.y.overlap(block.y)
        ]
        new_z_start = max(b.z.end for b in potential_supports) if potential_supports else 1
        fall_distance = falling.z.start - new_z_start
        falling.z.start -= fall_distance
        falling.z.end -= fall_distance
        falling.supporting_blocks = [b for b in potential_supports if b.z.end == new_z_start]
        for b in falling.supporting_blocks:
            b.supported_blocks.append(falling)


def part_1(inp: str, debug: bool):
    blocks = [Block.parse(line, str(i)) for i, line in enumerate(inp.splitlines())]
    if debug:
        for b in blocks:
            print(b)

    fall(blocks)

    if debug:
        print("after falling")
        for b in blocks:
            print(b)

    print(
        sum(
            1
            for block in blocks
            if not block.supported_blocks
            or all(len(supported.supporting_blocks) > 1 for supported in block.supported_blocks)
        )
    )


def part_2(inp: str, debug: bool):
    blocks = [Block.parse(line, str(i)) for i, line in enumerate(inp.splitlines())]
    fall(blocks)
    caused_to_fall_by: dict[Block, int] = collections.defaultdict(lambda: 0)
    for block in blocks:
        if debug:
            print(block.id_, "->", [b.id_ for b in block.causes_to_fall()])
        for cause in block.causes_to_fall():
            caused_to_fall_by[cause] += 1
    print(sum(caused_to_fall_by.values()))
