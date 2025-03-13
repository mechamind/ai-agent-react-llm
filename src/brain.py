import json
from common import AgentConfig

class Brain:
    def __init__(self, config: AgentConfig):
        self.config = config
        self.memory = []  # Stores reasoning and board history

    def remember(self, message: str):
        """Stores information in memory."""
        self.memory.append(message)

    def recall(self):
        """Returns past stored memory as context."""
        return "\n".join(self.memory)

    def think(self, prompt: str, agent):
        """AI makes a decision based on past memory and new input."""
        messages = [
            {"role": "system", "content": agent.instructions},
            {"role": "user", "content": self.recall()},
            {"role": "user", "content": prompt}
        ]
        
        openai_params = {
            "model": agent.model,
            "temperature": 0.1,
            "max_tokens": self.config.token_limit,
            "messages": messages
        }

        completion = self.config.model.chat.completions.create(**openai_params)
        return completion.choices[0].message.content
