import datetime

import wikipedia

from common import Tool, Agent


def perform_calculator(operation:str, a, b):
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        return a / b
    if operation == "sqare":
        return a**2
    if operation == "cube":
        return a**3  
    return "Invalid operation"

def search_wikipedia(search_query:str):
    try:
        page = wikipedia.page(search_query)
        text = page.content
    except Exception as e:
        return ("Could not find any information on wikipedia for the search query: "
                + search_query + ". Please try another search term")
    return text[:300]

def date_of_today():
    return datetime.date.today()

people_search_agent = Agent(
    name="People_search_Agent",
    instructions=f"""You are a helpful assistant that help to find people information on the Wikipedia using its name.""",
)

calculator_tool = Tool("Calculator", perform_calculator, "To perform math calculations")
wikipedia_tool = Tool("Wikipedia_search", search_wikipedia, "To search for information on wikipedia")
today_tool = Tool("Date_of_today", date_of_today, "To get the date of today")
people_search_tool = Tool("People_search", people_search_agent, "To search for person information")
people_search_agent.functions = [wikipedia_tool]

import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.full((3, 3), " ")  # 3x3 grid filled with spaces
        self.current_player = "X"  # Player X starts

    def display_board(self):
        return "\n".join([" | ".join(row) for row in self.board])

    def make_move(self, row: int, col: int):
        """Handles a move for the current player."""
        if self.board[row, col] != " ":
            return f"Invalid move! Cell ({row},{col}) is already occupied."
        
        self.board[row, col] = self.current_player
        if self.check_winner():
            winner = self.current_player
            self.reset_board()
            return f"Player {winner} wins! Game reset."
        
        if self.is_draw():
            self.reset_board()
            return "It's a draw! Game reset."
        
        # Switch player
        self.current_player = "O" if self.current_player == "X" else "X"
        return self.display_board()

    def check_winner(self):
        """Checks if a player has won."""
        for i in range(3):
            if all(self.board[i, :] == self.current_player):  # Row check
                return True
            if all(self.board[:, i] == self.current_player):  # Column check
                return True
        if all(np.diag(self.board) == self.current_player):  # Main diagonal
            return True
        if all(np.diag(np.fliplr(self.board)) == self.current_player):  # Other diagonal
            return True
        return False

    def is_draw(self):
        """Checks if the game is a draw (board full, no winners)."""
        return np.all(self.board != " ")

    def reset_board(self):
        """Resets the board after a game ends."""
        self.board = np.full((3, 3), " ")
        self.current_player = "X"

# Create a global Tic-Tac-Toe instance
tic_tac_toe_game = TicTacToe()

# Tool function to handle Tic-Tac-Toe moves
def tic_tac_toe_tool(row: int, col: int):
    return tic_tac_toe_game.make_move(row, col)

# Register the tool
tic_tac_toe_tool = Tool("TicTacToe", tic_tac_toe_tool, "Play a turn in a Tic-Tac-Toe game.")


