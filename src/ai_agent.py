import json
import random
from tic_tac_toe import TicTacToe

class AIAgent:
    def __init__(self, name, symbol):
        """Initialize AI agent with name and symbol (X or O)."""
        self.name = name
        self.symbol = symbol

    def choose_move(self, game: TicTacToe):
        """AI selects a random available move (for now)."""
        available_moves = [(r, c) for r in range(3) for c in range(3) if game.board[r][c] == " "]

        if not available_moves:
            return json.dumps({"error": "No moves available"})

        move = random.choice(available_moves)  # Pick a random move for now
        return json.dumps({"row": move[0], "col": move[1]})
