from pieces import Pawn, Rook, Bishop, Knight, King, Queen
class Board:
    def __init__(self):
        # Create an 8x8 chessboard
        self.board = [
            [Rook('white'), Knight('white'), Bishop('white'), Queen('white'),
             King('white'), Bishop('white'), Knight('white'), Rook('white')],
            [Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'),
             Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white')],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'),
             Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black')],
            [Rook('black'), Knight('black'), Bishop('black'), Queen('black'),
             King('black'), Bishop('black'), Knight('black'), Rook('black')]
        ]

    def display(self):
        # Print the chessboard to the console
        for row in self.board:
            row_str = ''
            for piece in row:
                if piece is None:
                    row_str += '  '
                else:
                    row_str += piece.get_symbol() + ' '
            print(row_str)

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        destination_piece = self.board[end_row][end_col]

        if piece is None:
            print("No piece at the start position!")
        elif destination_piece is not None and destination_piece.color == piece.color:
            print("Destination square is occupied by a piece of the same color!")
        elif piece.validate_move(start_row, start_col, end_row, end_col):
            if destination_piece is not None and destination_piece.color != piece.color:
                self.capture_piece(end_row, end_col)
                
            self.board[start_row][start_col] = None
            self.board[end_row][end_col] = piece
            piece.has_moved = True
        else:
            print("Invalid move!")

    def capture_piece(self, row, col):
        captured_piece = self.board[row][col]
        captured_piece_color = captured_piece.color

        self.board[row][col] = None
        print(f"Captured {captured_piece_color} {type(captured_piece).__name__}!")
    

myB = Board()
myB.display()
myB.move_piece(1,4,3,4)
myB.move_piece(6,4,4,4)
myB.move_piece(0,3,2,5)
myB.move_piece(2,5,6,5)





myB.display()