from tic_tac_toe import TicTacToe

# Initialize the game
game = TicTacToe()

# Play a few moves manually
print("Starting Tic-Tac-Toe Game:")
game.display_board()

moves = [(0, 0), (1, 1), (0, 1), (2, 2), (0, 2)]  # Sample moves

for move in moves:
    row, col = move
    if game.make_move(row, col):
        print(f"Player {game.current_player} made a move at ({row}, {col})")
        game.display_board()
    else:
        print(f"Invalid move at ({row}, {col})! Try again.")

    # Check winner
    winner = game.check_winner()
    if winner:
        print(f"🎉 Player {winner} wins! Game Over!")
        break

    # Check for draw
    if game.is_draw():
        print("😲 It's a draw! Game Over!")
        break
