from pydantic import BaseModel

class Match(BaseModel):
    id: str
    player1: str
    player2: str
    status: str
    round: int
    winner: str
    created_date: str
    started_date: str
    finished_date: str