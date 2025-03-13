from tic_tac_toe import TicTacToe
from ai_agent import AIAgent
import json

# Initialize the game and AI players
game = TicTacToe()
ai_x = AIAgent("Agent X", "X")
ai_o = AIAgent("Agent O", "O")

print("AI vs AI Tic-Tac-Toe - Starting Game!\n")
game.display_board()

for turn in range(9):  # Max 9 moves
    current_agent = ai_x if turn % 2 == 0 else ai_o
    print(f"{current_agent.name} ({current_agent.symbol}) is thinking...")

    # AI selects a move
    move_json = current_agent.choose_move(game)
    move = json.loads(move_json)  # Parse move

    if "error" in move:
        print(move["error"])
        break

    row, col = move["row"], move["col"]
    game.make_move(row, col)  # Apply move
    game.display_board()

    # Check for winner
    winner = game.check_winner()
    if winner:
        print(f"🎉 {current_agent.name} wins! Game Over!")
        break

    # Check for draw
    if game.is_draw():
        print("😲 It's a draw! Game Over!")
        break
