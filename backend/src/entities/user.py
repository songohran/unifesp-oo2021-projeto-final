from __future__ import annotations
from typing import List


class User:
    def __init__(self, name: str, email: str, password: str, cpf: str, cep: str, street: str, number: int) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.cpf = cpf
        self.cep = cep
        self.street = street
        self.number = number

    def from_list(users_list: list) -> List[User]:
        users = []

        for user in users_list:
            try:
                users.append(User.from_dict(user))
            except:
                pass

        return users

    def from_dict(user: dict) -> User:
        return User(user['name'], user['email'], user['password'],
                    user['cpf'], user['cep'], user['street'], user['number'])

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'cpf': self.cpf,
            'cep': self.cep,
            'street': self.street,
            'number': self.number
        }
