import os
import json
from typing import List

from entities.user import User


def create_data_folder():
    '''
    Função que criar a pasta data caso ela não exista
    '''
    try:
        os.mkdir('data')
    except FileExistsError:
        pass


def create_users_json():
    '''
    Função que cria arquivo users.json dentro da pasta data caso o arquivo não exista
    '''
    try:
        f = open('data/users.json', 'x')
        f.write('[]')
        f.close()
    except FileExistsError:
        pass


def setup():
    '''
    Função que garante que a pasta data tenha tudo que necessário
    '''
    create_data_folder()
    create_users_json()


def read_users() -> list:
    '''
    Função que lê o arquivo de usuários e retorna uma lista de usuários
    '''
    f = open('data/users.json', 'r')
    users = f.read()
    f.close()

    # json.loads convertendo variavel users de string para lista
    return json.loads(users)


def write_users(users: List[User]):
    '''
    Função que escreve no arquivo de usuários
    '''
    # Variavel que irá guardar usuários em forma de dicionário
    users_dict = []

    for user in users:
        # Convertendo variavel user da classe User para dicionário
        users_dict.append(User.to_dict(user))

    # json.dumps convertendo variavel users_dict de lista de dicionários para string
    users_json = json.dumps(users_dict)

    f = open('data/users.json', 'w')
    f.write(users_json)
    f.close()
