import itertools
import math
import random
import re
from dataclasses import dataclass
from typing import ClassVar, Iterable


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


def ensure_int(v: float) -> int:
    v_int = int(v)
    assert v_int == v
    return v_int


def iter_xy_spiral() -> Iterable[tuple[int, int]]:
    yield (0, 0)
    for hw in itertools.count(start=1):
        yield from ((i, hw) for i in range(-hw, hw))
        yield from ((hw, j) for j in range(hw, -hw, -1))
        yield from ((i, -hw) for i in range(hw, -hw, -1))
        yield from ((-hw, i) for i in range(-hw, hw))


def part_2(inp: str, debug: bool):
    hailstones = [Hailstone.parse(line) for line in inp.splitlines()]
    h1 = random.choice(hailstones)
    h2 = random.choice(hailstones)
    for Vx, Vy in iter_xy_spiral():
        dVx1 = Vx - h1.v.x
        dVy1 = Vy - h1.v.y
        dVx2 = Vx - h2.v.x
        dVy2 = Vy - h2.v.y

        denominator = dVx1 * dVy2 - dVx2 * dVy1
        if denominator == 0:
            continue

        # symbolic solution for a three particle XY intersection
        t1 = (-dVx2 * h1.r.y + dVx2 * h2.r.y + dVy2 * h1.r.x - dVy2 * h2.r.x) / denominator
        t2 = (-dVx1 * h1.r.y + dVx1 * h2.r.y + dVy1 * h1.r.x - dVy1 * h2.r.x) / denominator
        if t1 < 0 or t2 < 0:
            continue

        try:
            Rx = ensure_int(h1.r.x - dVx1 * t1)
            Ry = ensure_int(h1.r.y - dVy1 * t1)
            Vz = ensure_int((h1.r.z + h1.v.z * t1 - h2.r.z - h2.v.z * t2) / (t1 - t2))
            Rz = ensure_int(h1.r.z + h1.v.z * t1 - Vz * t1)

            # at this point we nailed R and V vectors for two random hailstones, time to check
            # if the others are hit as well
            for h in hailstones:
                # for each hailstone we check that "hit time" is the same for x, y and z
                t_hit = None
                for numerator, denominator in (
                    ((h.r.x - Rx), (Vx - h.v.x)),
                    ((h.r.y - Ry), (Vy - h.v.y)),
                    ((h.r.z - Rz), (Vz - h.v.z)),
                ):
                    if denominator != 0:
                        ta = numerator / denominator
                        assert ta > 0
                        if t_hit is None:
                            t_hit = ta
                        else:
                            assert math.isclose(t_hit, ta)
                    else:
                        assert numerator == 0
            print(Rx, Ry, Rz, Vx, Vy, Vz)
            print(Rx + Ry + Rz)
            return
        except (AssertionError, ZeroDivisionError) as e:
            pass
