from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_match, get_all_match, update_match, delete_match
from service import add_match_service
from models import Match, MatchRequest

router = APIRouter(prefix='/match')

@router.get('/')
async def all_match() -> list[Match]:
    return get_all_match()

@router.get('/{id}')
async def match(id: str) -> Match:
    return get_match(id)

@router.post('/')
async def create_match(match: MatchRequest):
    add_match_service(match)
    return JSONResponse("Addition successful", 202)

@router.put('/{id}')
async def put_match(id, match: Match):
    update_match(id, match)
    return JSONResponse("Update successful", 200)

@router.delete('/{id}')
async def del_match(id):
    delete_match(id)
    return JSONResponse("Delete successful", 200)