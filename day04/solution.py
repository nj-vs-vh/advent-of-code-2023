from dataclasses import dataclass
import re
from typing import ClassVar


@dataclass
class Card:
    number: int
    winning: set[int]
    have: set[int]

    def points(self) -> int:
        return len(self.winning & self.have)

    card_re: ClassVar[re.Pattern] = re.compile(r"Card\s+(\d+): ([\d ]+) \| ([\d ]+)$")

    @classmethod
    def parse(cls, line: str) -> "Card":
        m = cls.card_re.match(line)
        assert m is not None
        return Card(
            number=int(m.group(1)),
            winning={int(num) for num in m.group(2).strip().split()},
            have={int(num) for num in m.group(3).strip().split()},
        )



def part_1(inp: str, debug: bool):
    worth_total = 0
    for line in inp.splitlines():
        card = Card.parse(line)
        if debug:
            print(line, "-->", card)
        winning_numbers = card.points()
        worth_total += 2 ** (winning_numbers - 1) if winning_numbers > 0 else 0
    print(worth_total)


def part_2(inp: str, debug: bool):
    card_data = [Card.parse(line) for line in inp.splitlines()]
    card_copies = [1] * len(card_data)
    for idx, (card, copies) in enumerate(zip(card_data, card_copies)):
        for idx_copied in range(idx + 1, idx + card.points() + 1):
            card_copies[idx_copied] += copies
    
    print(sum(card_copies))
