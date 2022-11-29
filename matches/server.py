from fastapi import FastAPI
from fastapi.responses import JSONResponse

from routers import match
from errors import NotFound

matches = FastAPI(
    title='Poke-Fu-Mi Matches Service',
    version='0.1.0',
)

matches.include_router(match.router)


@matches.get('/')
async def root():
    return {'message': 'Hello World'}


@matches.exception_handler(NotFound)
def not_found_exception_handler(_, __):
    return JSONResponse("Not Found", 404)
