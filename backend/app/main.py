from fastapi import FastAPI

app = FastAPI(title= "AI Productivity App")

@app.get("/")
def root():
    return {"message": "Ai Productivity App"}

