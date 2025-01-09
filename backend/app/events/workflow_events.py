from llama_index.core.workflow import Event

class RetryEvent(Event):
    """Triggered when user requests a retry."""
    def __init__(self, query: str):
        self.query = query

class FinalizeEvent(Event):
    """Triggered when user approves the workflow result."""
    def __init__(self, result: str):
        self.result = result
