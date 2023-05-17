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


white_pawn = Pawn("white")
print(white_pawn.validate_move(1, 2, 2, 2))  # True
print(white_pawn.validate_move(2, 2, 3, 2))  # True
print(white_pawn.validate_move(3, 2, 4, 2))  # False
# class Rook(Piece):
#     def __init__(self, color):
#         super().__init__(color)

# class Knight(Piece):
#     def __init__(self, color):
#         super().__init__(color)

# class Bishop(Piece):
#     def __init__(self, color):
#         super().__init__(color)
# class Queen(Piece):
#     def __init__(self, color):
#         super().__init__(color)
# class King(Piece):
#     def __init__(self, color):
#         super().__init__(color)