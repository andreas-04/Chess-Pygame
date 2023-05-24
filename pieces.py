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

        # Check for obstacle in front of the pawn
        if col_diff == 0 and row_diff == direction:
            # Check if the destination square is occupied
            if self.board[end_row][end_col] is None:
                return True

        # Check for obstacle in the initial double-step move
        if col_diff == 0 and (1 <= row_diff <= 2) and row_diff == direction:
            # Check if the intermediate square is unoccupied
            if self.board[start_row + direction][start_col] is None:
                # Check if the destination square is unoccupied
                if self.board[end_row][end_col] is None:
                    return True

        return False

    def get_symbol(self):
        return '♙' if self.color == 'white' else '♟'

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
    def validate_move(self, start_row, start_col, end_row, end_col):
        if ((start_row == end_row) and (start_col != end_col)) or ((start_col == end_col) and (start_row != end_row)):
            # Check for obstacles in the path
            if start_row == end_row:  # Horizontal movement
                min_col = min(start_col, end_col)
                max_col = max(start_col, end_col)
                for col in range(min_col + 1, max_col):
                    if self.board[start_row][col] is not None:
                        return False
            else:  # Vertical movement
                min_row = min(start_row, end_row)
                max_row = max(start_row, end_row)
                for row in range(min_row + 1, max_row):
                    if self.board[row][start_col] is not None:
                        return False

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
        row_diff = end_row - start_row
        col_diff = end_col - start_col

        # Check if the movement is diagonal
        if abs(row_diff) == abs(col_diff):
            # Determine the direction of movement
            row_direction = 1 if row_diff > 0 else -1
            col_direction = 1 if col_diff > 0 else -1

            # Check for obstacles in the path
            current_row = start_row + row_direction
            current_col = start_col + col_direction
            while current_row != end_row and current_col != end_col:
                if self.board[current_row][current_col] is not None:
                    return False
                current_row += row_direction
                current_col += col_direction

            return True

        return False
    def get_symbol(self):
            return '♗' if self.color == 'white' else '♝'
    
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
    def validate_move(self, start_row, start_col, end_row, end_col):
        row_diff = end_row - start_row
        col_diff = end_col - start_col

        # Check if the movement is horizontal, vertical, or diagonal
        if (start_row == end_row) or (start_col == end_col) or (abs(row_diff) == abs(col_diff)):
            # Determine the direction of movement
            row_direction = 0 if start_row == end_row else (1 if row_diff > 0 else -1)
            col_direction = 0 if start_col == end_col else (1 if col_diff > 0 else -1)

            # Check for obstacles in the path
            current_row = start_row + row_direction
            current_col = start_col + col_direction
            while current_row != end_row or current_col != end_col:
                if self.board[current_row][current_col] is not None:
                    return False
                current_row += row_direction
                current_col += col_direction

            return True

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
