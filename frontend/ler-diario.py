import datetime
from browser import document, ajax, window, alert, html

from utils import go_to


def bootstrap():
    main = document.querySelector('.main')
    btn_back_to_home = document['btn-back-to-home']
    btn_back_to_home.bind('click', lambda _: go_to('/index.html'))

    cpf = window.sessionStorage.getItem('user-cpf')

    months = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
              'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

    if not cpf:
        alert('Um erro aconteceu faça logout e login para corrigir o problema')
        return

    def oncomplete(res):
        entries = res.json['entries']
        entries = entries.sort(key=lambda e: e['date'])

        for entry in entries:
            date = datetime.date.fromisoformat(entry['date'])
            date = html.H3(
                f'Dia {date.day} de {months[date.month - 1]} do ano {date.year}'
            )
            content = html.P(entry['content'].replace('\n', '<br/>'))

            main <= date
            main <= content

    ajax.get(
        f'http://localhost:5000/diaries/{cpf}',
        oncomplete=oncomplete
    )


bootstrap()
