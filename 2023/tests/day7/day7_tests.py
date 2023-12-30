from day7 import day7

lines = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


def test_part1():
    runner = day7.Day7Part1()
    result = runner.run(lines)
    expected = -1
    if result != expected:
        raise Exception(f"Expected {expected} got {result}")
    else:
        print("Part1 Success!")


def test_part2():
    runner = day7.Day7Part2()
    result = runner.run(lines)
    expected = -1
    if result != expected:
        raise Exception(f"Expected {expected} got {result}")
    else:
        print("Part2 Success!")


if __name__ == "__main__":
    test_part1()
    test_part2()
