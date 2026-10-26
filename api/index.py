import os, sys
sys.path.append(os.path.dirname(__file__))
from fastapi import FastAPI

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

@app.get("/api/health")
def health():
    return {"ok": True}