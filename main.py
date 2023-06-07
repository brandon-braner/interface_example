from fastapi import FastAPI

app = FastAPI()

from app.modules.user.router import router as user_router

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(user_router, prefix="/user")