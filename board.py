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
        # Get the piece at the start position
        piece = self.board[start_row][start_col]

        if piece is not None:
            
            # Check if the move is valid using the piece's validate_move method
            if piece.validate_move(start_row, start_col, end_row, end_col):
                # Move the piece
                self.board[start_row][start_col] = None
                self.board[end_row][end_col] = piece
            else:
                print("Invalid move!")
        else:
            print("No piece at the start position!")

myB = Board()
myB.display()
myB.move_piece(1,4,2,4)
myB.display()