from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_match, get_all_match, add_match
from models import Match

router = APIRouter(prefix='/match')

@router.get('/')
async def match() -> [Match]:
    return get_all_match()

@router.get('/{id}')
async def match(id: str) -> Match:
    return get_match(id)

@router.post('/')
async def create_match(match: Match) -> list[Match]:
    add_match(match)
    return JSONResponse("Addition successful", 202)