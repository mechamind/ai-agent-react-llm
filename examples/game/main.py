from tic_tac_toe import TicTacToe
from ai_agent import AIAgent
from reactexecutor import ReActExecutor

# Initialize game and AI agents
game = TicTacToe()
agent_x = AIAgent("Agent X", "X")
agent_o = AIAgent("Agent O", "O")

# Start ReAct execution
react_executor = ReActExecutor(agent_x, agent_o, game)
react_executor.execute()
