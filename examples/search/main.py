import os
from openai import OpenAI
from common import Agent, AgentConfig
from reactexecutor import ReActExecutor
from tools import people_search_tool, calculator_tool, tic_tac_toe_tool

open_ai = OpenAI(base_url="http://192.168.1.114:1234/v1", api_key="lm-studio")
main_agent = Agent(
    name= "Agent",
    model = "deepseek-r1-distill-llama-8b",
    instructions = """You are a helpful assistant that asists the user in completing a task using multiple tools.""",
    # functions=[people_search_tool, calculator_tool, tic_tac_toe_tool],
    functions=[tic_tac_toe_tool]
)



# if __name__ == "__main__":
#     query = "What is the double of six and triple of 7 and square of 3 and cube of number you got from one plus square of 2?"
#     agent_config = AgentConfig()
#     agent_config.with_model_client(open_ai)
#     agent_config.with_token_limit(5000)
#     agent_config.with_max_interactions(10)
#     react_exec = ReActExecutor(agent_config, main_agent)
#     react_exec.execute(query)

if __name__ == "__main__":
    print("Welcome to AI-powered Tic-Tac-Toe!")

    agent_config = AgentConfig()
    agent_config.with_model_client(open_ai)
    agent_config.with_token_limit(5000)
    agent_config.with_max_interactions(10)

    react_exec = ReActExecutor(agent_config, main_agent)  # Initialize ReActExecutor

    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input! Please enter numbers between 0 and 2.")
                continue

            # Convert user input into a natural language query for the agent
            query = f"Play Tic-Tac-Toe and place a move at row {row}, column {col}."
            result = react_exec.execute(query)  # Call AI agent to process query

            print(result)

            if "wins" in result or "draw" in result:
                print("Game over! Restarting...")
                break  # Exit on game over

        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 2.")

