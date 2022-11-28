from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_user_balance, update_user_balance
from models import Balance
from utils import authorize

router = APIRouter(prefix='/balance')


@router.get('/{username}')
async def get_balance(username: str, token: str | None = None) -> Balance:
    if not authorize(token, username=username):
        return JSONResponse({}, 401)
    return get_user_balance(username)


@router.put('/{username}')
async def put_balance(username: str,
                      balance: float,
                      token: str | None = None) -> Balance:
    if not authorize(token, role='admin'):
        return JSONResponse({}, 401)
    update_user_balance(username, balance)
    return JSONResponse("Update successful", 202)
