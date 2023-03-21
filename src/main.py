from fastapi import FastAPI, HTTPException
from utils import generate_path

app = FastAPI()


@app.get("/")
def home():
    return "cum"


@app.get("/api/{path}")
def gigachad(path: str):
    if path == generate_path(69):
        return "CUM!"

    raise HTTPException(status_code=418, detail="I'm a teapot")


