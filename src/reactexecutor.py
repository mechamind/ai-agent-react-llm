import json
from tic_tac_toe import TicTacToe
from ai_agent import AIAgent

class ReActExecutor:
    def __init__(self, agent_x: AIAgent, agent_o: AIAgent, game: TicTacToe):
        """Initialize ReAct logic with AI agents and game."""
        self.agent_x = agent_x
        self.agent_o = agent_o
        self.game = game
        self.memory = []  # Store past moves for reasoning

    def remember(self, message: str):
        """Store game state in memory."""
        self.memory.append(message)

    def recall(self):
        """Return past moves as memory context."""
        return "\n".join(self.memory)

    def execute(self):
        """Runs the game with ReAct logic."""
        print("AI vs AI Tic-Tac-Toe - ReAct Mode\n")
        self.game.display_board()

        for turn in range(9):  # Max 9 moves
            current_agent = self.agent_x if turn % 2 == 0 else self.agent_o
            print(f"{current_agent.name} ({current_agent.symbol}) is thinking...")

            # AI decides the move based on board state and past moves
            query = f"""
            The current Tic-Tac-Toe board state is:
            {json.dumps(self.game.board)}

            Past moves:
            {self.recall()}

            Your mark is '{current_agent.symbol}'. Play a valid move.
            Return JSON: {{"row": 1, "col": 1}}
            """
            
            move_json = current_agent.choose_move(self.game)  # AI selects move
            move = json.loads(move_json)

            if "error" in move:
                print(move["error"])
                break

            row, col = move["row"], move["col"]
            self.game.make_move(row, col)  # Apply move

            # Store memory for future turns
            self.remember(json.dumps({"player": current_agent.symbol, "move": (row, col)}))

            self.game.display_board()

            # Check for winner
            winner = self.game.check_winner()
            if winner:
                print(f"🎉 {current_agent.name} ({winner}) wins! Game Over!")
                break

            # Check for draw
            if self.game.is_draw():
                print("😲 It's a draw! Game Over!")
                break
