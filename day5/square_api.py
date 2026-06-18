from fastapi import FastAPI

app = FastAPI()

@app.get("/square/{n}")
def square_number(n: int):
    return {
        "input": n,
        "result": n * n
    }
@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI app"}