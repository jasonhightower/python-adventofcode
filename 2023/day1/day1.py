from support import fileio


class Day1Part1:

    def run(self, lines) -> int:
        result = 0
        for line in lines:
            result += self._line_val(line)
        return result

    def _line_val(self, input: str) -> int:
        number = self._first_digit(input) + self._last_digit(input)
        return int(number)

    def _first_digit(self, input: str) -> str:
        for i in range(len(input)):
            if self._is_digit(input[i]):
                return input[i]
        raise Exception(f"Could not find first digit from '{input}'")

    def _last_digit(self, input: str) -> str:
        for i in range(len(input) - 1, -1, -1):
            if self._is_digit(input[i]):
                return input[i]
        raise Exception(f"Could not find last digit from '{input}'")

    def _is_digit(self, input: str) -> bool:
        return input >= '0' and input <= '9'


number_text = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
]


class Day1Part2:

    def run(self, lines) -> int:
        result = 0
        for line in lines:
            result += self._line_val(line)
        return result

    def _line_val(self, input: str) -> int:
        number = self._first_digit(input) + self._last_digit(input)
        print(number)
        return int(number)

    def _first_digit(self, input: str) -> str:
        for i in range(len(input)):
            digit = self._read_digit(input, i)
            if digit is not None:
                return digit
        raise Exception(f"Could not find first digit from '{input}'")

    def _last_digit(self, input: str) -> str:
        for i in range(len(input) - 1, -1, -1):
            digit = self._read_digit(input, i)
            if digit is not None:
                return digit
        raise Exception(f"Could not find last digit from '{input}'")

    def _read_digit(self, input: str, index: int) -> str | None:
        if input[index] >= '0' and input[index] <= '9':
            return input[index]
        return self._read_number(input, index)

    def _read_number(self, input: str, index: int) -> str | None:
        # brute force, do something better
        for i, number in enumerate(number_text):
            if input[index:].startswith(number):
                return str(i + 1)
        return None


if __name__ == '__main__':
    lines = fileio.lines_from_file('day1_part1.txt')
    d1p1 = Day1Part1()
    result = d1p1.run(lines)
    print(result)
