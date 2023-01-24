from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def test():
    return {"message": "Hello World, test message"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
