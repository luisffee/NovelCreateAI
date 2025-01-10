from pydantic import BaseSettings

class Config(BaseSettings):
    app_name: str = "NovelCreateAI"
    debug: bool = False
    database_url: str = "postgresql://root:123456@db:5432/novelcreateai"
    
    OLLAMA_CONFIG: dict = {
        'model': "llama3.2:3b",
        'temperature': 0.4,
        'keep_alive': 600,
    }
    
    RAG_TEMPLATE: str = """
    Use o seguinte contexto (e apenas este contexto) para responder a pergunta.
    Se você não souber a resposta, diga que não sabe.
    Use no máximo uma frase e mantenha a resposta concisa,
    mas inclua a pergunta na resposta.

    Contexto: {context}
    Pergunta: {query}
    Resposta:
    """
    
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200