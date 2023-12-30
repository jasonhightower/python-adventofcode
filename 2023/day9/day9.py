from support.utils import parse_numbers


class Day9Part1:

    def run(self, input) -> int:
        result = 0
        for line in input:
            result += self.solve(parse_numbers(line))
        return result

    def solve(self, numbers: list[int]) -> int:
        series = [numbers]
        result = self.calc(numbers)
        series.append(result[0])
        i = 1
        while result[1] is False:
            result = self.calc(series[i])
            series.append(result[0])
            i += 1

        solution = 0
        for i in range(len(series) - 1, -1, -1):
            end = series[i][len(series[i]) - 1]
            solution += end
        return solution

    def calc(self, series: list[int]) -> (list[int], bool):
        result = [0] * (len(series) - 1)
        same = True
        for i in range(len(series) - 1):
            result[i] = series[i + 1] - series[i]
            if same and result[i] != result[0]:
                same = False
        return (result, same)


class Day9Part2:

    def run(self, input) -> int:
        result = 0
        for line in input:
            numbers = parse_numbers(line)
            numbers.reverse()
            result += self.solve(numbers)
        return result

    def solve(self, numbers: list[int]) -> int:
        series = [numbers]
        result = self.calc(numbers)
        series.append(result[0])
        i = 1
        while result[1] is False:
            result = self.calc(series[i])
            series.append(result[0])
            i += 1

        last_end = 0
        for i in range(len(series) - 1, -1, -1):
            end = series[i][len(series[i]) - 1] - last_end
            last_end = end
        return last_end

    def calc(self, series: list[int]) -> (list[int], bool):
        result = [0] * (len(series) - 1)
        same = True
        for i in range(len(series) - 1):
            result[i] = series[i] - series[i + 1]
            if same and result[i] != result[0]:
                same = False
        return (result, same)
