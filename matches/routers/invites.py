from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_invites_to_player, get_open_invites
from service import add_match_service
from models import Match, MatchInvite
from utils import authorize

router = APIRouter(prefix='/invites')


@router.get('/{username}')
async def players_invites(username: str,
                          token: str | None = None) -> list[Match]:
    if not authorize(token, username=username, role='player'):
        return JSONResponse({}, 401)
    return get_invites_to_player(username)


@router.get('/')
async def open_invites(token: str | None = None) -> list[Match]:
    if not authorize(token, role='player'):
        return JSONResponse({}, 401)
    return get_open_invites()


@router.post('/')
async def invite(match: MatchInvite, token: str | None = None):
    if not authorize(token, username=match.creator, role='admin'):
        return JSONResponse({}, 401)
    add_match_service(match)
    return JSONResponse("Invite created", 202)
