from typing import TypedDict
from flask import Flask, jsonify, request
from flask_cors import CORS

from entities.user import User
from entities.diary import Diary, DiaryEntry
from utils.crypt import compare_password, hash_password
import utils.data as data


# Criando aplicação do backend
app = Flask(__name__)
# Permitindo que frontend acesse o backend
CORS(app)


# Criando rota GET para uri /users
# Rota tem como funcionalidade pegar todos os usuários
@app.get('/users')
def get_users():
    # Enviando resposta em formato json da lista de usuários existentes
    return jsonify(data.read_users())


# Criando rota GET para uri /users pelo cpf
# Rota tem como funcionalidade pegar um usuário pelo cpf
@app.get('/users/<string:cpf>')
def get_user_by_cpf(cpf: str):
    # Pegando usuários da pasta data e convertendo eles para classe User
    users = User.from_list(data.read_users())
    # Variavel que irá guardar o usuário encontrado
    finded_user = None

    for user in users:
        # Verificando se algum usuário tem o mesmo cpf da requisição, se tiver irá guardar na variavel finded_user
        if user.cpf == cpf:
            finded_user = user
            break

    # Se tiver algum usuário encontrado
    if finded_user:
        # Convertendo finded_user para dicionário e enviando resposta em formato json com status 200
        return jsonify(User.to_dict(finded_user)), 200

    # Enviando resposta de usuário não encontrado com status 404
    return 'Usuário não encontrado', 404


# Criando rota POST para uri /users
# Rota tem como funcionalidade criar um usuário
@app.post('/users')
def add_user():
    # Verificando se o formato da requisição é do tipo JSON, pois é o tipo que o backend precisa para funcionar
    if request.is_json:
        # Pegando usuários da pasta data e convertendo eles para classe User
        users = User.from_list(data.read_users())
        # Pegando usuário enviado pela requisição e convertendo-o para classe User
        new_user = User.from_dict(request.get_json())

        for user in users:
            # Verificando se algum usuário já existente possuí o mesmo cpf do novo usuário
            if user.cpf == new_user.cpf:
                # Retornado mensagem de CPF já cadastro com status 409 indicando conflito do novo usuário com os usuários já existentes
                return 'CPF já cadastrado', 409

        # Criptografando senha do novo usuário
        hashed_password = hash_password(new_user.password)
        # Convertendo senha criptografada de bytes para string
        new_user.password = str(hashed_password)[2:-1]

        # Criação de diário para o usuário
        data.create_diary(new_user)

        # Adicionado o novo usuário na lista de usuários
        users.append(new_user)

        # Atualizando o arquivo que armazena lista de usuários
        data.write_users(users)

        # Retornando mensagem de que cadastro foi realizado com sucesso com status 201 indicando que um usuário foi criado
        return 'Cadastro realizado com sucesso', 201

    # Retornando mensagem de que o formato deve ser JSON com status 415 indicando que backend não tem suporte para nada além de JSON
    return 'Requisição deve ser em formato JSON', 415


# Criando rota POST para uri /auth/login
# Rota tem como funcionalidade autenticar um usuário
@app.post('/auth/login')
def login():
    # Verificando se o formato da requisição é do tipo JSON, pois é o tipo que o backend precisa para funcionar
    if request.is_json:
        # Pegando usuários da pasta data e convertendo eles para classe User
        users = User.from_list(data.read_users())

        class LoginInfo(TypedDict):
            '''
            Classe que representa um dicionário que tem apenas as chaves cpf e password
            '''
            cpf: str
            password: str

        # Pegando informações de login pela requisição
        login_info: LoginInfo = request.get_json()
        # Variavel que irá guardar o usuário encontrado
        finded_user = None

        for user in users:
            # Verificando se cpf do login bate com cpf de algum usuário, se tiver irá guardar na variavel finded_user
            if user.cpf == login_info['cpf']:
                finded_user = user
                break

        # Se usuário existir
        if finded_user:
            # Pegando senha do usuário encontrado e convertendo em bytes
            user_pw = finded_user.password.encode()
            # Decodificando senha de forma que remova os caracteres de escape '\\' e codificando de volta bytes
            user_pw = user_pw.decode('unicode-escape').encode('latin1')

            # Comparando senha codificada com senha enviada no login
            match_password = compare_password(user_pw, login_info['password'])

            # Se a senha bate
            if match_password:
                # Retorna resposta de usuário OK com status 200 indicando tudo certo
                return 'Usuário OK', 200

            # Retorna resposta senha incorreta com status 401 indicando falta de autorização
            return 'Senha Incorreta', 401

        # Retornado mensagem de que usuário não foi encontrado com status 404
        return 'Usuário não encontrado', 404

    # Retornando mensagem de que o formato deve ser JSON com status 415 indicando que backend não tem suporte para nada além de JSON
    return 'Requisição deve ser em formato JSON', 415


@app.get('/diaries')
def get_diaries():
    return jsonify(data.read_diaries())


@app.get('/diaries/<string:user_cpf>')
def get_diary_by_user_cpf(user_cpf: str):
    diaries = Diary.from_list(data.read_diaries())
    finded_diary = None

    for diary in diaries:
        if diary.user_cpf == user_cpf:
            finded_diary = diary
            break

    if finded_diary:
        return jsonify(Diary.to_dict(finded_diary)), 200

    return 'Diário não encontrado', 404


@app.put('/diaries/entries/<string:user_cpf>')
def update_entries(user_cpf: str):
    if request.is_json:
        try:
            new_entry = DiaryEntry.from_dict(request.get_json())
        except KeyError:
            return 'Requisição não contém os dados necessários', 400

        diaries = Diary.from_list(data.read_diaries())
        finded_diary = None

        for diary in diaries:
            if diary.user_cpf == user_cpf:
                finded_diary = diary
                break

        if finded_diary:
            entry_overwrited = False

            for entry in finded_diary.entries:
                if entry.date == new_entry.date:
                    entry.content = new_entry.content
                    entry_overwrited = True
                    break

            if not entry_overwrited:
                finded_diary.entries.append(new_entry)

            data.write_diaries(diaries)

            return 'Diário atualizado com sucesso', 200

        return 'Diário não encontrado', 404

    return 'Requisição deve ser em formato JSON', 415


if __name__ == '__main__':
    # Cria todo setup e arquivos necessários da pasta data
    data.setup()
    # Inicia o servidor da aplicação
    app.run(debug=True)
