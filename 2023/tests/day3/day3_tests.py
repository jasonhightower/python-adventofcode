from day3 import day3


def test_part1():
    lines = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    d3p1 = day3.Day3Part1()
    result = d3p1.run(lines)
    print(f"Expecting 4361 got {result}")


def test_part2():
    lines = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    d3p2 = day3.Day3Part2()
    result = d3p2.run(lines)
    print(f"Expecting 467835 got {result}")


if __name__ == "__main__":
    test_part1()
    test_part2()
