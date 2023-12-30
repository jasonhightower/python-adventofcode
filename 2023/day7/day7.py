from enum import Enum
from collections import Counter


CARD_VAL_LUT={
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

ORDER = 'J23456789TXQKA'

class HandType(Enum):
    FIVE_OF_A_KIND=7
    FOUR_OF_A_KIND=6
    FULL_HOUSE=5
    THREE_OF_A_KIND=4
    TWO_PAIR=3
    ONE_PAIR=2
    HIGH_CARD=1


class Day7Part1:

    def run(self, input) -> int:
        hands = [parse_hand(line, False) for line in input]

        hands.sort()

        result = 0
        rank = 1
        for hand in hands:
            print(hand)
            score = hand.bid * rank
            result += score
            rank += 1

        return result


RANK_LUT = [(1,1,1,1,1), (1,1,1,2), (1,2,2), (1,1,3), (2, 3), (1,4), (5,)]


class Day7Part2:

    def rank(self, hand):
        counts = tuple(sorted(Counter([ORDER.index(h) for h in hand]).values()))
        return RANK_LUT.index(counts)

    def run(self, input) -> int:
        hands = [(x, int(y)) for (x,y) in [hand.split() for hand in input]]
        rank = [(str(max([self.rank(h) for h in [hand.replace('J', r) for r in '23456789TQKA']])) + '-' + hand, bid) for (hand, bid) in hands]
        rank = sorted([(r.translate(str.maketrans('TQKAJ','ABCD1')), bid) for (r, bid) in rank])
        result = 0
        for i, (r, bid) in enumerate(rank):
            result += (i+1)*bid
        return result

class Hand:

    def __init__(self, cards: str, bid: int, play_joker: bool = False):
        self.bid = bid
        self.card_str = cards
        self.cards = {}
        self.high_cards = [0]*5
        self.joker_count = 0
        for i, c in enumerate(cards):
            self.cards[c] = self.cards[c] + 1 if c in self.cards else 1
            if c == 'J' and play_joker:
                self.high_cards[i] = 1
                self.joker_count += 1
            else:
                self.high_cards[i] = CARD_VAL_LUT[c]

        max_count = max(self.cards.values())
        match(max_count):
            case 5:
                self.type=HandType.FIVE_OF_A_KIND
            case 4:
                self.type=HandType.FOUR_OF_A_KIND
            case 3:
                self.type = HandType.FULL_HOUSE if len(self.cards) == 2 else HandType.THREE_OF_A_KIND
            case 2:
                self.type = HandType.TWO_PAIR if len(self.cards) == 3 else HandType.ONE_PAIR
            case _:
                self.type = HandType.HIGH_CARD

        if self.joker_count > 0:
            match self.type:
                case HandType.HIGH_CARD:
                    self.type = HandType.ONE_PAIR
                case HandType.ONE_PAIR:
                    self.type = HandType.THREE_OF_A_KIND
                case HandType.TWO_PAIR:
                    if self.joker_count == 2:
                        self.type = HandType.FOUR_OF_A_KIND
                    else:
                        self.type = HandType.FULL_HOUSE
                case HandType.THREE_OF_A_KIND:
                    if self.joker_count == 1:
                        self.type = HandType.FOUR_OF_A_KIND
                    else:
                        self.type = HandType.FIVE_OF_A_KIND
                case HandType.FULL_HOUSE:
                    self.type = HandType.FIVE_OF_A_KIND
                case HandType.FOUR_OF_A_KIND:
                    self.type = HandType.FIVE_OF_A_KIND

    def __str__(self):
        return f"{self.card_str} | {self.bid:04d} || {self.type} - {self.high_cards}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other) -> bool:
        return self.type == other.type and self.card_str == other.card_str

    def __lt__(self, other) -> bool:
        if self.type.value == other.type.value:
            return self.high_cards < other.high_cards
        return self.type.value < other.type.value


def parse_hand(line: str, play_joker: bool = False) -> Hand:
    segments = line.split(' ')
    cards = segments[0]
    bid = int(segments[1])
    return Hand(cards, bid, play_joker)
