def parse_numbers(input: str) -> list[int]:
    return [int(num) for num in input.split(' ') if num != '']

def parse_cards(input) -> list:
    return [Card.parse(line.split(':')[1]) for line in input]


class Card:

    def __init__(self, winners: list[int], numbers: list[int]):
        self.winners = winners
        self.numbers = set(numbers)

    def count_matches(self) -> int:
        return len(self.numbers.intersection(self.winners))

    def parse(card_input: str):
        segments = card_input.split('|')
        winners = parse_numbers(segments[0])
        numbers = parse_numbers(segments[1])
        return Card(winners, numbers)


Card.parse = staticmethod(Card.parse)


class Day4Part1:

    def run(self, input) -> int:
        cards = parse_cards(input)
        return sum([self.calc_points(card.count_matches()) for card in cards])

    def calc_points(self, matches) -> int:
        if matches <= 1:
            return matches
        return 1 << (matches - 1)


class Day4Part2:

    def __init__(self):
        self.num_cards = []

    def run(self, input) -> int:
        cards = parse_cards(input)
        self.num_cards = [1] * len(cards)

        for i, card in enumerate(cards):
            matches = card.count_matches()
            if matches > 0:
                start = i + 1
                for j in range(start, start + matches):
                    self.num_cards[j] += self.num_cards[i]
        return sum(self.num_cards)
