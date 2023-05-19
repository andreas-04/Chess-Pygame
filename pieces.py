class Piece:
    def __init__(self, color):
        self.color = color

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.has_moved = False
    def validate_move(self, start_row, start_col, end_row, end_col):
        direction = 1 if self.color == "white" else -1
        row_diff = end_row - start_row
        col_diff = abs(end_col - start_col)

        if self.has_moved:
            if col_diff == 0 and row_diff == direction:
                return True
        else:
            if col_diff == 0 and (1 <= row_diff <= 2) and row_diff == direction:
                return True

        return False
    def get_symbol(self):
        return '♙' if self.color == 'white' else '♟'

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
    def validate_move(self, start_row, start_col, end_row, end_col):
        if (start_row == end_row and start_col != end_col) or (start_col == end_col and start_row != end_row):
             return True
        return False
    def get_symbol(self):
        return '♖' if self.color == 'white' else '♜'


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
    def validate_move(self, start_row, start_col, end_row, end_col):
        row_offset = abs(start_row - end_row)
        col_offset = abs(start_col - end_col)
        if (row_offset == 2 and col_offset == 1) or (row_offset == 1 and col_offset == 2):
                return True
        else:
            return False
    def get_symbol(self):
            return '♘' if self.color == 'white' else '♞'

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
    def validate_move(self, start_row, start_col, end_row, end_col):
        row_offset = abs(start_row - end_row)
        col_offset = abs(start_col - end_col)

        # A valid bishop move consists of moving an equal number of squares diagonally in both
        # the row and column directions.
        if row_offset == col_offset:
            return True
        else:
            return False
    def get_symbol(self):
            return '♗' if self.color == 'white' else '♝'
    
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
    def validate_move(self, start_row, start_col, end_row, end_col):
        row_offset = abs(start_row - end_row)
        col_offset = abs(start_col - end_col)

        # A valid queen move consists of moving either horizontally (in a straight line),
        # vertically (in a straight line), or diagonally (in a straight line).
        if (start_row == end_row and start_col != end_col) or (start_col == end_col and start_row != end_row) or (row_offset == col_offset): 
            return True
        else:
            return False
    def get_symbol(self):
            return '♕' if self.color == 'white' else '♛'

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
    def validate_move(self, start_row, start_col, end_row, end_col):
        row_offset = abs(start_row - end_row)
        col_offset = abs(start_col - end_col)
        if (row_offset <= 1) and (col_offset <= 1):
            return True
        else:
            return False
    def get_symbol(self):
            return '♔' if self.color == 'white' else '♚'
