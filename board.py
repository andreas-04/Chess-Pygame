from pieces import Pawn, Rook, Bishop, Knight, King, Queen
class Board:
    def __init__(self):
        # Create an 8x8 chessboard
        self.board = [
            [Rook('black'), Knight('black'), Bishop('black'), Queen('black'),
             King('black'), Bishop('black'), Knight('black'), Rook('black')],
            [Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'),
             Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black')],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'),
             Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white')],
            [Rook('white'), Knight('white'), Bishop('white'), Queen('white'),
             King('white'), Bishop('white'), Knight('white'), Rook('white')]
            
        ]

    def display(self):
        print("   A B C D E F G H")
        print("  -----------------")
        for row in range(8):
            print(f"{row+1} |", end="")
            for col in range(8):
                piece = self.board[row][col]
                if piece is None:
                    print("  ", end="")
                else:
                    print(piece.get_symbol(), end=" ")
            print("|")
        print("  -----------------")

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        destination_piece = self.board[end_row][end_col]

        if piece is None:
            print("No piece at the start position!")
            return
        elif destination_piece is not None and destination_piece.color == piece.color:
            print("Destination square is occupied by a piece of the same color!")
            return
        elif not piece.validate_move(start_row, start_col, end_row, end_col):
            print("Invalid move!")
            return

        # Check if the current player's king is in check
        current_player = piece.color
        if self.is_king_in_check(current_player):
            print(f"{current_player.capitalize()} King is in check! Cannot make the move.")
            return

        self.board[start_row][start_col] = None
        self.board[end_row][end_col] = piece
        piece.has_moved = True

        # Check if the opponent's king is in check after the move
        opponent_color = "white" if current_player == "black" else "black"
        if self.is_king_in_check(opponent_color):
            print(f"{opponent_color.capitalize()} King is in check!")

    def capture_piece(self, row, col):
        captured_piece = self.board[row][col]
        captured_piece_color = captured_piece.color
        self.board[row][col] = None
        print(f"Captured {captured_piece_color} {type(captured_piece).__name__}!")

    def is_king_in_check(self, color):
        # Find the position of the king on the board
        king_position = None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King) and piece.color == color:
                    king_position = (row, col)
                    break
            if king_position:
                break

        # Check if any opponent piece has a valid move to capture the king
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.color != color:
                    if piece.validate_move(row, col, king_position[0], king_position[1]):
                        print(f"{piece.color.capitalize()} {type(piece).__name__} is checking the {color.capitalize()} King!")
                        return True

        return False
# myB = Board()
# myB.display()
# myB.move_piece(1,4,3,4)
# print("M1")
# myB.move_piece(0,3,2,5)
# myB.move_piece(2,5,6,5)
# myB.move_piece(6,4,5,4)




