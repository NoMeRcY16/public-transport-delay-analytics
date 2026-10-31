from fastapi import FastAPI

app = FastAPI(title="Transport ETA API")

@app.get("/")
def home():
    return {"status": "ok", "message": "Transport ETA backend is running"}
