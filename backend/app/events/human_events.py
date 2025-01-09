from llama_index.core.workflow import Event

class InputRequiredEvent(Event):
    """Triggered when user input is required."""
    def __init__(self, prefix: str, query: str, payload: str):
        self.prefix = prefix
        self.query = query
        self.payload = payload

class HumanResponseEvent(Event):
    """Triggered when human feedback is received."""
    def __init__(self, response: str):
        self.response = response
