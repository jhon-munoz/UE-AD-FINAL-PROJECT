from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_match, get_all_match, update_match, delete_match
from service import add_match_service
from models import Match, MatchRequest
from utils import authorize

router = APIRouter(prefix='/match')


@router.get('/')
async def all_match(token: str | None = None) -> list[Match]:
    if not authorize(token, role='admin'):
        return JSONResponse({}, 401)
    return get_all_match()


@router.get('/{id}')
async def match(id: str, token: str | None = None) -> Match:
    return get_match(id)


@router.post('/')
async def create_match(match: MatchRequest, token: str | None = None):
    add_match_service(match)
    return JSONResponse("Addition successful", 202)


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
