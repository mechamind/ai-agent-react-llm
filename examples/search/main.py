import os
import json
import random
from openai import OpenAI
from common import Agent, AgentConfig
from reactexecutor import ReActExecutor
from tic_tac_toe import tic_tac_toe_tool, game
from brain import Brain  # Import Brain

# Initialize OpenAI client
open_ai = OpenAI(base_url="http://192.168.1.114:1234/v1", api_key="lm-studio")

# Initialize Brain memory
brain = Brain(AgentConfig())

# Create Two AI Agents (X and O)
agent_x = Agent(
    name="Agent X",
    model="deepseek-r1-distill-llama-8b",
    instructions="""You are Agent X. You play Tic-Tac-Toe as 'X'.
    You must play **one move at a time**. Always check the board state before making a move.
    Respond in **valid JSON format**:
    {"row": 1, "col": 1}
    """,
    functions=[tic_tac_toe_tool]
)

agent_o = Agent(
    name="Agent O",
    model="deepseek-r1-distill-llama-8b",
    instructions="""You are Agent O. You play Tic-Tac-Toe as 'O'.
    You must play **one move at a time**. Always check the board state before making a move.
    Respond in **valid JSON format**:
    {"row": 1, "col": 1}
    """,
    functions=[tic_tac_toe_tool]
)

# Configure AI execution settings
agent_config = AgentConfig()
agent_config.with_model_client(open_ai)
agent_config.with_token_limit(5000)
agent_config.with_max_interactions(10)

# Initialize ReAct Executors for both agents
react_exec_x = ReActExecutor(agent_config, agent_x)
react_exec_o = ReActExecutor(agent_config, agent_o)

print("AI vs AI Tic-Tac-Toe - Starting Game!")

# Store the initial board state in memory
brain.remember(json.dumps({"board": game.board}))

# AI Agents take turns playing
for turn in range(9):  # Max 9 moves in Tic-Tac-Toe
    current_agent = react_exec_x if turn % 2 == 0 else react_exec_o  # X plays on even turns, O on odd
    agent_name = "X" if turn % 2 == 0 else "O"

    # Get the latest board state
    current_board = json.loads(brain.recall())["board"]

    # AI decides the move based on the board state and memory
    query = f"""
    The current Tic-Tac-Toe board state is:
    {json.dumps(current_board)}

    Past moves:
    {brain.recall()}

    Your mark is '{agent_name}'. Play a valid move (row, column) where the cell is EMPTY.
    Return only the move in JSON format: {{"row": 1, "col": 1}}
    """

    result = current_agent.execute(query)

    # Parse AI output
    try:
        move = json.loads(result.strip())  # Convert AI response to dictionary
        row, col = move["row"], move["col"]
    except Exception as e:
        print(f"⚠️ Error parsing AI output: {e}")
        print(f"Invalid response: {result}")
        break  # Exit if AI gives malformed output

    # Apply the move in Tic-Tac-Toe
    move_result = json.loads(tic_tac_toe_tool.func(row, col))

    # Store the new board state in Brain memory
    brain.remember(json.dumps({"board": move_result["board"]}))

    # Print board and results
    print(f"\nAgent {agent_name} played at ({row}, {col}):")
    for row in move_result["board"]:
        print(" | ".join(row))
    print("\n")

    # Check for winner or draw
    if "winner" in move_result:
        if move_result["winner"] == "Draw":
            print("\n😲 It's a draw! Game Over!\n")
        else:
            print(f"\n🎉 Player {move_result['winner']} wins! Game Over!\n")
        break
