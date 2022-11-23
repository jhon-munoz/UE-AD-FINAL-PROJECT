from fastapi import FastAPI
from fastapi.responses import JSONResponse

from routers import balance, pokemon, purchase
from errors import NotFound

store = FastAPI(
    title='Poke-Fu-Mi Store Service',
    version='0.1.0',
)
store.include_router(balance.router)
store.include_router(pokemon.router)
store.include_router(purchase.router)


@store.exception_handler(NotFound)
def not_found_exception_handler(_, __):
    return JSONResponse("Not Found", 404)
