from fastapi import FastAPI
app = FastAPI(title="StudyLog API")
@app.get("/health")
def health():
    return {"status":"ok"}