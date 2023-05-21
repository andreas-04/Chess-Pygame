from board import Board
class ChessGame:
    def __init__(self):
        self.board = Board()
        self.current_player = "white"

    def play(self):
        while True:
            self.board.display()

            # Check if the current player's king is in check
            if self.board.is_king_in_check(self.current_player):
                print(f"{self.current_player.capitalize()} King is in check!")

            # Get the player's move
            start_row, start_col, end_row, end_col = self.get_player_move()

            # Move the piece
            self.board.move_piece(start_row, start_col, end_row, end_col)

            # Check if the opponent's king is in checkmate
            # opponent_color = "white" if self.current_player == "black" else "black"
            # if self.board.is_king_in_checkmate(opponent_color):
            #     print(f"{opponent_color.capitalize()} King is in checkmate! {self.current_player.capitalize()} wins!")
            #     break

            # Switch to the next player's turn
            self.current_player = "black" if self.current_player == "white" else "white"

    def get_player_move(self):
        # Implement player input to get the move coordinates (start_row, start_col, end_row, end_col)
        # You can use input() or any other method suitable for your game interface
        # Return the move coordinates as integers

        # Example input format: "A2 A4" to move a piece from A2 to A4
        input_str = input(f"{self.current_player.capitalize()}'s turn: Enter your move (e.g., A2 A4): ")
        positions = input_str.split()

        # Convert positions to coordinates (row, col) - Adjust according to your implementation
        start_col = ord(positions[0][0].upper()) - ord('A')
        start_row = int(positions[0][1]) - 1
        end_col = ord(positions[1][0].upper()) - ord('A')
        end_row = int(positions[1][1]) - 1

        return start_row, start_col, end_row, end_col


# Main driver code
if __name__ == "__main__":
    game = ChessGame()
    game.play()
