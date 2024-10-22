from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/update")
def update():
    return {"status": "ok"}