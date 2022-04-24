from fastapi import FastAPI

app = FastAPI()


@app.get("/hogehoge")
async def hello():
    return {"message": "hello world!"}