from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "Project Zebra",
        "status": "running"
    }