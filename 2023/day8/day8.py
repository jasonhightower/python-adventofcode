import math
from functools import reduce


START = 'AAA'
END = 'ZZZ'


def get_dir(directions: list[int], index: int) -> int:
    return directions[index % len(directions)]


class Day8Part1:

    def run(self, input) -> int:
        input_iter = iter(input)
        directions = next(input_iter, None)
        next(input_iter, None)

        entries = [(segment[0][:3],(segment[1][2:5], segment[1][7:-1])) for segment in [line.split('=') for line in input_iter]]
        map = dict((key, value) for key, value in entries)

        directions = [0 if dir == 'L' else 1 for dir in directions]
        count = 0

        current = START
        while current != END:
            current = map[current][get_dir(directions, count)]
            count += 1

        return count


class Day8Part2:

    def run(self, input) -> int:
        input_iter = iter(input)
        directions = next(input_iter, None)
        next(input_iter, None)

        entries = [(segment[0][:3],(segment[1][2:5], segment[1][7:-1])) for segment in [line.split('=') for line in input_iter]]
        map = dict((key, value) for key, value in entries)

        directions = [0 if dir == 'L' else 1 for dir in directions]
        count = 0
        nodes = [key for key in map.keys() if str(key).endswith('A')]

        interval = []
        while len(nodes) > 0:
            dir = get_dir(directions, count)
            nodes = [map[node][dir] for node in nodes]
            for node in nodes:
                if node.endswith('Z'):
                    nodes.remove(node)
                    interval.append(count + 1)
            count += 1

        print(interval)
        return reduce(lambda x,y:math.lcm(x,y), interval)

    def is_finished(self, nodes: list[str]) -> bool:
        for node in nodes:
            if not node.endswith('Z'):
                return False
        return True
