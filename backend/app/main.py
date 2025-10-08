from fastapi import FastAPI
from .api import runs  

app = FastAPI()
app.include_router(runs.router)

@app.get("/ping")
def ping():
    return {"message": "pong"}
