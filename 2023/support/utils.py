
def parse_numbers(input: str) -> list[int]:
    return [int(num) for num in input.split(' ') if num != '']
