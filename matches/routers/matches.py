from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_match, get_all_matches, update_match, delete_match
from models import Match
from utils import authorize

router = APIRouter(prefix='/matches')


@router.get('/')
async def all_matches(token: str | None = None) -> list[Match]:
    if not authorize(token, role='admin'):
        return JSONResponse({}, 401)
    return get_all_matches()


@router.get('/{id}')
async def match(id: str, token: str | None = None) -> Match:
    return get_match(id)


@router.put('/{id}')
async def put_match(id, match: Match, token: str | None = None):
    if not authorize(token, role='admin'):
        return JSONResponse({}, 401)
    update_match(id, match)
    return JSONResponse("Update successful", 200)


@router.delete('/{id}')
async def del_match(id, token: str | None = None):
    if not authorize(token, role='admin'):
        return JSONResponse({}, 401)
    delete_match(id)
    return JSONResponse("Delete successful", 200)
