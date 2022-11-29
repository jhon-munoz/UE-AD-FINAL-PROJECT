from datetime import date
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_invites_to_player, get_open_invites, get_match, get_player_matches, update_match
from service import add_match_service
from models import Match, MatchInvite
from utils import authorize, get_username

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
    if not authorize(token, username=match.creator, role='player'):
        return JSONResponse({}, 401)
    add_match_service(match)
    return JSONResponse("Invite created", 202)


@router.post('/{match_id}')
async def accept_invite(match_id: str, token: str | None = None):
    match = get_match(match_id)
    if not authorize(token, username=match.invited, role='player'):
        return JSONResponse({}, 401)
    invited = get_username(token)
    if len(get_player_matches(match.creator)) >= 3 or len(
            get_player_matches(invited)) >= 3:
        return JSONResponse("Max simultaneous matches exceeded", 422)
    update_match(
        match_id, {
            'invited': invited,
            'status': 'in progress',
            'round': 1,
            'started_date': str(date.today()),
        })
    return JSONResponse("Invite accepted", 200)
