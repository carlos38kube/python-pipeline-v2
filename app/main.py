from fastapi import FastAPI

app = FastAPI(title="python-pipeline-v2")


@app.get("/")
def read_root():
    return {"status": "ok", "service": "python-pipeline-v2"}


@app.get("/health")
def health():
    return {"status": "healthy"}
