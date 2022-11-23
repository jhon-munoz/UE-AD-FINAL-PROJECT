from pydantic import BaseModel


class Balance(BaseModel):
    user: str
    balance: float


class Pokemon(BaseModel):
    id: str
    name: str
    type: str
    level: int
    price: float


class UserPokemon(BaseModel):
    user: str
    pokemon: list[Pokemon]
