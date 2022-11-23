from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_user_balance, update_user_balance
from models import Balance

router = APIRouter(prefix="/balance")


@router.get("/{username}")
async def get_balance(username: str) -> Balance:
    balance = get_user_balance(username)
    if balance is None:
        return JSONResponse("Not Found", 404)
    return balance


@router.put("/{username}")
async def put_balance(username: str, balance: float) -> Balance:
    update_user_balance(username, balance)
    return get_user_balance(username)
