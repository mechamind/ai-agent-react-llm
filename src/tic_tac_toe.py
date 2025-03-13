class TicTacToe:
    def __init__(self):
        """Initialize an empty 3x3 Tic-Tac-Toe board."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        """Prints the board in a readable format."""
        for row in self.board:
            print(" | ".join(row))
        print("\n")

    def make_move(self, row: int, col: int):
        """Places a move if the cell is empty and switches the player."""
        if self.board[row][col] != " ":
            return False  # Invalid move

        self.board[row][col] = self.current_player
        self.current_player = "O" if self.current_player == "X" else "X"
        return True  # Valid move

    def check_winner(self):
        """Checks if there is a winner after the last move."""
        for i in range(3):
            # **Check Row**
            if self.board[i][0] != " " and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]  # Winner found in row

            # **Check Column**
            if self.board[0][i] != " " and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]  # Winner found in column

        # **Check Diagonal (Top-Left to Bottom-Right)**
        if self.board[0][0] != " " and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]

        # **Check Diagonal (Top-Right to Bottom-Left)**
        if self.board[0][2] != " " and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return None  # No winner yet

    def is_draw(self):
        """Checks if the board is full (draw)."""
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def reset_board(self):
        """Resets the board for a new game."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
