from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Intro to FastAPI",
    description="A simple introduction to FastAPI",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")

def read_item(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
