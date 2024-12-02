from support.utils import parse_numbers


class Day12Part1:

    def __init__(self):
        self.memos = {}

    def _as_key(self, chars: str, numbers: list[int], group_size: int) -> str:
        ck = 'n' if not chars else chars
        nk = 'n' if not numbers else ''.join([str(num) for num in numbers])
        gk = 'n' if not group_size else str(group_size)
        return ck + '|' + nk + '|' + gk

    def run(self, input) -> int:
        num_solutions = 0
        for line in input:
            segments = line.split(' ')
            chars = str(segments[0])
            if chars.endswith('#') or chars.endswith('?'):
                chars += '.'
            numbers = parse_numbers(segments[1], ',')
            result = self.calc_solutions(chars, numbers)
            num_solutions += result
        return num_solutions

    def calc_solutions(self, chars: str, numbers: list[int], group_size=0) -> int:
        key = self._as_key(chars, numbers, group_size)
        if key in self.memos:
            return self.memos[key]
        print(f"{key}")
        num_solutions = 0
        if len(chars) == 0:
            if len(numbers) == 0:
                num_solutions += 1
        else:
            cur = chars[0]
            if cur == '.':
                if group_size == 0:
                    num_solutions += self.calc_solutions(chars[1:], numbers)
                elif numbers[0] == group_size:
                    num_solutions += self.calc_solutions(chars[1:], numbers[1:])
            elif cur == '#':
                if len(numbers) > 0 and group_size < numbers[0]:
                    num_solutions += self.calc_solutions(chars[1:], numbers, group_size + 1)
            elif cur == '?':
                num_solutions += self.calc_solutions('.' + chars[1:], numbers, group_size)
                num_solutions += self.calc_solutions('#' + chars[1:], numbers, group_size)
        self.memos[key] = num_solutions
        return num_solutions


class Day12Part2(Day12Part1):

    def run(self, input) -> int:
        num_solutions = 0
        for line in input:
            segments = line.split(' ')
            chars = str(segments[0]) + '?'
            chars *= 5
            chars = chars[:-1] + '.'
            if chars.endswith('..'):
                chars = chars[:-1]
            numbers = parse_numbers(segments[1], ',')
            numbers *= 5
            result = self.calc_solutions(chars, numbers)
            num_solutions += result
        return num_solutions
