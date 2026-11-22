from fastapi import FastAPI

app = FastAPI(title="Quote Extractor")

@app.get("/health")
def health():
    return {"status": "ok"}
