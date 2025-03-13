from typing import List, Callable, Union
from openai import OpenAI
from pydantic import BaseModel, Field

class ToolChoice(BaseModel):
    """Data model for choosing a tool in ReAct logic."""
    tool_name: str = Field(..., description="Name of the tool to use")
    reason_of_choice: str = Field(..., description="Reason for choosing the tool")

class ReactEnd(BaseModel):
    """Data model for the observation step."""
    stop: bool = Field(..., description="True if the game is over, else False")
    final_answer: str = Field(..., description="Final answer if the game is over")
    confidence: float = Field(..., description="Confidence score of the final answer")

class Tool:
    """Defines a tool that the AI agent can use."""
    def __init__(self, name: str, func: Callable, desc: str) -> None:
        self.name = name
        self.func = func
        self.desc = desc

class Agent(BaseModel):
    """Defines an AI Agent that plays Tic-Tac-Toe using ReAct logic."""
    name: str
    model: str
    instructions: str
    functions: List[Tool]

class AgentConfig:
    """Configuration settings for AI execution."""
    def __init__(self):
        self.max_interactions = 10
        self.model = None
        self.token_limit: int = 5000

    def with_model_client(self, model: OpenAI):
        self.model = model
        return self

    def with_token_limit(self, token_limit: int):
        self.token_limit = token_limit
        return self

    def with_max_interactions(self, max_int: int):
        self.max_interactions = max_int
        return self
