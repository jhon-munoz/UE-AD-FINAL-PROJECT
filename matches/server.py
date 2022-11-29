from fastapi import FastAPI
from fastapi.responses import JSONResponse

from routers import matches, invites
from errors import NotFound

matches = FastAPI(
    title='Poke-Fu-Mi Matches Service',
    version='0.1.0',
)

matches.include_router(matches.router)
matches.include_router(invites.router)


@matches.get('/')
async def root():
    return {'message': 'Hello World'}


@matches.exception_handler(NotFound)
def not_found_exception_handler(_, __):
    return JSONResponse("Not Found", 404)
