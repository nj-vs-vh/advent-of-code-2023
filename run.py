import argparse
import importlib
import time
import traceback
from pathlib import Path
from typing import Optional


def run_day(
    day: int,
    input_: str,
    parts_to_run: list[int],
    debug: bool,
) -> tuple[Optional[float], Optional[float]]:
    day_package_name = f"day{day:0>2}"
    day_dir = Path(__file__).parent / day_package_name
    if not day_dir.exists():
        raise ValueError(f"Solution dir not found for day = {day}")

    input_file = day_dir / input_
    input_ = input_file.read_text()

    solution = importlib.import_module(f"{day_package_name}.solution")
    runtime_1, runtime_2 = None, None
    if 1 in parts_to_run:
        print(f"\nRunning day {day} pt. 1...")
        try:
            t_start = time.time()
            solution.part_1(input_, debug)
            runtime_1 = 1000 * (time.time() - t_start)
            print(f"Done in {runtime_1:.4f} msec")
        except Exception:
            print("Error running pt. 1")
            traceback.print_exc()
    if 2 in parts_to_run:
        print(f"\nRunning day {day} pt. 2...")
        try:
            t_start = time.time()
            solution.part_2(input_, debug)
            runtime_2 = 1000 * (time.time() - t_start)
            print(f"Done in {runtime_2:.4f} msec")
        except Exception:
            print("Error running pt. 2")
            traceback.print_exc()
    return runtime_1, runtime_2


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day")
    parser.add_argument("--input", required=False, default="input.txt")
    parser.add_argument("--debug", required=False, action="store_true")
    parser.add_argument("--parts", required=False, default="1,2")

    args = parser.parse_args()

    run_day(
        day=int(args.day),
        input_=args.input,
        parts_to_run=[int(p) for p in args.parts.split(",")],
        debug=args.debug,
    )
