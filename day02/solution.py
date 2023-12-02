import collections
import enum
import operator
import re
from dataclasses import dataclass
from functools import reduce
from typing import MutableMapping


class CubeColor(enum.Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    def __repr__(self) -> str:
        return self.value


@dataclass
class ColoredCubesDraw:
    count: int
    color: CubeColor


@dataclass
class Game:
    id_: int
    draws: list[list[ColoredCubesDraw]]

    @classmethod
    def parse(cls, line: str) -> "Game":
        game_re = re.compile(r"Game (\d+): (.*)")
        game_match = game_re.match(line)
        assert game_match
        game_id = int(game_match.group(1))
        game_body: str = game_match.group(2)

        draws_str = game_body.split(";")
        draws: list[list[ColoredCubesDraw]] = []
        for draw_str in draws_str:
            draw: list[ColoredCubesDraw] = []
            colored_cube_draws_str = draw_str.strip().split(",")
            for colored_cube_draw_str in colored_cube_draws_str:
                number, color = colored_cube_draw_str.strip().split(" ")
                draw.append(ColoredCubesDraw(count=int(number), color=CubeColor(color)))
            draws.append(draw)
        return Game(id_=game_id, draws=draws)


def part_1(inp: str, debug: bool):
    total_count = {
        CubeColor.RED: 12,
        CubeColor.GREEN: 13,
        CubeColor.BLUE: 14,
    }
    games = [Game.parse(line) for line in inp.splitlines()]
    possible_games = [
        game
        for game in games
        if all(
            all(
                colored_cube_draw.count <= total_count[colored_cube_draw.color]
                for colored_cube_draw in draw
            )
            for draw in game.draws
        )
    ]
    print(sum(g.id_ for g in possible_games))


def part_2(inp: str, debug: bool):
    res = 0
    for line in inp.splitlines():
        game = Game.parse(line)
        max_cubes_per_color: MutableMapping[CubeColor, int] = collections.defaultdict(lambda: 0)
        for draw in game.draws:
            for colored_cubes_draw in draw:
                max_cubes_per_color[colored_cubes_draw.color] = max(
                    max_cubes_per_color[colored_cubes_draw.color], colored_cubes_draw.count
                )
        power = reduce(operator.mul, max_cubes_per_color.values(), 1)
        res += power
    print(res)
