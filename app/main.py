from fastapi import FastAPI

from functions import update_all_data
app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/update")
def update():
    update_all_data()