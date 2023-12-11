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


def expanded_length(galaxy_coords: set[int], expansion_factor: int) -> list[int]:
    res: list[int] = []
    for galaxy_1, galaxy_2 in itertools.pairwise(sorted(galaxy_coords)):
        res.append(1)  # for galaxy 1
        expansion_start = galaxy_1 + 1
        if galaxy_2 > expansion_start:
            res.extend([expansion_factor] * (galaxy_2 - expansion_start))
    res.append(1)  # the last galaxy
    # we never go past last galaxy => no need to calculate the expansion
    return res


def cumsum(values: list[int]) -> list[int]:
    sum_ = 0
    res: list[int] = []
    for v in values:
        sum_ += v
        res.append(sum_)
    return res


def sum_expanded_distances(galaxies: list[Coords], expansion_factor: int, debug: bool) -> int:
    expanded_length_i = expanded_length({g.i for g in galaxies}, expansion_factor)
    expanded_length_j = expanded_length({g.j for g in galaxies}, expansion_factor)
    if debug:
        print(f"{expanded_length_i = }")
        print(f"{expanded_length_j = }")

    # got the idea from https://www.reddit.com/r/adventofcode/comments/18fmrjk/comment/kcv9xcz/
    cumsum_i = cumsum(expanded_length_i)
    cumsum_j = cumsum(expanded_length_j)

    distance_sum = 0
    for idx_start, start in enumerate(galaxies[:-1]):
        for delta_idx, end in enumerate(galaxies[idx_start + 1 :]):
            if debug:
                idx_end = idx_start + delta_idx + 1
                print(f"calculating distance #{idx_start + 1} {start} -> #{idx_end + 1} {end}")

            i_min, i_max = start.i, end.i
            if i_min > i_max:
                i_min, i_max = i_max, i_min
            delta_i = cumsum_i[i_max] - cumsum_i[i_min]

            j_min, j_max = start.j, end.j
            if j_min > j_max:
                j_min, j_max = j_max, j_min
            delta_j = cumsum_j[j_max] - cumsum_j[j_min]
            if debug:
                print(f"\tdi = {delta_i}, dj = {delta_j}, total = {delta_i + delta_j}")

            # manhattan metric
            distance_sum += delta_i + delta_j

    return distance_sum


def part_1(inp: str, debug: bool):
    galaxies = parse_galaxies(inp)
    if debug:
        print("input:\n", inp, "\n\n")
        print("comoving galaxy coords = ", *galaxies, sep="\n\t")
        print()

        debug_expansion_factor = 3
        expansion_length_i = expanded_length(
            {g.i for g in galaxies}, expansion_factor=debug_expansion_factor
        )
        expansion_length_j = expanded_length(
            {g.j for g in galaxies}, expansion_factor=debug_expansion_factor
        )
        print(f"{expansion_length_i = }")
        print(f"{expansion_length_j = }")

        # printing expanded map
        galaxy_set = set(galaxies)
        height = max(g.i for g in galaxies) + 1
        width = max(g.j for g in galaxies) + 1
        expanded_map: list[list[str]] = []
        galaxy_idx = 1
        for i in range(height):
            if i < len(expansion_length_i) - 1 and expansion_length_i[i] > 1:
                expanded_map.extend([[] for _ in range(debug_expansion_factor)])
            else:
                line = []
                for j in range(width):
                    if Coords(i, j) in galaxy_set:
                        line.append(str(galaxy_idx))
                        galaxy_idx += 1
                    else:
                        if j < len(expansion_length_j) - 1 and expansion_length_j[j] > 1:
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
