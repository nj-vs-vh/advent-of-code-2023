from typing import Callable, TypeVar

T = TypeVar("T")


def format_map(
    map: list[list[T]],
    formatter: Callable[[T], str] = str,
    cell_width: int = 1,
) -> str:
    horizontal_bound = " " + "-" * len(map[0]) * cell_width + " "
    return "\n".join(
        [horizontal_bound]
        + [
            "".join(["|"] + [formatter(cell).center(cell_width, " ") for cell in row] + ["|"])
            for row in map
        ]
        + [horizontal_bound]
    )
