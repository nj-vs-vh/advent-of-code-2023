import random
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

    h1 = random.choice(hailstones)
    h2 = random.choice(hailstones)
    V_range = 300
    rhs = np.array([h1.r.x, h1.r.y, h2.r.x, h2.r.y]).T
    for V1 in range(-V_range, V_range + 1):
        for V2 in range(-V_range, V_range + 1):
            xy_matrix = np.array(
                [
                    [1, 0, V1 - h1.v.x, 0],
                    [0, 1, V2 - h1.v.y, 0],
                    [1, 0, 0, V1 - h2.v.x],
                    [0, 1, 0, V2 - h2.v.y],
                ]
            )
            try:
                assert np.linalg.matrix_rank(xy_matrix) == 4, "matrix is not full rank"
                xy_solution = np.linalg.inv(xy_matrix) @ rhs
                R1, R2, t1, t2 = xy_solution[0], xy_solution[1], xy_solution[2], xy_solution[3]
                assert t1 > 0 and t2 > 0, "negative times found"
                for Ra in (R1, R2):
                    assert int(Ra) == Ra, "non-integer xy solution"
                V3 = (h1.r.z + h1.v.z * t1 - h2.r.z - h2.v.z * t2) / (t1 - t2)
                R3 = h1.r.z + h1.v.z * t1 - V3 * t1
                assert int(R3) == R3, "non-integer R3"
                R1 = int(R1)
                R2 = int(R2)
                R3 = int(R3)
                V1 = int(V1)
                V2 = int(V2)
                V3 = int(V3)
                print(R1, R2, R3, V1, V2, V3)
                for h in hailstones:
                    t = None
                    for num, den in (
                        ((h.r.x - R1), (V1 - h.v.x)),
                        ((h.r.y - R2), (V2 - h.v.y)),
                        ((h.r.z - R3), (V3 - h.v.z)),
                    ):
                        if den != 0:
                            ta = num / den
                            assert ta > 0
                            if t is None:
                                t = ta
                            else:
                                assert np.isclose(t, ta)
                print(R1, R2, R3, V1, V2, V3)
                print(R1 + R2 + R3)
                return
            except (np.linalg.LinAlgError, AssertionError, ZeroDivisionError) as e:
                # print(repr(e))
                pass
