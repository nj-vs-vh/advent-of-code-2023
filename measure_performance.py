import math
import os
import re
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from run import run_day


@contextmanager
def suppress_output():
    with open(os.devnull, "w") as fnull:
        with redirect_stderr(fnull) as err, redirect_stdout(fnull) as out:
            yield (err, out)


@dataclass
class PerfMeasurement:
    t_sample: list[float]

    @property
    def mean(self) -> float:
        return float(np.mean(self.t_sample))

    def __add__(self, other: "PerfMeasurement") -> "PerfMeasurement":
        assert len(self.t_sample) == len(other.t_sample)
        return PerfMeasurement([t1 + t2 for t1, t2 in zip(self.t_sample, other.t_sample)])

    def __str__(self) -> str:
        std = np.std(self.t_sample)
        std_log10 = math.log10(std)
        ndigits = -math.floor(std_log10)
        return f"{round(self.mean, ndigits)} ± {round(std, ndigits)}"


if __name__ == "__main__":
    days_perf: list[tuple[int, tuple[PerfMeasurement, PerfMeasurement]]] = []
    for day in range(1, 26):
        try:
            print(f"Measuring day {day}...")
            sample_1: list[float] = []
            sample_2: list[float] = []
            with suppress_output():
                for _ in range(100):
                    t1, t2 = run_day(day, input_="input.txt", parts_to_run=[1, 2], debug=False)
                    assert t1
                    assert t2
                    sample_1.append(t1)
                    sample_2.append(t2)
            days_perf.append(
                (
                    day,
                    (
                        PerfMeasurement(sample_1),
                        PerfMeasurement(sample_2),
                    ),
                )
            )
        except Exception:
            print(f"Error measuring day {day}, ignoring")

    # calculating "scores"
    both_part_measurements = [p1 + p2 for _, (p1, p2) in days_perf]
    log_mean_both_parts = [math.log(bp.mean) for bp in both_part_measurements]
    center_logtime = np.mean(log_mean_both_parts)
    min_logtime = min(log_mean_both_parts)
    max_logtime = max(log_mean_both_parts)
    scores = [
        (
            (center_logtime - logtime) / (center_logtime - min_logtime)
            if logtime < center_logtime
            else -(logtime - center_logtime) / (max_logtime - center_logtime)
        )
        for logtime in log_mean_both_parts
    ]

    # results formatting
    headers = [
        "**Day**",
        "**Part 1**, msec",
        "**Part 2**, msec",
        "**Total**, msec",
        "**Relative score**",
    ]
    markdown_table = [
        headers,
        ["---:"] + [":---:"] * (len(headers) - 2) + ["---"],
    ]
    total_part_1: PerfMeasurement | None = None
    total_part_2: PerfMeasurement | None = None
    total_both_parts: PerfMeasurement | None = None
    for (day, (part_1, part_2)), both_parts, score in zip(
        days_perf, both_part_measurements, scores
    ):
        max_emoji_score_len = 10
        emoji_score_len = round(max_emoji_score_len * abs(score))
        if emoji_score_len == 0:
            score_emojis = "🛹"
        else:
            score_emojis = "🚀" * emoji_score_len if score > 0 else "🐢" * emoji_score_len
        markdown_table.append([str(day), str(part_1), str(part_2), str(both_parts), score_emojis])

        total_part_1 = part_1 if total_part_1 is None else total_part_1 + part_1
        total_part_2 = part_2 if total_part_2 is None else total_part_2 + part_2
        total_both_parts = (
            both_parts if total_both_parts is None else total_both_parts + both_parts
        )

    markdown_table.append(
        ["All days", str(total_part_1), str(total_part_2), str(total_both_parts), ""]
    )

    readme_file = Path(__file__).parent / "README.md"
    readme = readme_file.read_text()
    readme = re.sub(
        (
            "(?<="
            + re.escape("<!-- generated table start -->")
            + ")(.*)(?="
            + re.escape("<!-- generated table end -->")
            + ")"
        ),
        "\n" + "\n".join([" | ".join(row) for row in markdown_table]) + "\n",
        readme,
        flags=re.MULTILINE | re.DOTALL,
    )
    readme_file.write_text(readme)
    print("Done")
