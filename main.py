from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API работает"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Dogs vs Cats Classification API"}
