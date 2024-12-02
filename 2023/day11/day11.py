
class SpaceImage:

    def __init__(self, rows: list[str]):
        EMPTY_ROW = '.' * len(rows[0])
        self.row_map = dict()
        self.col_map = dict()
        self.galaxies = []

        for i in range(len(rows[0])):
            self.col_map[i] = False

        for r in range(len(rows)):
            row = rows[r]
            self.row_map[r] = row != EMPTY_ROW
            for c in range(len(row)):
                col = row[c]
                if col == '#':
                    self.galaxies.append((c, r))
                    self.col_map[c] = True

    def row_has_galaxy(self, row: int) -> bool:
        return self.row_map[row]

    def col_has_galaxy(self, col: int) -> bool:
        return self.col_map[col]



class Day11Part1:

    def run(self, input):
        spaceimg = SpaceImage(input)

        total_distance = 0
        num_galaxies = len(spaceimg.galaxies)
        for i in range(num_galaxies):
            start = spaceimg.galaxies[i]
            for j in range(i + 1, num_galaxies):
                end = spaceimg.galaxies[j]

                sc = start[0]
                ec = end[0]
                distance = 0
                for c in range(sc, ec, 1 if sc <= ec else -1):
                    distance += 1 if spaceimg.col_has_galaxy(c) else 2

                sr = start[1]
                er = end[1]
                for r in range(sr, er, 1 if sr <= er else -1):
                    distance += 1 if spaceimg.row_has_galaxy(r) else 2
                total_distance += distance

        return total_distance


class Day11Part2:

    def run(self, input):
        spaceimg = SpaceImage(input)

        total_distance = 0
        num_galaxies = len(spaceimg.galaxies)
        for i in range(num_galaxies):
            start = spaceimg.galaxies[i]
            for j in range(i + 1, num_galaxies):
                end = spaceimg.galaxies[j]

                sc = start[0]
                ec = end[0]
                distance = 0
                for c in range(sc, ec, 1 if sc <= ec else -1):
                    distance += 1 if spaceimg.col_has_galaxy(c) else 1000000

                sr = start[1]
                er = end[1]
                for r in range(sr, er, 1 if sr <= er else -1):
                    distance += 1 if spaceimg.row_has_galaxy(r) else 1000000
                total_distance += distance

        return total_distance
