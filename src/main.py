from fastapi import FastAPI, HTTPException
from utils import read_path, generate_path

app = FastAPI()


@app.get("/")
def home():
    return "cum"


@app.get("/api/{path}")
def gigachad(path: str):
    if path == generate_path():
        return "CUM!"

    raise HTTPException(status_code=418, detail="I'm a teapot")


