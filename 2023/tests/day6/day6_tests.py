from day6 import day6

lines = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]


def test_part1():
    runner = day6.Day6Part1()
    result = runner.run(lines)
    expected = 288
    if result != expected:
        raise Exception(f"Expected {expected} got {result}")
    else:
        print("Part1 Success!")


def test_part2():
    runner = day6.Day6Part2()
    result = runner.run(lines)
    expected = 71503
    if result != expected:
        raise Exception(f"Expected {expected} got {result}")
    else:
        print("Part2 Success!")


if __name__ == "__main__":
    test_part1()
    test_part2()
