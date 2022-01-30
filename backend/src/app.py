from typing import TypedDict
from flask import Flask, jsonify, request
from flask_cors import CORS

from entities.user import User
from utils.crypt import compare_password, hash_password
from utils.data import read_users, write_users


app = Flask(__name__)
CORS(app)


@app.get('/users')
def get_users():
    return jsonify(read_users())


@app.get('/users/<string:cpf>')
def get_user_by_cpf(cpf: str):
    users = User.from_list(read_users())
    finded_user = None

    for user in users:
        if user.cpf == cpf:
            finded_user = user
            break

    if finded_user:
        return jsonify(User.to_dict(finded_user)), 200

    return 'Usuário não encontrado', 404


@app.post('/users')
def add_user():
    if request.is_json:
        users = User.from_list(read_users())
        new_user = User.from_dict(request.get_json())

        for user in users:
            if user.cpf == new_user.cpf:
                return 'CPF já cadastrado', 409

        hashed_password = hash_password(new_user.password)
        new_user.password = str(hashed_password)[2:-1]

        users.append(new_user)

        write_users(users)

        return 'Cadastro realizado com sucesso', 201

    return 'Requisição deve ser em formato JSON', 415


@app.post('/auth/login')
def login():
    if request.is_json:
        users = User.from_list(read_users())

        class LoginInfo(TypedDict):
            cpf: str
            password: str

        login_info: LoginInfo = request.get_json()
        finded_user = None

        for user in users:
            if user.cpf == login_info['cpf']:
                finded_user = user

        if finded_user:
            user_pw = finded_user.password.encode()
            user_pw = user_pw.decode('unicode-escape').encode('latin1')

            match_password = compare_password(user_pw, login_info['password'])

            if match_password:
                return 'Usuário OK', 200

            return 'Senha Incorreta', 401

        return 'Usuário não encontrado', 404

    return 'Requisição deve ser em formato JSON', 415
