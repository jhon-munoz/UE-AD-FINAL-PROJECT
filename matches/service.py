from models import MatchInvite, Match
from datetime import date
from db import add_match


def add_match_service(match: MatchInvite) -> None:
    match_in = Match()
    match_in.created = match.created
    match_in.invited = match.invited
    match_in.status = 'created'
    match_in.round = 0
    match_in.winner = ''
    match_in.created_date = str(date.today())
    match_in.started_date = ''
    match_in.finished_date = ''
    add_match(match_in)
