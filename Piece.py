from Board import *


class Piece:
    def __init__(self, name, side):
        self.name = name
        self.side = side
        self.loc = None

    def __str__(self):
        if self.side == "Black":
            return "b"
        elif self.side == "White":
            return "w"


class King(Piece):
    def __init__(self, side):
        super().__init__("King", side)

    def __str__(self):
        return "K" + super().__str__()

    def moves(self):
        moves = []
        for i in range(max(0, self.loc.column - 1), min(8, self.loc.column + 2)):
            for j in range(max(0, self.loc.row - 1), min(8, self.loc.row + 2)):
                coord = Coordinate.create_from_number(i, j)
                if not coord.equals(self.loc):
                    moves.append(coord)
        return moves


class Queen(Piece):
    def __init__(self, side):
        super().__init__("Queen", side)

    def __str__(self):
        return "Q" + super().__str__()

    def moves(self):
        moves = []
        for i in range(0, 7):
            coord = Coordinate.create_from_number(i, self.loc.row)
            if not coord.equals(self.loc):
                moves.append(coord)
            coord = Coordinate.create_from_number(self.loc.column, i)
            if not coord.equals(self.loc):
                moves.append(coord)

        for i in range(-7, 8):
            coord = Coordinate.create_from_number(self.loc.column + i, self.loc.row + i)
            if coord and not coord.equals(self.loc):
                moves.append(coord)
            coord = Coordinate.create_from_number(self.loc.column - i, self.loc.row + i)
            if coord and not coord.equals(self.loc):
                moves.append(coord)

        return moves


class Rook(Piece):
    def __init__(self, side):
        super().__init__("Rook", side)

    def __str__(self):
        return "R" + super().__str__()

    def moves(self):
        moves = []
        for i in range(0, 7):
            coord = Coordinate.create_from_number(i, self.loc.row)
            if not coord.equals(self.loc):
                moves.append(coord)
            coord = Coordinate.create_from_number(self.loc.column, i)
            if not coord.equals(self.loc):
                moves.append(coord)
        return moves


class Knight(Piece):
    def __init__(self, side):
        super().__init__("Knight", side)

    def __str__(self):
        return "N" + super().__str__()

    def moves(self):
        moves = []

        coord = Coordinate.create_from_number(self.loc.column + 1, self.loc.row + 2)
        if coord:
            moves.append(coord)
        coord = Coordinate.create_from_number(self.loc.column + 2, self.loc.row + 1)
        if coord:
            moves.append(coord)
        coord = Coordinate.create_from_number(self.loc.column - 1, self.loc.row + 2)
        if coord:
            moves.append(coord)
        coord = Coordinate.create_from_number(self.loc.column - 2, self.loc.row + 1)
        if coord:
            moves.append(coord)

        coord = Coordinate.create_from_number(self.loc.column + 1, self.loc.row - 2)
        if coord:
            moves.append(coord)
        coord = Coordinate.create_from_number(self.loc.column + 2, self.loc.row - 1)
        if coord:
            moves.append(coord)
        coord = Coordinate.create_from_number(self.loc.column - 1, self.loc.row - 2)
        if coord:
            moves.append(coord)
        coord = Coordinate.create_from_number(self.loc.column - 2, self.loc.row - 1)
        if coord:
            moves.append(coord)

        return moves

class Bishop(Piece):
    def __init__(self, side):
        super().__init__("Bishop", side)

    def __str__(self):
        return "B" + super().__str__()

    def moves(self):
        moves = []

        for i in range(-7, 8):
            coord = Coordinate.create_from_number(self.loc.column + i, self.loc.row + i)
            if coord and not coord.equals(self.loc):
                moves.append(coord)
            coord = Coordinate.create_from_number(self.loc.column - i, self.loc.row + i)
            if coord and not coord.equals(self.loc):
                moves.append(coord)

        return moves


class Pawn(Piece):
    def __init__(self, side):
        super().__init__("Pawn", side)

    def __str__(self):
        return "P" + super().__str__()

    def moves(self):
        pass
