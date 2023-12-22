def parse_numbers(input: str) -> list[int]:
    return [int(num) for num in input.split(' ') if num != '']


def numbers_as_intervals(numbers: list[int]):
    results = []
    i = 0
    while i < len(numbers):
        results.append((numbers[i], numbers[i] + numbers[i+1]))
        i += 2
    return results


def parse_maps(lineiter: iter) -> dict:
    maps = {}
    while True:
        map = parse_map(lineiter)
        if map is None:
            return maps
        maps[map.source_type] = map


def parse_map(lineiter: iter) -> None:
    title = next(lineiter, None)
    if title is None:
        return None
    segments = title.split(' ')[0].split('-')
    source_type = segments[0]
    dest_type = segments[2]
    map = RangeMap(source_type, dest_type)
    while True:
        entry = next(lineiter, None)
        if entry is None or entry.strip() == '':
            return map
        numbers = parse_numbers(entry)
        map.put(numbers[1], numbers[0], numbers[2])


class RangeMap:

    def __init__(self,
                 source_type: str,
                 dest_type: str):
        self.source_type = source_type
        self.dest_type = dest_type
        self.entries = []

    def put(self, source: int, dest: int, length: int):
        self.entries.append((source, source + length, dest - source))

    def map_intervals(self, intervals: list[(int, int)]) -> list[(int, int)]:
        results = []
        for interval in intervals:
            results.extend(self.map_interval(interval))
        return results

    def map_interval(self, interval: (int, int)) -> list[(int, int)]:
        results = []
        interval_stack = [interval]
        while len(interval_stack) > 0:
            current = interval_stack.pop()
            overlapped = False
            for entry in self.entries:
                if self.intervals_overlap(current, entry):
                    results.append((max(current[0], entry[0]) + entry[2], min(current[1], entry[1]) + entry[2]))
                    if current[0] < entry[0]:
                        interval_stack.append((current[0], entry[0] - 1))
                    if current[1] > entry[1]:
                        interval_stack.append((entry[1] + 1, current[1]))
                    overlapped = True
            if not overlapped:
                results.append(current)
        return results

    def intervals_overlap(self, source: (int, int), target: (int, int)) -> bool:
        return not (source[0] > target[1] or source[1] < target[0])

    def get(self, index: int):
        for entry in self.entries:
            if index >= entry[0] and index <= entry[1]:
                return index + entry[2]
        return index


class Day5Part1:

    def run(self, input) -> int:
        lineiter = iter(input)

        values = parse_numbers(next(lineiter, None).split(':')[1])

        next(lineiter, None)
        maps = parse_maps(lineiter)

        target = 'location'
        current = 'seed'

        while current != target:
            map = maps[current]
            values = [map.get(value) for value in values]
            current = map.dest_type

        return min(values)


class Day5Part2:

    def run(self, input) -> int:
        lineiter = iter(input)

        numbers = parse_numbers(next(lineiter, None).split(':')[1])
        intervals = numbers_as_intervals(numbers)

        next(lineiter, None)
        maps = parse_maps(lineiter)

        target = 'location'
        current = 'seed'

        while current != target:
            map = maps[current]
            intervals = map.map_intervals(intervals)
            current = map.dest_type

        return min(intervals)[0]
