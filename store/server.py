from fastapi import FastAPI

from routers import balance, pokemon

store = FastAPI(
    title='Poke-Fu-Mi Store Service',
    version='0.1.0',
)
store.include_router(balance.router)
store.include_router(pokemon.router)


@store.get('/')
async def root():
    return {'message': 'Hello World'}
