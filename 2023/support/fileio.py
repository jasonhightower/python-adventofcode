def lines_from_file(path: str) -> list[str]:
    file = open(file=path, mode='r')
    return file.readlines()
