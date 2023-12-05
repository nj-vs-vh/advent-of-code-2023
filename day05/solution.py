from dataclasses import dataclass
from itertools import chain
from typing import Optional


@dataclass
class Range:
    start: int
    length: int

    @property
    def end(self) -> int:
        return self.start + self.length

    def __repr__(self) -> str:
        return f"Range [{self.start / 1e9 :.4f}, {(self.end) / 1e9 :.4f})"

    def overlap(
        self, other: "Range"
    ) -> tuple[Optional["Range"], Optional["Range"], Optional["Range"]]:
        """
        Find overlap range between the self and the other; also returns subranges of self
        that lie to the left and to the right of the overlap
        """
        left: Optional[Range] = None
        right: Optional[Range] = None
        overlap_start = max(self.start, other.start)
        overlap_end = min(self.end, other.end)
        if overlap_end <= overlap_start:
            if self.start < other.start:
                left = self
            else:
                right = self
            return left, None, right
        overlap = Range(start=overlap_start, length=overlap_end - overlap_start)
        if overlap.start > self.start:
            left = Range(start=self.start, length=overlap.start - self.start)
        if overlap.end < self.end:
            right = Range(
                start=overlap.end,
                length=self.end - overlap.end,
            )
        return left, overlap, right


@dataclass
class RangeMap:
    length: int
    source_start: int
    target_start: int

    @property
    def source_range(self) -> Range:
        return Range(start=self.source_start, length=self.length)

    @property
    def offset(self) -> int:
        return self.target_start - self.source_start


@dataclass
class Map:
    name: str
    range_maps: list[RangeMap]

    def apply(self, num: int) -> int:
        for range_map in self.range_maps:
            if range_map.source_start <= num < range_map.source_start + range_map.length:
                return num + range_map.offset
        return num

    def apply_to_range(self, range: Range) -> list[tuple[Range, bool]]:
        subranges: list[tuple[Range, bool]] = [(range, False)]  # range, already mapped flag
        for range_map in self.range_maps:
            subranges_new: list[tuple[Range, bool]] = []
            for subrange, is_mapped in subranges:
                if is_mapped:
                    subranges_new.append((subrange, True))
                    continue
                left, overlap, right = subrange.overlap(range_map.source_range)
                if left:
                    subranges_new.append((left, False))
                if overlap:
                    subranges_new.append(
                        (
                            Range(start=overlap.start + range_map.offset, length=overlap.length),
                            True,
                        )
                    )
                if right:
                    subranges_new.append((right, False))
            subranges = subranges_new
        return subranges


def parse_seeds(inp: str) -> list[int]:
    return [int(s) for s in inp.split("\n", 1)[0].strip().removeprefix("seeds: ").split()]


def parse_seed_ranges(inp: str) -> list[Range]:
    numbers = parse_seeds(inp)
    return [
        Range(start=start, length=length)
        for start, length in zip(
            numbers[0::2],
            numbers[1::2],
        )
    ]


def parse_maps(inp: str) -> list[Map]:
    paragraphs = inp.split("\n\n")
    maps: list[Map] = []
    for p in paragraphs[1:]:
        lines = p.splitlines()
        map = Map(name=lines[0].strip().removesuffix(" map:"), range_maps=[])
        for line in lines[1:]:
            target, source, len_ = line.strip().split()
            map.range_maps.append(
                RangeMap(length=int(len_), source_start=int(source), target_start=int(target))
            )
        maps.append(map)
    return maps


def part_1(inp: str, debug: bool):
    seeds = parse_seeds(inp)
    maps = parse_maps(inp)
    if debug:
        print(seeds)
        print(*maps, sep="\n")

    final_targets: list[int] = []
    for seed in seeds:
        value = seed
        for map in maps:
            source_value = value
            value = map.apply(value)
            if debug:
                print(map.name, source_value, "->", value)
        final_targets.append(value)

    if debug:
        print(final_targets)
    print(min(final_targets))


def part_2(inp: str, debug: bool):
    seed_ranges = parse_seed_ranges(inp)
    maps = parse_maps(inp)
    if debug:
        print(seed_ranges)

    ranges = seed_ranges
    for map in maps:
        mapped_subranges = list(chain.from_iterable(map.apply_to_range(range) for range in ranges))
        ranges = [r for r, _ in mapped_subranges]

    if debug:
        print(ranges)

    print(min(ranges, key=lambda r: r.start).start)
