from day1 import day1


def test_part1():
    lines = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    d1p1 = day1.Day1Part1()
    result = d1p1.run(lines)
    print(f"Expecting 142 got {result}")


def test_part2():
    lines = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    d1p2 = day1.Day1Part2()
    result = d1p2.run(lines)
    print(f"Expecting 281 got {result}")


if __name__ == "__main__":
    test_part1()
    test_part2()
