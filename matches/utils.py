import requests as re
import os

AUTH_URL = 'http://auth'
USERS_URL = 'http://users'


def authorize(token: str | None,
              username: str | None = None,
              role: str | None = None) -> bool:
    if token is None:
        return False
    requester_name = re.get(
        f'{AUTH_URL}/user-context/{token}').json()['username']
    if requester_name is None:
        return False
    if username is not None and requester_name != username:
        return False
    if role is not None:
        requester_role = re.get(
            f'{USERS_URL}/users/{requester_name}?token={os.environ["token"]}'
        ).json()['role']
        if requester_role != role:
            return False
    return True
