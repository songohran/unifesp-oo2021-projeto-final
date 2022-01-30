import os
import json
from typing import List

from entities.user import User


def create_data_folder():
    try:
        os.mkdir('data')
    except FileExistsError:
        pass


def create_users_json():
    try:
        f = open('data/users.json', 'x')
        f.write('[]')
        f.close()
    except FileExistsError:
        pass


def read_users() -> list:
    f = open('data/users.json', 'r')
    users = f.read()
    f.close()

    return json.loads(users)


def write_users(users: List[User]):
    users_dict = []

    for user in users:
        users_dict.append(User.to_dict(user))

    users_json = json.dumps(users_dict)

    f = open('data/users.json', 'w')
    f.write(users_json)
    f.close()


create_data_folder()
create_users_json()
