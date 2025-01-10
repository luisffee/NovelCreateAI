from fastapi import FastAPI

app = FastAPI(
    title="Collaborative Story Creation API",
    description="A multi-agent workflow backend for collaborative story creation.",
    version="1.0.0",
)



@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

