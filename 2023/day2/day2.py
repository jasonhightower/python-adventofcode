class Day2Part1:

    def run(self, lines, args: list[str]) -> int:
        if len(args) < 3:
            print("Day2Part1 requires 3 args")
            return -1

        red = int(args[0])
        green = int(args[1])
        blue = int(args[2])

        count = 0
        for i, line in enumerate(lines):
            turns = line.split(':')[1].split(';')
            possible = True
            for turn in turns:
                if not self.is_possible(turn, red, green, blue):
                    possible = False
                    break
            if possible:
                count += i + 1
        return count

    def is_possible(self, turn: str, red: int, green: int, blue: int) -> bool:
        counts = turn.split(',')
        for count in counts:
            splits = count.strip().split(' ')
            num = int(splits[0])
            color = splits[1]
            if color == 'red':
                if num > red:
                    return False
            elif color == 'green':
                if num > green:
                    return False
            elif color == 'blue':
                if num > blue:
                    return False
            else:
                raise Exception(f"Unknown color '{color}'")
        return True


class Day2Part2:

    def run(self, lines) -> int:
        count = 0
        for i, line in enumerate(lines):
            turns = line.split(':')[1].split(';')
            max = [0, 0, 0]
            for turn in turns:
                max = self.find_max(turn, max)
            count += (max[0] * max[1] * max[2])
            print(f"{count} - {max}")
        return count

    def find_max(self, turn: str, max: list[int]) -> list[int]:
        counts = turn.split(',')
        for count in counts:
            splits = count.strip().split(' ')
            num = int(splits[0])
            color = splits[1]
            if color == 'red':
                if num > max[0]:
                    max[0] = num
            elif color == 'green':
                if num > max[1]:
                    max[1] = num
            elif color == 'blue':
                if num > max[2]:
                    max[2] = num
            else:
                raise Exception(f"Unknown color '{color}'")
        return max
