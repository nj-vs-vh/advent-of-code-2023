import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import cProfile
import pstats

from solution import part_1, part_2

# hack to display time in msec
pstats.f8 = lambda x: f"{1000 * x :8.2f}"  # type: ignore


inp = (Path(__file__).parent / "input.txt").read_text()

profile = cProfile.Profile()
with profile:
    part_1(inp, debug=False)
    part_2(inp, debug=False)

ps = pstats.Stats(profile).sort_stats(pstats.SortKey.CALLS)
ps.print_stats()
