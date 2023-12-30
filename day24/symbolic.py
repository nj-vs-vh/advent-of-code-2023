from sympy import Symbol
from sympy.solvers import solve

# unknowns
Rx = Symbol("Rx")
Ry = Symbol("Ry")
t1 = Symbol("t1")
t2 = Symbol("t2")

# parameters
dVx1 = Symbol("dVx1")
dVy1 = Symbol("dVy1")
dVx2 = Symbol("dVx2")
dVy2 = Symbol("dVy2")
r1x = Symbol("r1x")
r1y = Symbol("r1y")
r2x = Symbol("r2x")
r2y = Symbol("r2y")

s = solve(
    [
        Rx + dVx1 * t1 - r1x,  # type: ignore
        Ry + dVy1 * t1 - r1y,  # type: ignore
        Rx + dVx2 * t2 - r2x,  # type: ignore
        Ry + dVy2 * t2 - r2y,  # type: ignore
    ],
    [Rx, Ry, t1, t2],
)

print(*s.items(), sep="\n")
