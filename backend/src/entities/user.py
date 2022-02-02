from __future__ import annotations
from typing import List


class User:
    '''
    Classe responsável pela facilitação da manipulação de dados de usuários
    '''

    def __init__(self, name: str, email: str, password: str, cpf: str, cep: str, street: str, number: int) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.cpf = cpf
        self.cep = cep
        self.street = street
        self.number = number

    def from_list(users_list: list) -> List[User]:
        '''
        Função que transforma uma lista genérica em uma lista da classe User
        '''
        users = []

        for user in users_list:
            try:
                users.append(User.from_dict(user))
            except:
                pass

        return users

    def from_dict(user: dict) -> User:
        '''
        Função que transforma um dicionário genérico em um objeto da classe User
        '''
        return User(user['name'], user['email'], user['password'],
                    user['cpf'], user['cep'], user['street'], user['number'])

    def to_dict(self) -> dict:
        '''
        Função que transforma um objeto da classe User em um dicionário genérico
        '''
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'cpf': self.cpf,
            'cep': self.cep,
            'street': self.street,
            'number': self.number
        }
