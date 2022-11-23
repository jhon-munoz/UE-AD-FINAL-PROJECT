from pydantic import BaseModel


class Balance(BaseModel):
    user: str
    balance: float


class PokemonAdd(BaseModel):
    name: str
    type: str
    level: int
    price: float


class Pokemon(PokemonAdd):
    id: str


class UserPokemon(BaseModel):
    user: str
    pokemon: list[Pokemon]


class PokemonPurchase(BaseModel):
    user: str
    pokemon_id: str
