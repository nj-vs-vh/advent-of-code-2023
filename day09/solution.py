import itertools


def parse_readings(inp: str) -> list[list[int]]:
    return [[int(num) for num in line.split()] for line in inp.splitlines()]


def calculate_deltas(reading: list[int]) -> list[list[int]]:
    res = [reading]
    while True:
        next_derivative = [s_1 - s_0 for s_0, s_1 in itertools.pairwise(res[-1])]
        if not next_derivative:
            next_derivative.append(0)
        res.append(next_derivative)
        if all(d == 0 for d in next_derivative):
            break
    return res


def extrapolate(reading: list[int], debug: bool) -> int:
    deltas = calculate_deltas(reading)
    if debug:
        print(reading, deltas)
    current_derivative_projection = 0
    for derivative in deltas[::-1]:
        current_derivative_projection = derivative[-1] + current_derivative_projection
    return current_derivative_projection


def part_1(inp: str, debug: bool):
    readings = parse_readings(inp)
    if debug:
        print(inp)
        print(readings)

    extrapolation_sum = 0
    for reading in readings:
        extrapolation_sum += extrapolate(reading, debug=debug)
    print(extrapolation_sum)


def part_2(inp: str, debug: bool):
    readings = parse_readings(inp)
    extrapolation_sum = 0
    for reading in readings:
        extrapolation_sum += extrapolate(reading[::-1], debug=debug)
    print(extrapolation_sum)
