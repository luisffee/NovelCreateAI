from app.config import Config
from langchain_ollama import OllamaLLM as Ollama

class BaseLLMTool:
    def __init__(self, model_name):
        config = Config()
        if not model_name:
            model_name = config.OLLAMA_CONFIG["model"]
        else:
            config.OLLAMA_CONFIG["model"] = model_name
        
        self.llm = Ollama(config.OLLAMA_CONFIG)

    async def query(self, prompt: str) -> str:
        """Interacts with an LLM to generate a response."""
        response = await self.llm.generate(prompt)
        return response
