import os
import json
from typing import List

from entities.user import User
from entities.diary import Diary


def create_data_folder():
    '''
    Função que criar a pasta data caso ela não exista
    '''
    try:
        os.mkdir('data')
    except FileExistsError:
        pass


def create_file(filename: str):
    '''
    Função que cria um arquivo dentro da pasta data caso o arquivo não exista
    '''
    try:
        f = open(f'data/{filename}', 'x')
        f.write('[]')
        f.close()
    except FileExistsError:
        pass


def setup():
    '''
    Função que garante que a pasta data tenha tudo que necessário
    '''
    create_data_folder()
    create_file('users.json')
    create_file('diaries.json')


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
    # json.dumps convertendo variavel users_dict de lista de dicionários para string
    users_json = json.dumps(User.to_list(users))

    f = open('data/users.json', 'w')
    f.write(users_json)
    f.close()


def read_diaries() -> list:
    '''
    Função que lê o arquivo de diários e retorna uma lista de diários
    '''
    f = open('data/diaries.json', 'r')
    diaries = f.read()
    f.close()

    # json.loads convertendo variavel diaries de string para lista
    return json.loads(diaries)


def write_diaries(diaries: List[Diary]) -> list:
    '''
    Função que escreve no arquivo de diários
    '''
    # json.dumps convertendo variavel diaries_dict de lista de dicionários para string
    diaries_json = json.dumps(Diary.to_list(diaries))

    f = open('data/diaries.json', 'w')
    f.write(diaries_json)
    f.close()


def create_diary(user: User):
    diaries = Diary.from_list(read_diaries())
    new_diary = Diary(user.cpf, list())

    diaries.append(new_diary)

    write_diaries(diaries)
