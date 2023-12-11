import itertools
from dataclasses import dataclass


@dataclass(frozen=True)
class Coords:
    i: int
    j: int


def parse_galaxies(inp: str) -> list[Coords]:
    res: list[Coords] = []
    for i, line in enumerate(inp.splitlines()):
        for j, char in enumerate(line):
            if char == "#":
                res.append(Coords(i, j))
    return res


def expansion_mask(galaxy_coords: set[int], expansion_factor: int) -> list[int]:
    res: list[int] = []
    for galaxy_1, galaxy_2 in itertools.pairwise(sorted(galaxy_coords)):
        res.append(1)  # for galaxy 1
        expansion_start = galaxy_1 + 1
        if galaxy_2 > expansion_start:
            res.extend([expansion_factor] * (galaxy_2 - expansion_start))
    res.append(1)  # the last galaxy
    # we never go past last galaxy => no need to calculate the expansion
    return res


def sum_expanded_distances(galaxies: list[Coords], expansion_factor: int, debug: bool) -> int:
    expansion_mask_i = expansion_mask({g.i for g in galaxies}, expansion_factor)
    expansion_mask_j = expansion_mask({g.j for g in galaxies}, expansion_factor)
    if debug:
        print(f"{expansion_mask_i = }")
        print(f"{expansion_mask_j = }")

    distance_sum = 0
    for idx_start, start in enumerate(galaxies[:-1]):
        for delta_idx, end in enumerate(galaxies[idx_start + 1 :]):
            if debug:
                idx_end = idx_start + delta_idx + 1
                print(f"calculating distance #{idx_start + 1} {start} -> #{idx_end + 1} {end}")

            i_min, i_max = start.i, end.i
            if i_min > i_max:
                i_min, i_max = i_max, i_min
            expanded_i = sum(expansion_mask_i[i_min:i_max])

            j_min, j_max = start.j, end.j
            if j_min > j_max:
                j_min, j_max = j_max, j_min
            expanded_j = sum(expansion_mask_j[j_min:j_max])
            if debug:
                print(f"\tdi = {expanded_i}, dj = {expanded_j}, total = {expanded_i + expanded_j}")

            # manhattan metric
            distance_sum += expanded_i + expanded_j

    return distance_sum


def part_1(inp: str, debug: bool):
    galaxies = parse_galaxies(inp)
    if debug:
        print("input:\n", inp, "\n\n")
        print("comoving galaxy coords = ", *galaxies, sep="\n\t")
        print()

        debug_expansion_factor = 3
        expansion_mask_i = expansion_mask(
            {g.i for g in galaxies}, expansion_factor=debug_expansion_factor
        )
        expansion_mask_j = expansion_mask(
            {g.j for g in galaxies}, expansion_factor=debug_expansion_factor
        )
        print(f"{expansion_mask_i = }")
        print(f"{expansion_mask_j = }")

        # printing expanded map
        galaxy_set = set(galaxies)
        height = max(g.i for g in galaxies) + 1
        width = max(g.j for g in galaxies) + 1
        expanded_map: list[list[str]] = []
        galaxy_idx = 1
        for i in range(height):
            if i < len(expansion_mask_i) - 1 and expansion_mask_i[i] > 1:
                expanded_map.extend([[] for _ in range(debug_expansion_factor)])
            else:
                line = []
                for j in range(width):
                    if Coords(i, j) in galaxy_set:
                        line.append(str(galaxy_idx))
                        galaxy_idx += 1
                    else:
                        if j < len(expansion_mask_j) - 1 and expansion_mask_j[j] > 1:
                            line.extend(["|"] * debug_expansion_factor)
                        else:
                            line.append(".")
                expanded_map.append(line)
        expanded_width = len(next(l for l in expanded_map if l))
        expanded_map = [l or ["-" for _ in range(expanded_width)] for l in expanded_map]
        for row in expanded_map:
            print("".join(row))

    print(
        sum_expanded_distances(
            galaxies,
            expansion_factor=2,
            debug=debug,
        )
    )


def part_2(inp: str, debug: bool):
    print(
        sum_expanded_distances(
            galaxies=parse_galaxies(inp),
            expansion_factor=1000000,
            debug=False,
        )
    )
