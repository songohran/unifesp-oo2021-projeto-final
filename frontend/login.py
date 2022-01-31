import json

from browser import document, alert, ajax

from utils import go_to


def get_form_data_values(inputs):
    return {
        'password': inputs['password'].value,
        'cpf': inputs['cpf'].value,
    }


def validate_form_data(inputs):
    data = get_form_data_values(inputs)

    if not data['password']:
        alert("O campo senha não pode estar vazio!")
        inputs['password'].classList.add('input-error')
        return

    if not data['cpf']:
        alert("O campo cpf senha não pode estar vazio!")
        inputs['cpf'].classList.add('input-error')
        return

    return data


def authenticate_user(inputs):
    data = validate_form_data(inputs)

    if not data:
        return

    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)

    def oncomplete(res):
        alert(res.text)

        for input in inputs.values():
            input.classList.remove('input-error')

        if res.status == 200:
            go_to('/index.html')

    ajax.post(
        'http://localhost:5000/auth/login',
        headers=headers, data=data,
        oncomplete=oncomplete
    )


form = document.querySelector('form')
form.bind('submit', lambda e: e.preventDefault())

inputs = dict()
inputs['cpf'] = document.querySelector('input#cpf')
inputs['password'] = document.querySelector('input#password')

btn_login = document['btn-login']
btn_login.bind('click', lambda _: authenticate_user(inputs))

btn_cancel = document['btn-cancel']
btn_cancel.bind('click', lambda _: go_to('/index.html'))
