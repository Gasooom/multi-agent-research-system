# milestone: api gateway service entry point

from fastapi import FastAPI
from services.common.logging import setup_logging

setup_logging()

app = FastAPI(title="API Gateway")


@app.get("/health")
def health():
    return {"status": "ok"}