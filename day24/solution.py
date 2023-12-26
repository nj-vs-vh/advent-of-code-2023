import re
from dataclasses import dataclass
from typing import ClassVar

import numpy as np


@dataclass
class Vector3D:
    x: int
    y: int
    z: int


@dataclass
class Hailstone:
    r: Vector3D
    v: Vector3D

    REGEX: ClassVar = re.compile(
        r"(-?\d+),\s*(-?\d+),\s*(-?\d+)\s*@\s*(-?\d+),\s*(-?\d+),\s*(-?\d+)"
    )

    @classmethod
    def parse(cls, line: str) -> "Hailstone":
        m = cls.REGEX.match(line)
        assert m is not None, repr(line)
        return Hailstone(
            r=Vector3D(
                x=int(m.group(1)),
                y=int(m.group(2)),
                z=int(m.group(3)),
            ),
            v=Vector3D(
                x=int(m.group(4)),
                y=int(m.group(5)),
                z=int(m.group(6)),
            ),
        )


def part_1(inp: str, debug: bool):
    hailstones = [Hailstone.parse(line) for line in inp.splitlines()]

    bound_lower = 200000000000000
    bound_upper = 400000000000000
    crossings_within_bound = 0
    for i, h1 in enumerate(hailstones):
        for h2 in hailstones[i + 1 :]:
            t2_denom = h2.v.x * h1.v.y - h1.v.x * h2.v.y
            if t2_denom == 0:  # parallel speeds -> no crossing
                continue

            t2 = (h1.v.x * (h2.r.y - h1.r.y) - h1.v.y * (h2.r.x - h1.r.x)) / t2_denom
            if t2 <= 0:
                continue

            t1 = (
                (h2.r.y - h1.r.y + h2.v.y * t2) / h1.v.y
                if h1.v.y != 0
                else (h2.r.x - h1.r.x + h2.v.x * t2) / h1.v.x
            )
            if t1 <= 0:
                continue

            x_crossing = h2.r.x + h2.v.x * t2
            y_crossing = h2.r.y + h2.v.y * t2
            if (
                bound_lower <= x_crossing <= bound_upper
                and bound_lower <= y_crossing <= bound_upper
            ):
                if debug:
                    print(h1, h2)
                crossings_within_bound += 1

    print(crossings_within_bound)


def part_2(inp: str, debug: bool):
    hailstones = [Hailstone.parse(line) for line in inp.splitlines()]

    h1 = hailstones[0]
    h2 = hailstones[1]
    h3 = hailstones[2]
    rhs = np.array([h1.r.x, h1.r.y, h1.r.z, h2.r.x, h2.r.y, h2.r.z, h3.r.x, h3.r.y, h3.r.z]).T
    for V1 in range(-10, 10):
        for V2 in range(-10, 10):
            for V3 in range(-10, 10):
                matrix = np.array(
                    [
                        [1, 0, 0, V1, -h1.v.x, 0, 0, 0, 0],
                        [0, 1, 0, V2, -h1.v.y, 0, 0, 0, 0],
                        [0, 0, 1, V3, -h1.v.z, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, V1, -h2.v.x, 0, 0],
                        [0, 1, 0, 0, 0, V2, -h2.v.y, 0, 0],
                        [0, 0, 1, 0, 0, V3, -h2.v.z, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, V1, -h3.v.x],
                        [0, 1, 0, 0, 0, 0, 0, V2, -h3.v.y],
                        [0, 0, 1, 0, 0, 0, 0, V3, -h3.v.z],
                    ]
                )
                try:
                    print(matrix)
                    assert np.linalg.matrix_rank(matrix) == 9
                    solution = np.linalg.solve(matrix, rhs)
                    # inverse = np.linalg.inv(matrix)
                    # solution = inverse @ rhs
                    assert all(t > 0 for t in solution[3:])
                    R1, R2, R3 = solution[0], solution[1], solution[2]
                    print(V1, V2, V3)
                    print(int(R1) + int(R2) + int(R3))
                    for Ra in (R1, R2, R3):
                        assert int(Ra) == Ra
                    print(rhs)
                    print(matrix @ solution)
                    return
                except (np.linalg.LinAlgError, AssertionError):
                    pass
