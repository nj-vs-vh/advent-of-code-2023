import itertools
from dataclasses import dataclass


@dataclass(frozen=True)
class Coords:
    i: int
    j: int


@dataclass(frozen=True)
class Range:
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

    def __repr__(self) -> str:
        return f"Range[{self.start}, {(self.end)})"


def parse_galaxies(inp: str) -> list[Coords]:
    res: list[Coords] = []
    for i, line in enumerate(inp.splitlines()):
        for j, char in enumerate(line):
            if char == "#":
                res.append(Coords(i, j))
    return res


def expansion_mask(galaxy_coords: set[int]) -> list[bool]:
    res: list[bool] = []
    for galaxy_1, galaxy_2 in itertools.pairwise(sorted(galaxy_coords)):
        res.append(False)  # for galaxy 1
        expansion_start = galaxy_1 + 1
        if galaxy_2 > expansion_start:
            res.extend([True] * (galaxy_2 - expansion_start))
    # after the last galaxy we don't need to calculate the expansion
    return res


def expanded_distance(
    comoving_distance: Range,
    expansion_mask: list[bool],
    expansion_factor: int,
) -> int:
    return sum(
        expansion_factor if is_expanded else 1
        for is_expanded in expansion_mask[comoving_distance.start : comoving_distance.end]
    )


def sum_expanded_distances(galaxies: list[Coords], expansion_factor: int, debug: bool) -> int:
    expansion_mask_i = expansion_mask({g.i for g in galaxies})
    expansion_mask_j = expansion_mask({g.j for g in galaxies})
    if debug:
        print(f"{expansion_mask_i = }")
        print(f"{expansion_mask_j = }")

    distance_sum = 0
    for idx_start, start in enumerate(galaxies[:-1]):
        for delta_idx, end in enumerate(galaxies[idx_start + 1 :]):
            idx_end = idx_start + delta_idx + 1
            if debug:
                print(f"calculating distance #{idx_start + 1} {start} -> #{idx_end + 1} {end}")
            distance_i = expanded_distance(
                comoving_distance=Range.from_edges(start.i, end.i),
                expansion_mask=expansion_mask_i,
                expansion_factor=expansion_factor,
            )
            distance_j = expanded_distance(
                comoving_distance=Range.from_edges(start.j, end.j),
                expansion_mask=expansion_mask_j,
                expansion_factor=expansion_factor,
            )
            if debug:
                print(f"\tdi = {distance_i}, dj = {distance_j}, total = {distance_i + distance_j}")

            # manhattan metric
            distance_sum += distance_i + distance_j

    return distance_sum


def part_1(inp: str, debug: bool):
    galaxies = parse_galaxies(inp)
    if debug:
        print("input:\n", inp, "\n\n")
        print("comoving galaxy coords = ", *galaxies, sep="\n\t")
        print()
        expansion_mask_i = expansion_mask({g.i for g in galaxies})
        expansion_mask_j = expansion_mask({g.j for g in galaxies})
        print(f"{expansion_mask_i = }")
        print(f"{expansion_mask_j = }")

        # printing expanded map
        debug_expansion_factor = 3
        galaxy_set = set(galaxies)
        height = max(g.i for g in galaxies) + 1
        width = max(g.j for g in galaxies) + 1
        expanded_map: list[list[str]] = []
        galaxy_idx = 1
        for i in range(height):
            if i < len(expansion_mask_i) - 1 and expansion_mask_i[i]:
                expanded_map.extend([[] for _ in range(debug_expansion_factor)])
            else:
                line = []
                for j in range(width):
                    if Coords(i, j) in galaxy_set:
                        line.append(str(galaxy_idx))
                        galaxy_idx += 1
                    else:
                        if j < len(expansion_mask_j) - 1 and expansion_mask_j[j]:
                            line.extend(["|"] * debug_expansion_factor)
                        else:
                            line.append(".")
                expanded_map.append(line)
        expanded_width = len(next(l for l in expanded_map if l))
        expanded_map = [l or ["-" for _ in range(expanded_width)] for l in expanded_map]
        for row in expanded_map:
            print("".join(row))

    print(sum_expanded_distances(galaxies, expansion_factor=2, debug=debug))


def part_2(inp: str, debug: bool):
    print(
        sum_expanded_distances(
            galaxies=parse_galaxies(inp),
            expansion_factor=1000000,
            debug=False,
        )
    )
