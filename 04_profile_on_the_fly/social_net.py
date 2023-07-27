import random

import requests

backend_endpoint = "http://localhost:8000"


def get_user_name(user_id: int) -> str:
    r = requests.get(f"{backend_endpoint}/users/{user_id}")
    r.raise_for_status()
    user = r.json()
    return user["name"]

def get_user_friends(user_id: int) -> list[int]:
    r = requests.get(f"{backend_endpoint}/friends/{user_id}")
    r.raise_for_status()
    friends = r.json()
    return friends


def serf_social_net():
    user_id = 1
    while True:
        name = get_user_name(user_id)
        friends  = get_user_friends(user_id)
        user_id = random.choice(friends)


if __name__ == "__main__":
    try:
        serf_social_net()
    except KeyboardInterrupt:
        pass
