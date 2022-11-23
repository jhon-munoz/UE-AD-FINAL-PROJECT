from fastapi import FastAPI

store = FastAPI(
    title="Poke-Fu-Mi Store Service",
    version="0.1.0",
)


@store.get("/")
async def root():
    return {"message": "Hello World"}
