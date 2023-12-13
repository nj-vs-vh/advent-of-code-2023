import random
from typing import Literal, Optional

MapCell = Literal[".", "#"]
ASH: MapCell = "."
ROCK: MapCell = "#"

Map = list[list[MapCell]]


def format_bin(num: int, length: int) -> str:
    return bin(num)[2:].rjust(length, "0")


def format_map(map: Map) -> str:
    return "\n".join("".join(row) for row in map)


def low_bits(num: int, count: int) -> int:
    return num & ((1 << count) - 1)


def high_bits(num: int, full_length: int, count: int) -> int:
    if full_length < count:
        return num
    else:
        return num >> (full_length - count)


def find_mirror_points(row: tuple[MapCell, ...]) -> tuple[set[int], set[int]]:
    length = len(row)
    bit_chars = ["1" if c is ROCK else "0" for c in row]
    normal = int("".join(bit_chars), base=2)
    reflected = int("".join(reversed(bit_chars)), base=2)

    abs_max_offset = length - 2
    mirror_points: set[int] = set()
    mirror_points_with_smudge: set[int] = set()
    for offset in range(-abs_max_offset, abs_max_offset + 1, 2):
        overlap_length = length - abs(offset)
        mirror_point = (length + offset) // 2 - 1
        if offset < 0:
            normal_part = high_bits(normal, full_length=length, count=overlap_length)
            reflected_part = low_bits(reflected, count=overlap_length)
        else:
            normal_part = low_bits(normal, count=overlap_length)
            reflected_part = high_bits(reflected, full_length=length, count=overlap_length)

        match (normal_part ^ reflected_part).bit_count():
            case 0:  # zero bits difference = perfect reflection
                mirror_points.add(mirror_point)
            case 2:  # one smidge causes two-bit difference (one in normal and one in reflected parts)
                mirror_points_with_smudge.add(mirror_point)
    return mirror_points, mirror_points_with_smudge


def parse_maps(inp: str) -> list[Map]:
    maps: list[Map] = []
    for section in inp.split("\n\n"):
        map: Map = []
        for line in section.splitlines():
            map.append(list(line))  # type: ignore
        maps.append(map)
    return maps


def transposed(map: Map) -> Map:
    map_t: Map = []
    for row in map:
        if not map_t:
            map_t = [[c] for c in row]
        else:
            for transposed_col, cell in zip(map_t, row):
                transposed_col.append(cell)
    return map_t


def part_1(inp: str, debug: bool):
    maps = parse_maps(inp)
    result = 0
    for map in maps:
        if debug:
            print("\n\nprocessing map\n" + format_map(map))
        for factor, map_variant in zip((1, 100), (map, transposed(map))):
            if debug:
                print("\nmap variant\n" + format_map(map_variant))
            common_mirror_points: Optional[set[int]] = None
            for row in map_variant:
                mirror_points, _ = find_mirror_points(tuple(row))
                if common_mirror_points is None:
                    common_mirror_points = mirror_points
                else:
                    common_mirror_points.intersection_update(mirror_points)
                if not common_mirror_points:
                    break

            if common_mirror_points:
                if debug:
                    print("common mirror points: ", common_mirror_points)
                result += factor * (next(iter(common_mirror_points)) + 1)
                break
    print(result)


def part_2(inp: str, debug: bool):
    maps = parse_maps(inp)
    result = 0
    for map in maps:
        if debug:
            print("\n\nprocessing map\n" + format_map(map))
        for factor, map_variant in zip((1, 100), (map, transposed(map))):
            if debug:
                print("\nmap variant\n" + format_map(map_variant))
            row_mirror_points = [find_mirror_points(tuple(row)) for row in map_variant]
            found_smudged_mirror = False
            for smudged_row_idx in range(len(map_variant)):
                common_mirror_points: set[int] = set()
                for idx, (
                    mirror_points,
                    mirror_points_with_smudge,
                ) in enumerate(row_mirror_points):
                    mirror_points_ = (
                        mirror_points_with_smudge if idx == smudged_row_idx else mirror_points
                    )
                    if not common_mirror_points:
                        common_mirror_points = mirror_points_.copy()
                    else:
                        common_mirror_points.intersection_update(mirror_points_)
                    if not common_mirror_points:
                        break
                if common_mirror_points:
                    result += factor * (next(iter(common_mirror_points)) + 1)
                    found_smudged_mirror = True
                    break
            if found_smudged_mirror:
                break

    print(result)
