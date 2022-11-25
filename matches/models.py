from pydantic import BaseModel

class MatchRequest(BaseModel):
    player1: str = ''
    player2: str = ''

class Match(MatchRequest):
    _id: str
    status: str = ''
    round: int = ''
    winner: str = ''
    created_date: str = ''
    started_date: str = ''
    finished_date: str = ''