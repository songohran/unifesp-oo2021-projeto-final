import json

from browser import document, alert, ajax

from utils import go_to


def get_form_data_values(inputs) -> dict:
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


def validate_form_data(inputs):
    data = get_form_data_values(inputs)

    if not data['name']:
        alert("O campo nome não pode estar vazio!")
        inputs['name'].classList.add('input-error')
        return

    if not data['email']:
        alert("O campo email não pode estar vazio!")
        inputs['email'].classList.add('input-error')
        return

    if not data['password']:
        alert("O campo senha não pode estar vazio!")
        inputs['password'].classList.add('input-error')
        return

    if not data['password_confirm']:
        alert("O campo confirmar senha não pode estar vazio!")
        inputs['password_confirm'].classList.add('input-error')
        return

    if data['password'] != data['password_confirm']:
        alert("As duas senhas tem que ser idênticas!")
        inputs['password'].classList.add('input-error')
        inputs['password_confirm'].classList.add('input-error')
        return

    if not data['cpf']:
        alert("O campo cpf senha não pode estar vazio!")
        inputs['cpf'].classList.add('input-error')
        return

    if not data['cep']:
        alert("O campo cep senha não pode estar vazio!")
        inputs['cep'].classList.add('input-error')
        return

    if not data['street']:
        alert("O campo logradouro senha não pode estar vazio!")
        inputs['street'].classList.add('input-error')
        return

    if not data['number']:
        alert("O campo número senha não pode estar vazio!")
        inputs['number'].classList.add('input-error')
        return

    return data


def create_user_record(inputs):
    data = validate_form_data(inputs)

    if not data:
        return

    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)

    def oncomplete(res):
        alert(res.text)

        for input in inputs.values():
            input.classList.remove('input-error')

        if res.status == 201:
            go_to('/index.html')

    ajax.post(
        'http://localhost:5000/users',
        headers=headers, data=data,
        oncomplete=oncomplete
    )


def handle_cep_blur(ev, input):
    cep = ev.target.value.replace('-', '')

    def fill_street_input(res):
        is_error = res.json.get('erro') == True

        if not is_error:
            input.value = str(res.json.get('logradouro'))
            input.disabled = True

    if len(cep) == 8:
        ajax.get(
            f'https://viacep.com.br/ws/{cep}/json/',
            oncomplete=fill_street_input
        )


form = document.querySelector('form')
form.bind('submit', lambda e: e.preventDefault())

inputs = dict()
inputs['name'] = document.querySelector('input#name')
inputs['email'] = document.querySelector('input#email')
inputs['password'] = document.querySelector('input#password')
inputs['password_confirm'] = document.querySelector('input#password_confirm')
inputs['cpf'] = document.querySelector('input#cpf')
inputs['cep'] = document.querySelector('input#cep')
inputs['street'] = document.querySelector('input#street')
inputs['number'] = document.querySelector('input#number')

inputs['cep'].bind('blur', lambda ev: handle_cep_blur(ev, inputs['street']))

btn_record = document['btn-create-record']
btn_record.bind('click', lambda _: create_user_record(inputs))

btn_cancel = document['btn-cancel']
btn_cancel.bind('click', lambda _: go_to('/index.html'))
