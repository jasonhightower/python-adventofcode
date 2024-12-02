
def parse_numbers(input: str, separator: str = ' ') -> list[int]:
    return [int(num) for num in input.split(separator) if num != '']
