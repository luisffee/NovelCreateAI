from llama_index.core.workflow import Event

class StartEvent(Event):
    """Base event to start a workflow."""
    def __init__(self, query: str):
        self.query = query

class StopEvent(Event):
    """Base event to stop a workflow."""
    def __init__(self, result: str):
        self.result = result