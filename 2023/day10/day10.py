import types
import math


class Board:

    def __init__(self, squares: list[str]):
        self.squares = squares
        self.__find_start()
        self.__visited = set()
        self.__visited.add((self.start[0], self.start[1]))

    def tile_at(self, x: int, y: int) -> str:
        if x < 0 or y < 0:
            return None
        return self.squares[y][x]

    def visited(self, x: int, y: int) -> bool:
        return (x, y) in self.__visited

    def mark_visited(self, x: int, y: int):
        self.__visited.add((x, y))

    def __find_start(self):
        for y in range(len(self.squares)):
            x = self.squares[y].find('S')
            if x != -1:
                self.start = (x, y)
                return
        raise Exception("Start not found")

    def visited_path(self) -> set((int, int)):
        return self.__visited


consts = types.SimpleNamespace()

consts.UP = 1
consts.DOWN = 2
consts.LEFT = 3
consts.RIGHT = 4

consts.RIGHT_LUT = {
        'J': consts.UP,
        '-': consts.RIGHT,
        '7': consts.DOWN,
}
consts.UP_LUT = {
        'F': consts.RIGHT,
        '|': consts.UP,
        '7': consts.LEFT,
}
consts.DOWN_LUT = {
        'L': consts.RIGHT,
        '|': consts.DOWN,
        'J': consts.LEFT,
}
consts.LEFT_LUT = {
        '-': consts.LEFT,
        'L': consts.UP,
        'F': consts.DOWN,
}

consts.DIR_LUT = {
        consts.UP: consts.UP_LUT,
        consts.DOWN: consts.DOWN_LUT,
        consts.RIGHT: consts.RIGHT_LUT,
        consts.LEFT: consts.LEFT_LUT
}


class Cursor:

    def __init__(self, board: Board, dir: int,  x: int = 0, y: int = 0):
        self.x = x
        self.y = y
        self.board = board
        self.dir = dir
        self.lut = consts.DIR_LUT[self.dir]
        self.move_count = 0
        self.path = []

    def move(self):
        nx = self.x
        ny = self.y
        match self.dir:
            case consts.UP:
                ny -= 1
            case consts.DOWN:
                ny += 1
            case consts.RIGHT:
                nx += 1
            case consts.LEFT:
                nx -= 1
        self.x = nx
        self.y = ny
        self.path.append((self.x, self.y))

        tile = self.board.tile_at(self.x, self.y)
        if tile != 'S':
            self.dir = self.lut[tile]
            self.lut = consts.DIR_LUT[self.dir]
        self.move_count += 1


class Day10Part1:

    def run(self, input) -> int:
        board = Board([line for line in input])
        cursor = None
        if self.valid_connection(consts.UP, board.tile_at(board.start[0], board.start[1] - 1)):
            cursor = Cursor(board, consts.UP, board.start[0], board.start[1])
        elif self.valid_connection(consts.DOWN, board.tile_at(board.start[0], board.start[1]+ 1)):
            cursor = Cursor(board, consts.DOWN, board.start[0], board.start[1])
        elif self.valid_connection(consts.LEFT, board.tile_at(board.start[0] - 1, board.start[1])):
            cursors = Cursor(board, consts.LEFT, board.start[0], board.start[1])
        elif len(cursors) < 2 and self.valid_connection(consts.RIGHT, board.tile_at(board.start[0] + 1, board.start[1])):
            cursor = Cursor(board, consts.RIGHT, board.start[0], board.start[1])
        else:
            raise Exception(f"Valid connection not found")

        while True:
            cursor.move()
            if board.start[0] == cursor.x and board.start[1] == cursor.y:
                break

        return math.ceil(cursor.move_count/2)

    def valid_connection(self, dir: int, tile: str) -> bool:
        return tile in consts.DIR_LUT[dir]


class Day10Part2:

    def run(self, input) -> int:
        board = Board([line for line in input])
        cursor = None

        if self.valid_connection(consts.UP, board.tile_at(board.start[0], board.start[1] - 1)):
            cursor = Cursor(board, consts.UP, board.start[0], board.start[1])
        elif self.valid_connection(consts.DOWN, board.tile_at(board.start[0], board.start[1]+ 1)):
            cursor = Cursor(board, consts.DOWN, board.start[0], board.start[1])
        elif self.valid_connection(consts.LEFT, board.tile_at(board.start[0] - 1, board.start[1])):
            cursor = Cursor(board, consts.LEFT, board.start[0], board.start[1])
        else:
            cursor = Cursor(board, consts.RIGHT, board.start[0], board.start[1])

        while True:
            cursor.move()
            if board.start[0] == cursor.x and board.start[1] == cursor.y:
                break

        area = self.calc_area(cursor)
        boundary_points = len(cursor.path)
        inside = area - boundary_points/2 + 1
        return inside

    def calc_area(self, cursor: Cursor) -> int:
        vp = cursor.path

        area = 0
        for i in range(len(vp)):
            j = (i + 1) % len(vp)

            area += vp[i][0] * vp[j][1]
            area -= vp[j][0] * vp[i][1]

        area /= 2
        return area if area >= 0 else -area




    def valid_connection(self, dir: int, tile: str) -> bool:
        return tile in consts.DIR_LUT[dir]
