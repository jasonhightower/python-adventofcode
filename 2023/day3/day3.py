class Day3Part1:

    def run(self, input) -> int:
        count = 0
        for y in range(len(input)):
            line = input[y]
            line_len = len(line)
            x = 0
            while x < line_len:
                if self.is_digit(line[x]):
                    end = self.find_end(x, line)
                    engine_part = int(input[y][x:end])
                    print(f"Checking {engine_part}")
                    if self.is_engine_part(input, x, end, y):
                        print("YES")
                        count += engine_part
                    x = end
                else:
                    x += 1
        return count

    def is_engine_part(self, input, start, end, line_num) -> bool:
        if self.is_symbol(start - 1, line_num, input) or self.is_symbol(end, line_num, input):
            return True
        for x in range(start - 1, end + 1):
            if self.is_symbol(x, line_num - 1, input) or self.is_symbol(x, line_num + 1, input):
                return True
        return False

    def is_symbol(self, x: int, y: int, input: list[str]) -> bool:
        if x < 0 or y < 0 or y >= len(input) or x >= len(input[y]):
            return False
        c = input[y][x]
        if c != '.' and not self.is_digit(c):
            print(f"{c} is symbol")
            return True
        return False

    def is_digit(self, char) -> bool:
        return char >= '0' and char <= '9'

    def find_end(self, start: int, line: str) -> int:
        i = start + 1
        while i < len(line) and self.is_digit(line[i]):
            i += 1
        return i


class Day3Part2:

    def run(self, input) -> int:
        symbols = []

        for y in range(len(input)):
            line = input[y]
            for x in range(len(input)):
                if line[x] == '*':
                    symbols.append(self.parse_symbol((x, y), input))

        count = 0
        for symbol in symbols:
            if symbol.is_gear():
                print(f"Gear {symbol.x},{symbol.y} - {symbol.part_numbers}")
                count += symbol.calc_gear_ratio()
        return count

    def parse_symbol(self, pos: (int, int), input):
        symbol = Symbol(pos[0], pos[1])
        y = pos[1] - 1
        while y <= pos[1] + 1:
            x = pos[0] - 1
            while x <= pos[0] + 1:
                if self.is_digit(x, input[y]):
                    start = self.find_start_digit(x, input[y])
                    end = self.find_end_digit(x, input[y])
                    print(f"found num {start} to {end} at line {y} -- {input[y][start:end]}")
                    symbol.add_part_no(int(input[y][start:end]))
                    x = end
                x += 1
            y += 1
        return symbol

    def valid(self, x: int, y: int, w: int, h: int) -> bool:
        return x >= 0 and y >= 0 and x < w and y < h

    def is_digit(self, x: int, line: str) -> bool:
        if x < 0 or x >= len(line):
            return False
        return line[x] >= '0' and line[x] <= '9'

    def find_start_digit(self, x: int, line: str) -> int:
        while True:
            if not self.is_digit(x - 1, line):
                return x
            x -= 1

    def find_end_digit(self, x: int, line: str) -> int:
        while True:
            if not self.is_digit(x + 1, line):
                return x + 1
            x += 1


class Symbol:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.part_numbers = []

    def is_gear(self):
        return len(self.part_numbers) == 2

    def calc_gear_ratio(self) -> int | None:
        if self.is_gear():
            return self.part_numbers[0] * self.part_numbers[1]
        return None

    def add_part_no(self, part_no: int):
        self.part_numbers.append(part_no)
