from fastapi import FastAPI
from api import log_router

app = FastAPI()

app.include_router(log_router, prefix="/logs")

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)