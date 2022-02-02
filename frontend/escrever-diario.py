import json
from browser import document, alert, window, ajax

from datetime import date

from utils import go_to


def save_diary_entry(date_input, textarea_diary_entry_content):
    cpf = window.sessionStorage.getItem('user-cpf')
    date_str = date_input.value
    diary_entry_content = textarea_diary_entry_content.value

    if not cpf:
        alert('Um erro aconteceu faça logout e login para corrigir o problema')
        return

    if not date_str:
        alert('Não pode atualizar o diário sem definir uma data')
        return

    headers = {'Content-Type': 'application/json'}
    data = {
        'date': date_str,
        'content': diary_entry_content
    }
    data = json.dumps(data)

    def oncomplete(res):
        alert(res.text)

        if res.status == 200:
            go_to('/index.html')

    ajax.patch(
        f'http://localhost:5000/diaries/entries/{cpf}',
        headers=headers, data=data,
        oncomplete=oncomplete
    )


date_input = document.querySelector('input[type="date"]')
date_input.value = date.today()

textarea_diary_entry_content = document['diary-entry-content']

btn_save_diary_entry = document['btn-save-diary-entry']
btn_save_diary_entry.bind(
    'click',
    lambda _: save_diary_entry(date_input, textarea_diary_entry_content)
)

btn_cancel = document['btn-cancel']
btn_cancel.bind('click', lambda _: go_to('/index.html'))
