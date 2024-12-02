from day12 import day12


def test_run():
    input = ['???.### 1,1,3']
    solution = day12.Day12Part1()
    result = solution.run(input)
    assert result == 1


def test_run10():
    input = ['?###???????? 3,2,1']
    solution = day12.Day12Part1()
    result = solution.run(input)
    assert result == 10


def test_run3():
    input = ['?#?#?#?#?#?#?#? 1,3,1,6']

    solution = day12.Day12Part1()
    result = solution.run(input)
    assert result == 1

def test_input():
    input = [
"???.### 1,1,3",
".??..??...?##. 1,1,3",
"?#?#?#?#?#?#?#? 1,3,1,6",
"????.#...#... 4,1,1",
"????.######..#####. 1,6,5",
"?###???????? 3,2,1",
            ]
    solution = day12.Day12Part1()
    result = solution.run(input)
    assert result == 21


def test_input_part2():
    input = [
"???.### 1,1,3",
".??..??...?##. 1,1,3",
"?#?#?#?#?#?#?#? 1,3,1,6",
"????.#...#... 4,1,1",
"????.######..#####. 1,6,5",
"?###???????? 3,2,1",
            ]
    solution = day12.Day12Part2()
    result = solution.run(input)
    assert result == 525152


def test_part2_run():
    input = ['???.### 1,1,3']
    solution = day12.Day12Part2()
    result = solution.run(input)
    assert result == 1
