from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_user_balance, update_user_balance
from models import Balance

router = APIRouter(prefix='/balance')


@router.get('/{username}')
async def get_balance(username: str) -> Balance:
    return get_user_balance(username)


@router.put('/{username}')
async def put_balance(username: str, balance: float) -> Balance:
    update_user_balance(username, balance)
    return JSONResponse("Update successful", 202)
