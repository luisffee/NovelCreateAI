from llama_index.core.workflow import Event

class ProgressEvent(Event):
    """Emitted to inform about workflow progress."""
    def __init__(self, msg: str):
        self.msg = msg
