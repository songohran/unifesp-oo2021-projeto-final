import json
import re

from browser import document, alert, ajax

from utils import *


def get_form_data_values(inputs: dict) -> dict:
    '''
    Função que recebe um dicionário de inputs e retorna um outro dicionário contendo os valores do inputs de nome, email, senha, confirmar senha, cpf, cep, logradouro e número
    '''
    return {
        'name': inputs['name'].value,
        'email': inputs['email'].value,
        'password': inputs['password'].value,
        'password_confirm': inputs['password_confirm'].value,
        'cpf': inputs['cpf'].value,
        'cep': inputs['cep'].value,
        'street': inputs['street'].value,
        'number': inputs['number'].value,
    }


def validate_cpf(cpf: str) -> bool:
    '''
    Função que verifica se o cpf é válido
    '''
    # Remove do cpf tudo que não for número
    cpf = re.sub(r'\D', '', cpf)

    # Verifica o tamanho do cpf, se for diferente de 11 então é inválido
    if len(cpf) != 11:
        return False

    # Variavel que irá guardar primeiro digito verifVariavel que irá guardar segundo digito icador
    first_verifying_digit = None
    # Variavel que irá guardar segundo digito verificador
    second_verifying_digit = None

    # Soma da multiplicação dos 9 primeiros digitos
    for i, char in enumerate(cpf[:9]):
        if first_verifying_digit == None:
            first_verifying_digit = int(char) * 10
            continue

        first_verifying_digit += int(char) * (10 - i)

    # Resto da divisão por 11
    first_verifying_digit %= 11
    first_verifying_digit = 11 - first_verifying_digit
    # Se for maior que 10 o digito verificador é 0 senão é o que foi encontrado mesmo
    first_verifying_digit = first_verifying_digit if first_verifying_digit < 10 else 0

    # Verificando se o penúltimo digito do cpf bate com primeiro digito verificador
    if int(cpf[-2]) != first_verifying_digit:
        return False

    # Soma da multiplicação dos 10 primeiros digitos
    for i, char in enumerate(cpf[:10]):
        if second_verifying_digit == None:
            second_verifying_digit = int(char) * 11
            continue

        second_verifying_digit += int(char) * (11 - i)

    # Resto da divisão por 11
    second_verifying_digit %= 11
    second_verifying_digit = 11 - second_verifying_digit
    # Se for maior que 10 o digito verificador é 0 senão é o que foi encontrado mesmo
    second_verifying_digit = second_verifying_digit if second_verifying_digit < 10 else 0

    # Verificando se o último digito do cpf bate com segundo digito verificador
    if int(cpf[-1]) != second_verifying_digit:
        return False

    return True


def validate_form_data(inputs: dict):
    '''
    Função que garante que nenhum dos campos estejam vazios
    '''
    data = get_form_data_values(inputs)

    if not data['name']:
        alert('O campo nome não pode estar vazio!')
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['name'].classList.add('input-error')
        return

    if not data['email']:
        alert('O campo email não pode estar vazio!')
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['email'].classList.add('input-error')
        return

    if not data['password']:
        alert('O campo senha não pode estar vazio!')
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['password'].classList.add('input-error')
        return

    if not data['password_confirm']:
        alert('O campo confirmar senha não pode estar vazio!')
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['password_confirm'].classList.add('input-error')
        return

    if data['password'] != data['password_confirm']:
        alert('As duas senhas tem que ser idênticas!')
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['password'].classList.add('input-error')
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['password_confirm'].classList.add('input-error')
        return

    if not data['cpf']:
        alert('O campo cpf não pode estar vazio!')
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['cpf'].classList.add('input-error')
        return

    if not validate_cpf(data['cpf']):
        alert('Cpf digitado não é válido')
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['cpf'].classList.add('input-error')
        return

    if not data['cep']:
        alert('O campo cep não pode estar vazio!')
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['cep'].classList.add('input-error')
        return

    if not data['street']:
        alert('O campo logradouro não pode estar vazio!')
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['street'].classList.add('input-error')
        return

    if not data['number']:
        alert('O campo número não pode estar vazio!')
        # Adicionando classe input-error ao input, essa classe deixa o input vermelhinho
        inputs['number'].classList.add('input-error')
        return

    return data


def create_user_record(inputs):
    '''
    Função que cria usuário enviando requisição para o backend
    '''
    # Pega os dados do input e garante que nenhum deles estejam vazios
    data = validate_form_data(inputs)

    # Se um dos inputs estiverem vazios então data vai ser None, e caso data seja None a função irá parar aqui
    if not data:
        return

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

        # Se o usuário for criado com sucesso o status da resposta será 201, e se o status for 201 voltará para página index.html
        if res.status == 201:
            go_to('/index.html')

    # Enviando requisição do tipo POST para o backend
    ajax.post(
        # URL em que se deve acessar para criação de usuário no backend
        'http://localhost:5000/users',
        headers=headers, data=data,
        oncomplete=oncomplete
    )


def handle_cep_blur(ev, input):
    '''
    Função responsável por tentar preencher o campo logradouro automaticamente caso o cep seja válido
    '''
    # Pegando o valor do campo cep e retirando o hífen
    cep = ev.target.value.replace('-', '')

    def fill_street_input(res):
        '''
        Função responsável por pegar a resposta da API viacep e usá-la para preencher o campo logradouro caso estiver tudo certo
        '''
        # Verificando se houve um erro na requisição
        is_error = res.json.get('erro') == True

        # Se não houve erro então preencha o valor do campo logradouro, senão faça nada
        if not is_error:
            input.value = str(res.json.get('logradouro'))
            input.disabled = True

    # Verificando se o cep está no tamanho correto, se não estiver a função não irá fazer nada
    if len(cep) == 8:
        # Enviando requisição GET para API de viacep
        ajax.get(
            f'https://viacep.com.br/ws/{cep}/json/',
            oncomplete=fill_street_input
        )


# Pegando o formulário pela tag
form = document.querySelector('form')
# Prevenindo ação padrão do formulário
form.bind('submit', lambda e: e.preventDefault())

# Criando um dicionário para os inputs
inputs = dict()
# Armazenando no dicionário o input de nome
inputs['name'] = document.querySelector('input#name')
# Armazenando no dicionário o input de email
inputs['email'] = document.querySelector('input#email')
# Armazenando no dicionário o input de senha
inputs['password'] = document.querySelector('input#password')
# Armazenando no dicionário o input de confirmar senha
inputs['password_confirm'] = document.querySelector('input#password_confirm')
# Armazenando no dicionário o input de cpf
inputs['cpf'] = document.querySelector('input#cpf')
# Armazenando no dicionário o input de cep
inputs['cep'] = document.querySelector('input#cep')
# Armazenando no dicionário o input de logradouro
inputs['street'] = document.querySelector('input#street')
# Armazenando no dicionário o input de número
inputs['number'] = document.querySelector('input#number')

# Adicionando funcionalidade ao campo cep de tentar preencher o campo logradouro quando terminar de escrever o cep
inputs['cep'].bind('blur', lambda ev: handle_cep_blur(ev, inputs['street']))

# Pegando o botão de criar cadastro
btn_record = document['btn-create-record']
# Adicionando funcionalidade de criar cadastro de usuário ao botão de criar cadastro
btn_record.bind('click', lambda _: create_user_record(inputs))

# Pegando o botão de cancelar
btn_cancel = document['btn-cancel']
# Adicionando funcionalidade de voltar para página index.html ao botão de cancelar
btn_cancel.bind('click', lambda _: go_to('/index.html'))

# Criando dicionário para guardar os ícones de olho aberto do campo senha e do campo confirmar senha
eye_icons = dict()
# Armazendo ícone de olho aberto do campo senha
eye_icons['password'] = inputs['password'].parentElement.querySelector(
    'svg#eye')
# Armazendo ícone de olho fechado do campo confirmar senha
eye_icons['password_confirm'] = inputs['password_confirm'].parentElement.querySelector(
    'svg#eye')

# Criando dicionário para guardar os ícones de olho fechado do campo senha e do campo confirmar senha
closed_eye_icons = dict()
# Armazendo ícone de olho fechado do campo senha
closed_eye_icons['password'] = inputs['password'].parentElement.querySelector(
    'svg#closed-eye')
# Armazendo ícone de olho fechado do campo confirmar senha
closed_eye_icons['password_confirm'] = inputs['password_confirm'].parentElement.querySelector(
    'svg#closed-eye')

# Adicionando o comportamento de clique no olho aberto do campo senha
eye_icons['password'].bind(
    'click',
    lambda _: toggle_password(
        eye_icons['password'],
        closed_eye_icons['password'],
        inputs['password']
    )
)
# Adicionando o comportamento de clique no olho fechado do campo senha
closed_eye_icons['password'].bind(
    'click',
    lambda _: toggle_password(
        eye_icons['password'],
        closed_eye_icons['password'],
        inputs['password']
    )
)

# Adicionando o comportamento de clique no olho aberto do campo confirmar senha
eye_icons['password_confirm'].bind(
    'click',
    lambda _: toggle_password(
        eye_icons['password_confirm'],
        closed_eye_icons['password_confirm'],
        inputs['password_confirm']
    )
)
# Adicionando o comportamento de clique no olho fechado do campo confirmar senha
closed_eye_icons['password_confirm'].bind(
    'click',
    lambda _: toggle_password(
        eye_icons['password_confirm'],
        closed_eye_icons['password_confirm'],
        inputs['password_confirm']
    )
)
