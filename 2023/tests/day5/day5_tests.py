from day5 import day5

lines = [
    "seeds: 79 14 55 13",
    "",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]


def test_part1():
    runner = day5.Day5Part1()
    result = runner.run(lines)
    expected = 35
    if result != expected:
        raise Exception(f"Expected {expected} got {result}")
    else:
        print("Part1 Success!")


def test_part2():
    runner = day5.Day5Part2()
    result = runner.run(lines)
    expected = 46
    if result != expected:
        raise Exception(f"Expected {expected} got {result}")
    else:
        print("Part2 Success!")


if __name__ == "__main__":
#    test_part1()
    test_part2()
