import re
from typing import Iterable, Literal


def hash_(string: str) -> int:
    hash_ = 0
    for char in string:
        hash_ = ((hash_ + ord(char)) * 17) % 256
    return hash_


def part_1(inp: str, debug: bool):
    print(sum(hash_(instruction) for instruction in inp.split(",")))


LensLabel = str
FocalLength = int

RemoveLens = Literal["remove"]
AddLens = FocalLength
Action = AddLens | RemoveLens


def iter_instructions(inp: str) -> Iterable[tuple[LensLabel, Action]]:
    instruction_re = re.compile(r"(\w+)((-)|(=(\d+)))(,|$)")
    for match_ in instruction_re.finditer(inp):
        label = match_.group(1)
        if match_.group(3) is not None:
            action: Action = "remove"
        else:
            action = int(match_.group(5))
        yield label, action


def part_2(inp: str, debug: bool):
    boxes: tuple[list[tuple[LensLabel, FocalLength]], ...] = tuple([[] for _ in range(256)])
    for lens_label, action in iter_instructions(inp):
        box_idx = hash_(lens_label)
        lens_slot_idx = next(
            (
                i
                for i, (
                    lens_label,
                    _,
                ) in enumerate(boxes[box_idx])
                if lens_label == lens_label
            ),
            None,
        )
        if action == "remove":
            if lens_slot_idx is not None:
                boxes[box_idx].pop(lens_slot_idx)
        else:
            if lens_slot_idx is not None:
                boxes[box_idx][lens_slot_idx] = (lens_label, action)
            else:
                boxes[box_idx].append((lens_label, action))

    focal_power = sum(
        (box_idx + 1)
        * sum(
            (lens_slot_idx + 1) * focal_length
            for lens_slot_idx, (_, focal_length) in enumerate(lenses)
        )
        for box_idx, (lenses) in enumerate(boxes)
    )
    print(focal_power)
