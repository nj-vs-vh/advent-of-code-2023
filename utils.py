from typing import Any, Callable, TypeVar, cast

T = TypeVar("T")

Map = list[list[T]]
Coords = tuple[int, int]


def parse_simple_map(inp: str, char_parser: Callable[[str], T] | None = None) -> Map[T]:
    res = [
        [
            char_parser(char)
            if char_parser
            else cast(T, char)  # NOTE: default to no validation here
            for char in line
        ]
        for line in inp.splitlines()
    ]
    assert len({len(row) for row in res}) == 1, "Non-rectangular map detected!"
    return res


def format_map(
    map: Map[T],
    formatter: Callable[[T], str] = lambda t: str(t) if t is not None else " ",
    cell_width: int | None = None,
    rulers_each: int | None = None,
) -> str:
    _, width = dimensions(map)
    # formatting
    str_map = [[formatter(cell) for cell in row] for row in map]
    # aligning all cells
    target_len = cell_width or max(max(len(s) for s in row) for row in str_map)
    str_map = [[s.center(target_len, " ") for s in row] for row in str_map]
    # inserting rulers
    if rulers_each is not None:
        for i_ruler in range(1, 1 + width // rulers_each):
            for row in str_map:
                idx = i_ruler - 1 + i_ruler * rulers_each
                if idx < len(row):
                    row.insert(idx, "┆")

    top_bound_chars = ["╭"]
    bot_bound_chars = ["╰"]
    horiz_ruler_chars = ["├"]
    for i in range(len(str_map[0])):
        top_bound_chars.append(
            "―" * target_len
            if not rulers_each or (i + 1 - ((i + 1) // rulers_each)) % rulers_each
            else "┬"
        )
        bot_bound_chars.append(
            "―" * target_len
            if not rulers_each or (i + 1 - ((i + 1) // rulers_each)) % rulers_each
            else "┴"
        )
        horiz_ruler_chars.append(
            "―" * target_len
            if not rulers_each or (i + 1 - ((i + 1) // rulers_each)) % rulers_each
            else "┼"
        )
    top_bound_chars.append("╮")
    bot_bound_chars.append("╯")
    horiz_ruler_chars.append("┤")
    lines: list[str] = ["".join(top_bound_chars)]
    for i_row, row in enumerate(str_map):
        lines.append("".join(["│"] + row + ["│"]))
        if i_row != len(str_map) - 1 and rulers_each and (i_row + 1) % rulers_each == 0:
            lines.append("".join(horiz_ruler_chars))
    lines.append("".join(bot_bound_chars))
    return "\n".join(lines)


def dimensions(map: Map) -> Coords:
    return len(map), len(map[0])


def init_map(init_value: T, height: int, width: int) -> Map[T]:
    return [[init_value for _ in range(width)] for _ in range(height)]


def transposed(map: Map[T]) -> Map[T]:
    return [list(c) for c in zip(*map)]


def init_map_like(init_value: T, other: list[list[Any]]) -> Map[T]:
    return init_map(init_value, *dimensions(other))


DefaultT = TypeVar("DefaultT")


def sparse_to_dense_map(
    coord_values: dict[Coords, T],
    default: DefaultT,
    top_left_corner: Coords | None = None,
    bottom_right_corner: Coords | None = None,
) -> tuple[Map[T | DefaultT], tuple[int, int]]:
    if top_left_corner is None:
        i_min = min(i for i, _ in coord_values.keys())
        j_min = min(j for _, j in coord_values.keys())
    else:
        i_min, j_min = top_left_corner
    if bottom_right_corner is None:
        i_max = max(i for i, _ in coord_values.keys())
        j_max = max(j for _, j in coord_values.keys())
    else:
        i_max, j_max = bottom_right_corner

    map_: Map[T | DefaultT] = init_map(
        default,
        height=i_max - i_min + 1,
        width=j_max - j_min + 1,
    )
    for (i, j), value in coord_values.items():
        if i_min <= i <= i_max and j_min <= j <= j_max:
            map_[i - i_min][j - j_min] = value

    return map_, (i_min, j_min)


def _choose_first_truthy(values: tuple[T, ...]) -> T:
    for value in values:
        if value:
            return value
    else:
        return values[-1]


def union_maps(
    *maps: Map[T],
    choose: Callable[[tuple[T, ...]], T] = _choose_first_truthy,
) -> Map[T]:
    assert len({dimensions(map) for map in maps}) == 1
    return [[choose(cells) for cells in zip(*map_rows)] for map_rows in zip(*maps)]
