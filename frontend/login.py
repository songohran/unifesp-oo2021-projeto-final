import json

from browser import document, alert, ajax

from utils import *


def get_form_data_values(inputs):
    '''
    Função que recebe um dicionário de inputs e retorna um outro dicionário contendo os valores do inputs de senha e cpf
    '''
    return {
        'password': inputs['password'].value,
        'cpf': inputs['cpf'].value,
    }


def validate_form_data(inputs):
    '''
    Função que garante que nenhum dos campos estejam vazios
    '''
    data = get_form_data_values(inputs)

    if not data['password']:
        alert("O campo senha não pode estar vazio!")
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['password'].classList.add('input-error')
        return

    if not data['cpf']:
        alert("O campo cpf senha não pode estar vazio!")
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['cpf'].classList.add('input-error')
        return

    return data


def authenticate_user(inputs):
    '''
    Função que autentica usuário enviando requisição para o backend
    '''
    # Pega os dados do input e garante que nenhum deles estejam vazios
    data = validate_form_data(inputs)

    # Se um dos inputs estiverem vazios então data vai ser None, e caso data seja None a função irá parar aqui
    if not data:
        return

    cpf = data['cpf']

    # Definindo o tipo de conteúdo que será enviado para o backend
    headers = {'Content-Type': 'application/json'}
    # Transformando o data que é um dicionário em uma string em formato json
    data = json.dumps(data)

    def oncomplete(res):
        '''
        Função rodada depois que o backend devolver alguma resposta
        '''
        # Pega a resposta como texto e mostra dentro de um alert
        alert(res.text)

        # Limpando classes de css desnecessárias dos inputs
        for input in inputs.values():
            input.classList.remove('input-error')

        # Se o usuário for autenticado com sucesso o status da resposta será 200, e se o status for 200 voltará para página index.html
        if res.status == 200:
            window.sessionStorage.setItem('login', True)
            window.sessionStorage.setItem('user-cpf', cpf)
            go_to('/index.html')

    # Enviando requisição do tipo POST para o backend
    ajax.post(
        # URL em que se deve acessar para autenticação de usuário no backend
        'http://localhost:5000/auth/login',
        headers=headers, data=data,
        oncomplete=oncomplete
    )


# Pegando o formulário pela tag
form = document.querySelector('form')
# Prevenindo ação padrão do formulário
form.bind('submit', lambda e: e.preventDefault())

# Criando um dicionário para os inputs
inputs = dict()
# Armazenando no dicionário o input de cpf
inputs['cpf'] = document.querySelector('input#cpf')
# Armazenando no dicionário o input de senha
inputs['password'] = document.querySelector('input#password')

# Pegando o botão de fazer login
btn_login = document['btn-login']
# Adicionando funcionalidade de autenticar usuário quando clicar no botão de fazer login
btn_login.bind('click', lambda _: authenticate_user(inputs))

# Pegando o botão de cancelar
btn_cancel = document['btn-cancel']
# Adicionado funcionalidade de voltar para página index.html quando clicar no botão de cancelar
btn_cancel.bind('click', lambda _: go_to('/index.html'))

# Pegando o ícone de olho aberto
eye_icon = document['eye']
# Pegando o ícone de olho fechado
closed_eye_icon = document['closed-eye']

# Adicionando o comportamento de clique no olho aberto
eye_icon.bind(
    'click',
    lambda _: toggle_password(eye_icon, closed_eye_icon, inputs['password'])
)
# Adicionando o comportamento de clique no olho fechado
closed_eye_icon.bind(
    'click',
    lambda _: toggle_password(eye_icon, closed_eye_icon, inputs['password'])
)
