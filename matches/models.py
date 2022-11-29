from pydantic import BaseModel
from pydantic import conint
from typing import Literal


class MatchInvite(BaseModel):
    creator: str
    invited: str | None


class Match(MatchInvite):
    _id: str
    status: Literal['created', 'in progress', 'finished']
    round: conint(ge=0, le=6)  # 0 for created and 6 for finished
    winner: str | None
    created_date: str
    started_date: str | None
    finished_date: str | None
