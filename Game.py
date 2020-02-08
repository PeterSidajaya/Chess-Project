# Personal Chess project
# v0.0.2
# Author: Peter Sidajaya
# TO-DO: finish check_legal_move to add conditional whether any piece is blocking

from Piece import*


class Game:
    def __init__(self):
        self.board = Board()
        self.finish = False
        self.turn = "White"
        self.check_white = False
        self.check_black = False
        self.pieces = []
        self.White_king = King("White")
        self.Black_king = King("Black")

        self.add_piece(self.White_king, Coordinate("e", 1))
        self.add_piece(Queen("White"), Coordinate("d", 1))
        self.add_piece(Bishop("White"), Coordinate("c", 1))
        self.add_piece(Bishop("White"), Coordinate("f", 1))
        self.add_piece(Knight("White"), Coordinate("b", 1))
        self.add_piece(Knight("White"), Coordinate("g", 1))
        self.add_piece(Rook("White"), Coordinate("a", 1))
        self.add_piece(Rook("White"), Coordinate("h", 1))
        for i in ("a", "b", "c", "d", "e", "f", "g", "h"):
            self.add_piece(Pawn("White"), Coordinate(i, 2))

        self.add_piece(self.Black_king, Coordinate("e", 8))
        self.add_piece(Queen("Black"), Coordinate("d", 8))
        self.add_piece(Bishop("Black"), Coordinate("c", 8))
        self.add_piece(Bishop("Black"), Coordinate("f", 8))
        self.add_piece(Knight("Black"), Coordinate("b", 8))
        self.add_piece(Knight("Black"), Coordinate("g", 8))
        self.add_piece(Rook("Black"), Coordinate("a", 8))
        self.add_piece(Rook("Black"), Coordinate("h", 8))
        for i in ("a", "b", "c", "d", "e", "f", "g", "h"):
            self.add_piece(Pawn("Black"), Coordinate(i, 7))

        # self.add_piece(King("White"), Coordinate("e", 1))
        # self.add_piece(King("Black"), Coordinate("e", 8))
        # self.add_piece(Rook("White"), Coordinate("h", 2))

        self.play()

    def move_piece(self, start_loc, end_loc):
        start_piece = self.board.find(start_loc)
        target_piece = self.board.find(end_loc)
        if self.check_legal_move(start_piece, target_piece, start_loc, end_loc):
            self.board.remove(start_loc)
            if target_piece:
                self.board.remove(end_loc)
            self.add_piece(start_piece, end_loc)
            self.next_turn()

    def check_legal_move(self, piece1, piece2, start, end):
        if not piece1:
            print("No piece")
            return False
        if piece1.side != self.turn:
            print("Not your piece")
            return False
        if piece2:
            if piece1.side == piece2.side:
                print("That's your own piece")
                return False
        for i in piece1.moves():
            if i.equals(end):
                return True
        print("Illegal move")
        return False

    def add_piece(self, piece, loc):
        piece.loc = loc
        self.board.add(piece, loc)
        self.pieces.append(piece)

    def remove_piece(self, loc):
        piece = self.board.find(loc)
        piece.loc = None
        self.board.remove(loc)
        self.pieces.remove(piece)

    def select_piece(self, loc):
        return self.board.find(loc)

    def play(self):
        self.take_input()

    def take_input(self):
        print(self.board)
        input_string = str(input())
        if input_string[0:4] == "move":
            coord1 = Coordinate(input_string[5], int(input_string[6]))
            coord2 = Coordinate(input_string[8], int(input_string[9]))
            self.move_piece(coord1, coord2)

    def next_turn(self):
        check = self.check_for_check()
        if check == "White":
            self.check_white = True
        elif check == "Black":
            self.check_black = True
        if self.turn == "White":
            self.turn = "Black"
            print("Black's turn")
        elif self.turn == "Black":
            self.turn = "White"
            print("White's turn")
        self.take_input()

    def check_for_check(self):
        for piece in self.pieces:
            for move in piece.moves():
                if self.White_king.loc.equals(move):
                    print(piece.loc)
                    if self.check_legal_move(piece, self.White_king, piece.loc, move):
                        print("Check")
                        return "White"
                if self.Black_king.loc.equals(move):
                    print(piece.loc)
                    if self.check_legal_move(piece, self.Black_king, piece.loc, move):
                        print("Check")
                        return "Black"


if __name__ == "__main__":
    root = Game()