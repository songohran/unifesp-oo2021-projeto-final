from browser import document, alert, ajax
import json

from utils import go_to


def get_form_data_values() -> dict:
    password = document.querySelector('input#password').value
    cpf = document.querySelector('input#cpf').value

    return {
        'password': password,
        'cpf': cpf,
    }


def validate_form_data():
    data = get_form_data_values()

    if not data['password']:
        return alert("O campo senha não pode estar vazio!")

    if not data['cpf']:
        return alert("O campo cpf senha não pode estar vazio!")

    return data


def create_user_record(_):
    data = validate_form_data()

    if not data:
        return

    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)

    def oncomplete(res):
        alert(res.text)

        if res.status == 200:
            go_to('/index.html')

    ajax.post(
        'http://localhost:5000/auth/login',
        headers=headers, data=data,
        oncomplete=oncomplete
    )


btn_login = document['btn-login']
btn_cancel = document['btn-cancel']

form = document.querySelector('form')
form.bind('submit', lambda e: e.preventDefault())

btn_login.bind('click', create_user_record)
btn_cancel.bind('click', lambda _: go_to('/index.html'))
