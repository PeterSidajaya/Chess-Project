class Coordinate:
    dic = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
    }
    reverse_dic = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h",
    }

    def __init__(self, column, row):
        self.string = column + str(row)
        self.row = row - 1
        self.column = Coordinate.dic[column]

    def __str__(self):
        return self.string

    def equals(self, coord):
        if (self.row == coord.row) and (self.column == coord.column):
            return True
        else:
            return False

    @classmethod
    def create_from_number(cls, column, row):
        if column < 0 or column > 7:
            return None
        elif row < 0 or row > 7:
            return None
        else:
            return Coordinate(Coordinate.reverse_dic[column], row + 1)


class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append([None, None, None, None, None, None, None, None])

    def add(self, piece, loc):
        self.board[loc.row][loc.column] = piece

    def remove(self, loc):
        self.board[loc.row][loc.column] = None

    def find(self, loc):
        return self.board[loc.row][loc.column]

    def __str__(self):
        ret = ""
        for i in range(7, -1, -1):
            for j in range(8):
                if not(self.board[i][j]):
                    ret += " X  "
                else:
                    ret += " {} ".format(self.board[i][j].__str__())
            ret += "\n"
        return ret
