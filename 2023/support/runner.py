import sys


def main(day: int, part: int, args=None):
    classname = f"Day{day}Part{part}"
    mod = __import__(f"day{day}.day{day}", fromlist=[classname])
    klass = getattr(mod, classname)

    solution = klass()
    if is_test(args):
        if len(args) == 1:
            args = None
        test(solution, day, part, args)
    else:
        run(solution, day, args)


def run(solution, day: int, args=None):
    with open(f"day{day}/day{day}.txt") as f:
        input = [line.rstrip('\n') for line in f]
        if args is None:
            result = solution.run(input)
        else:
            result = solution.run(input, args)
        if result is not None:
            print(result)


def test(solution, day: int, part: int, args=None):
    with open(f"day{day}/part{part}_test.txt") as f:
        input = [line.rstrip('\n') for line in f]
        expected = int(input[0])
        input = input[1:]
        if args is None:
            result = solution.run(input)
        else:
            result = solution.run(input, args)

        if result != expected:
            raise Exception(f"Expected {expected} got {result}")
        else:
            print(f"Day {day} Part {part} - Success")


def is_test(args) -> bool:
    if args is None or len(args) == 0:
        return False

    if args[0] == "test":
        return True
    return False


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage runner.py <day> <part> [extra arguments]")

    day = int(args[0])
    part = int(args[1])
    if len(args) > 2:
        main(day, part, args[2:])
    else:
        main(day, part)
