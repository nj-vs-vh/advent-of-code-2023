import collections
import functools
from dataclasses import dataclass
from typing import ClassVar, Literal


def card_cost_pt1(card: str) -> int:
    match card:
        case "2":
            return 0
        case "3":
            return 1
        case "4":
            return 2
        case "5":
            return 3
        case "6":
            return 4
        case "7":
            return 5
        case "6":
            return 6
        case "8":
            return 7
        case "9":
            return 8
        case "T":
            return 9
        case "J":
            return 10
        case "Q":
            return 11
        case "K":
            return 12
        case "A":
            return 13
    raise ValueError(f"Unexpected card: {card}")


def card_cost_pt2(card: str) -> int:
    match card:
        case "J":
            return 0
        case "2":
            return 1
        case "3":
            return 2
        case "4":
            return 3
        case "5":
            return 4
        case "6":
            return 5
        case "7":
            return 6
        case "6":
            return 7
        case "8":
            return 8
        case "9":
            return 9
        case "T":
            return 10
        case "Q":
            return 11
        case "K":
            return 12
        case "A":
            return 13
    raise ValueError(f"Unexpected card: {card}")


@functools.total_ordering
@dataclass
class Hand:
    cards: str
    card_costs: list[int]
    type: list[int]
    type_rank: int

    HAND_TYPES_RANKING: ClassVar = [
        [5],  # five of a kind
        [4, 1],  # four of a kind
        [3, 2],  # full house
        [3, 1, 1],  # three of a kind
        [2, 2, 1],  # two pair
        [2, 1, 1, 1],  # one pair
        [1, 1, 1, 1, 1],  # high hand
    ]

    @classmethod
    def parse(cls, cards: str, part: int) -> "Hand":
        card_cost_fn = card_cost_pt1 if part == 1 else card_cost_pt2
        card_costs = [card_cost_fn(card) for card in cards]
        card_count = collections.Counter(cards)
        if part == 2 and "J" in card_count and len(card_count) > 1:
            # in pt2 Joker pretends to be the most counted card to increase hand power
            joker_count = card_count.pop("J")
            max_count_card = max(card_count.items(), key=lambda cc: cc[1])[0]
            card_count[max_count_card] += joker_count
        type = sorted(card_count.values(), reverse=True)
        return Hand(
            cards=cards,
            card_costs=card_costs,
            type=type,
            type_rank=cls.HAND_TYPES_RANKING.index(type),
        )

    def __str__(self) -> str:
        return f"{self.cards} (type = {self.type}, type rank = {self.type_rank})"

    def __eq__(self, other: "Hand") -> bool:
        return self.cards == other.cards

    def __lt__(self, other: "Hand") -> bool:
        if self.type_rank == other.type_rank:
            return self.card_costs < other.card_costs
        else:
            return self.type_rank > other.type_rank


def parse_input(inp: str, part: Literal[1, 2]) -> list[tuple[Hand, int]]:
    res: list[tuple[Hand, int]] = []
    for line in inp.splitlines():
        cards, bid = line.split()
        res.append((Hand.parse(cards=cards, part=part), int(bid)))
    return res


def calculate_winnings(hands_with_bids: list[tuple[Hand, int]], debug: bool) -> int:
    if debug:
        for hand, bid in hands_with_bids:
            print(hand, "bid = ", bid)
    hands_with_bids.sort(key=lambda hand_bid: hand_bid[0])
    if debug:
        print("Sorted:")
        for hand, bid in hands_with_bids:
            print(hand, "bid = ", bid)
    return sum(bid * (rank + 1) for rank, (_, bid) in enumerate(hands_with_bids))


def part_1(inp: str, debug: bool):
    hands_with_bids = parse_input(inp, part=1)
    print(calculate_winnings(hands_with_bids, debug=debug))


def part_2(inp: str, debug: bool):
    hands_with_bids = parse_input(inp, part=2)
    print(calculate_winnings(hands_with_bids, debug=debug))
