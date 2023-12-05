from dataclasses import dataclass
from itertools import chain
from typing import Optional


@dataclass
class Range:
    start: int
    length: int

    def overlap(self, other: "Range") -> tuple[Optional["Range"], list["Range"]]:
        """
        Find overlap range between the self and the other; also returns ranges that
        are left after subtracting the overlap from te original
        """
        overlap_left = max(self.start, other.start)
        overlap_right = min(self.start + self.length, other.start + other.length)
        if overlap_right < overlap_left:
            return None, [self]
        overlap = Range(start=overlap_left, length=overlap_right - overlap_left)
        rest: list[Range] = []
        if overlap.start > self.start:
            rest.append(Range(start=self.start, length=overlap.start - self.start))
        if overlap.start + overlap.length < self.start + self.length:
            rest.append(
                Range(
                    start=overlap.start + overlap.length,
                    length=self.length - overlap.length - overlap.start,
                )
            )
        return overlap, rest


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

    def apply_to_range(self, range: Range) -> list[Range]:
        unmapped = [range]
        mapped: list[Range] = []
        for range_map in self.range_maps:
            unmapped_still: list[Range] = []
            for subrange in unmapped:
                overlap, rest = subrange.overlap(range_map.source_range)
                unmapped_still.extend(rest)
                if overlap:
                    mapped.append(
                        Range(start=overlap.start + range_map.offset, length=overlap.length)
                    )
            unmapped = unmapped_still
        return mapped + unmapped


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
        ranges = list(chain.from_iterable(map.apply_to_range(range) for range in ranges))

    if debug:
        print(ranges)

    print(min(ranges, key=lambda r: r.start).start)
