from browser import document, alert, ajax
import json

from utils import go_to


def get_form_data_values() -> dict:
    name = document.querySelector('input#name').value
    email = document.querySelector('input#email').value
    password = document.querySelector('input#password').value
    password_confirm = document.querySelector('input#password_confirm').value
    cpf = document.querySelector('input#cpf').value
    cep = document.querySelector('input#cep').value
    street = document.querySelector('input#street').value
    number = document.querySelector('input#number').value

    return {
        'name': name,
        'email': email,
        'password': password,
        'password_confirm': password_confirm,
        'cpf': cpf,
        'cep': cep,
        'street': street,
        'number': number,
    }


def validate_form_data():
    data = get_form_data_values()

    if not data['name']:
        return alert("O campo nome não pode estar vazio!")

    if not data['email']:
        return alert("O campo email não pode estar vazio!")

    if not data['password']:
        return alert("O campo senha não pode estar vazio!")

    if not data['password_confirm']:
        return alert("O campo confirmar senha não pode estar vazio!")

    if data['password'] != data['password_confirm']:
        return alert("As duas senhas tem que ser idênticas!")

    if not data['cpf']:
        return alert("O campo cpf senha não pode estar vazio!")

    if not data['cep']:
        return alert("O campo cep senha não pode estar vazio!")

    if not data['street']:
        return alert("O campo logradouro senha não pode estar vazio!")

    if not data['number']:
        return alert("O campo número senha não pode estar vazio!")

    return data


def create_user_record(_):
    data = validate_form_data()

    if not data:
        return

    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)

    def oncomplete(res):
        alert(res.text)

        if res.status == 201:
            go_to('/index.html')

    ajax.post(
        'http://localhost:5000/users',
        headers=headers, data=data,
        oncomplete=oncomplete
    )


btn_record = document['btn-create-record']
btn_cancel = document['btn-cancel']

form = document.querySelector('form')
form.bind('submit', lambda e: e.preventDefault())

btn_record.bind('click', create_user_record)
btn_cancel.bind('click', lambda _: go_to('/index.html'))
