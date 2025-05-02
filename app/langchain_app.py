from fastapi import FastAPI
from langchain_openai import ChatOpenAI

app = FastAPI()
llm = ChatOpenAI()

@app.get("/ping")
def ping():
    return {"msg": "pong"}

@app.get("/ask")
def ask(q: str):
    return {"answer": llm.invoke(q).content}
