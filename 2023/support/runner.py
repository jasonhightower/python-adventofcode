import sys


def main(day: int, part: int, args=None):
    classname = f"Day{day}Part{part}"
    mod = __import__(f"day{day}.day{day}", fromlist=[classname])
    klass = getattr(mod, classname)

    inst = klass()
    with open(f"day{day}.txt") as f:
        input = [line.rstrip('\n') for line in f]
        if args is None:
            result = inst.run(input)
        else:
            result = inst.run(input, args)
        if result is not None:
            print(result)


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
