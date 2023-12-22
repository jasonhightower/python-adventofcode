import math


def calc_distance(hold_time: int, max_time: int):
    return hold_time * (max_time - hold_time)


def parse_numbers(input: str) -> list[int]:
    return [int(num) for num in input.split(' ') if num != '']


def find_possible_results(race: (int, int)) -> int:
    i = 1
    while i < race[0]:
        if calc_distance(i, race[0]) > race[1]:
            index = i - 1
            result = (race[0] - 1) - 2*index
            return result
        i += 1
    return 0


class Day6Part1:

    def run(self, input) -> int:
        times = parse_numbers(input[0].split(':')[1])
        records = parse_numbers(input[1].split(':')[1])

        results = [find_possible_results(race) for race in zip(times, records)]
        return math.prod(results)


class Day6Part2:

    def run(self, input) -> int:
        time = int(str(input[0]).split(':')[1].replace(' ', ''))
        record = int(str(input[1]).split(':')[1].replace(' ', ''))

        return find_possible_results((time, record))
