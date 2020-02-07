from Piece import*


class Game:
    def __init__(self):
        self.board = Board()

        self.add_piece(King("White"), Coordinate("e", 1))
        self.add_piece(Queen("White"), Coordinate("d", 1))
        self.add_piece(Bishop("White"), Coordinate("c", 1))
        self.add_piece(Bishop("White"), Coordinate("f", 1))
        self.add_piece(Knight("White"), Coordinate("b", 1))
        self.add_piece(Knight("White"), Coordinate("g", 1))
        self.add_piece(Rook("White"), Coordinate("a", 1))
        self.add_piece(Rook("White"), Coordinate("h", 1))
        for i in ("a", "b", "c", "d", "e", "f", "g", "h"):
            self.add_piece(Pawn("White"), Coordinate(i, 2))

        self.add_piece(King("Black"), Coordinate("e", 8))
        self.add_piece(Queen("Black"), Coordinate("d", 8))
        self.add_piece(Bishop("Black"), Coordinate("c", 8))
        self.add_piece(Bishop("Black"), Coordinate("f", 8))
        self.add_piece(Knight("Black"), Coordinate("b", 8))
        self.add_piece(Knight("Black"), Coordinate("g", 8))
        self.add_piece(Rook("Black"), Coordinate("a", 8))
        self.add_piece(Rook("Black"), Coordinate("h", 8))
        for i in ("a", "b", "c", "d", "e", "f", "g", "h"):
            self.add_piece(Pawn("Black"), Coordinate(i, 7))

    def move_piece(self, start_loc, end_loc):
        def check_legal_move(piece1, piece2, start, end):
            if piece1.side == piece2.side:
                return False

        start_piece = self.board.find(start_loc)
        if not start_piece:
            print("No piece at the location!")
        target_piece = self.board.find(end_loc)
        if check_legal_move(start_piece, target_piece, start_loc, end_loc):
            self.board.remove(start_loc)
            if target_piece:
                self.board.remove(end_loc)
            self.add_piece(start_piece, end_loc)
        else:
            print("Illegal move!")

    def add_piece(self, piece, loc):
        piece.loc = loc
        self.board.add(piece, loc)

    def remove_piece(self, loc):
        piece = self.board.find(loc)
        piece.loc = None
        self.board.remove(loc)

    def select_piece(self, loc):
        return self.board.find(loc)


if __name__ == "__main__":
    root = Game()
    print(root.board)
    for i in root.select_piece(Coordinate("c", 1)).moves():
        print(i)