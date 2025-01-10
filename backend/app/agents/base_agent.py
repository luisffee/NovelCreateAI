from app.tools.llm_tool import LLMTool

class BaseAgent:
    def __init__(self):
        self.llm_tool = LLMTool()
        # Add other tools as needed

    async def run(self, context: dict):
        raise NotImplementedError("Agents must implement the `run` method.")
