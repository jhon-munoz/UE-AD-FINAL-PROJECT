from fastapi import FastAPI
from fastapi.responses import JSONResponse

from db import get_match, get_match_list, add_match
from models import Match
from errors import NotFound


matches = FastAPI(
    title='Poke-Fu-Mi Matches Service',
    version='0.1.0',
)


# @matches.get('/')
# async def root():
#     return {'message': 'Hello World'}

@matches.get('/{id}')
async def match(id: str) -> Match:
    return get_match(id)

@matches.get('/')
async def match() -> [Match]:
    return get_match_list()

@matches.post('/')
async def create_match(match: Match) -> list[Match]:
    add_match(match)
    return JSONResponse("Addition successful", 202)

@matches.exception_handler(NotFound)
def not_found_exception_handler(_, __):
    return JSONResponse("Not Found", 404)