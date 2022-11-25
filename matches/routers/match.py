from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_match, get_all_match, add_match, update_match, delete_match
from models import Match, MatchRequest
from datetime import date

router = APIRouter(prefix='/match')

@router.get('/')
async def all_match() -> list[Match]:
    return get_all_match()

@router.get('/{id}')
async def match(id: str) -> Match:
    return get_match(id)

@router.post('/')
async def create_match(match: MatchRequest):
    match_in = Match()
    match_in.player1 = match.player1
    match_in.player2 = match.player2
    match_in.status = 'created'
    match_in.round = 0
    match_in.winner = ''
    match_in.created_date = str(date.today())
    match_in.started_date = ''
    match_in.finished_date = ''
    add_match(match_in)
    return JSONResponse("Addition successful", 202)

@router.put('/{id}')
async def put_match(id, match: Match):
    update_match(id, match)
    return JSONResponse("Update successful", 200)

@router.delete('/{id}')
async def del_match(id):
    delete_match(id)
    return JSONResponse("Delete successful", 200)