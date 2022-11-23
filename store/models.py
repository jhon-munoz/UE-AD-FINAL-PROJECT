from pydantic import BaseModel


class Balance(BaseModel):
    user: str
    balance: float
