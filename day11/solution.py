import itertools
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Coords:
    i: int
    j: int


@dataclass(frozen=True)
class Range:
    """Copied with minimal modifications from day 5"""

    start: int
    length: int

    @classmethod
    def from_edges(cls, start: int, end: int) -> "Range":
        if start > end:
            # to make sure that start is included and end is excluded
            start, end = end + 1, start + 1
        return Range(start=start, length=end - start)

    @property
    def end(self) -> int:
        return self.start + self.length

    def contains(self, i: int) -> bool:
        return self.start <= i < self.end

    def __repr__(self) -> str:
        return f"Range[{self.start}, {(self.end)})"

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


def parse_galaxies(inp: str) -> list[Coords]:
    res: list[Coords] = []
    for i, line in enumerate(inp.splitlines()):
        for j, char in enumerate(line):
            if char == "#":
                res.append(Coords(i, j))
    return res


def calculate_expansion_ranges(galaxy_coords: set[int]) -> list[Range]:
    res: list[Range] = []
    for galaxy_1, galaxy_2 in itertools.pairwise(sorted(galaxy_coords)):
        range_start = galaxy_1 + 1
        if galaxy_2 > range_start:
            res.append(Range.from_edges(start=range_start, end=galaxy_2))
    return res


def expanded_distance(
    comoving_distance: Range, expansion_ranges: list[Range], expansion_factor: int, debug: bool
) -> int:
    if debug:
        print("... expanding distance")
    res = 0
    # expansion_ranges.sort(key=lambda r: r.start)
    comoving_range_left: Optional[Range] = comoving_distance
    for er in expansion_ranges:
        unexpanded, expanded, comoving_range_left = comoving_range_left.overlap(er)
        if debug:
            print("... er =", er, "unex", unexpanded, "exp", expanded, "left", comoving_range_left)
        if unexpanded is not None:
            res += unexpanded.length
        if expanded is not None:
            res += expansion_factor * expanded.length
        if comoving_range_left is None:
            break
    if comoving_range_left:
        res += comoving_range_left.length

    return res


def sum_expanded_distances(galaxies: list[Coords], expansion_factor: int, debug: bool) -> int:
    expansion_ranges_i = calculate_expansion_ranges({g.i for g in galaxies})
    expansion_ranges_j = calculate_expansion_ranges({g.j for g in galaxies})
    if debug:
        print(f"{expansion_ranges_i = }")
        print(f"{expansion_ranges_j = }")

    distance_sum = 0
    for idx_start, start in enumerate(galaxies[:-1]):
        for delta_idx, end in enumerate(galaxies[idx_start + 1 :]):
            idx_end = idx_start + delta_idx + 1
            if debug:
                print(f"calculating distance #{idx_start + 1} {start} -> #{idx_end + 1} {end}")
            distance_i = expanded_distance(
                comoving_distance=Range.from_edges(start.i, end.i),
                expansion_ranges=expansion_ranges_i,
                expansion_factor=expansion_factor,
                debug=debug,
            )
            distance_j = expanded_distance(
                comoving_distance=Range.from_edges(start.j, end.j),
                expansion_ranges=expansion_ranges_j,
                expansion_factor=expansion_factor,
                debug=debug,
            )
            if debug:
                print(f"\tdi = {distance_i}, dj = {distance_j}, total = {distance_i + distance_j}")

            # manhattan metric
            distance_sum += distance_i + distance_j

    return distance_sum


def part_1(inp: str, debug: bool):
    galaxies = parse_galaxies(inp)
    if debug:
        print(inp)
        print("galaxy coords = ", *galaxies, sep="\n\t")
        expansion_ranges_i = calculate_expansion_ranges({g.i for g in galaxies})
        expansion_ranges_j = calculate_expansion_ranges({g.j for g in galaxies})
        print(f"{expansion_ranges_i = }")
        print(f"{expansion_ranges_j = }")

        galaxy_set = set(galaxies)
        height = max(g.i for g in galaxies) + 1
        width = max(g.j for g in galaxies) + 1
        expanded_map: list[list[str]] = []
        galaxy_idx = 1
        for i in range(height):
            if any(er.contains(i) for er in expansion_ranges_i):
                expanded_map.extend([[], []])
            else:
                line = []
                for j in range(width):
                    if Coords(i, j) in galaxy_set:
                        line.append(str(galaxy_idx))
                        galaxy_idx += 1
                    else:
                        if any(er.contains(j) for er in expansion_ranges_j):
                            line.append("|")
                            line.append("|")
                        else:
                            line.append(".")
                expanded_map.append(line)
        expanded_width = len(next(l for l in expanded_map if l))
        expanded_map = [l or ["="] * expanded_width for l in expanded_map]
        for row in expanded_map:
            for char in row:
                print(char, end="")
            print()

    print(sum_expanded_distances(galaxies, expansion_factor=2, debug=debug))


def part_2(inp: str, debug: bool):
    galaxies = parse_galaxies(inp)
    print(sum_expanded_distances(galaxies, expansion_factor=1000000, debug=False))
