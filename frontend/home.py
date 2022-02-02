from browser import document, window

from utils import *

# Botão que leva para página de criar cadastro
btn_record = document['btn-create-record']
# Botão que leva para página de fazer login
btn_login = document['btn-login']
# Botão que leva para página de escrever diário
btn_write_diary = document['btn-write-diary']
# Botão que leva para página de ler diário
btn_read_diary = document['btn-read-diary']
# Botão que faz logout
btn_logout = document['btn-logout']


def logout():
    window.sessionStorage.removeItem('login')
    window.sessionStorage.removeItem('user-cpf')
    window.location.reload()


btn_record.bind('click', lambda _: go_to('/cadastro.html'))
btn_login.bind('click', lambda _: go_to('/login.html'))
btn_write_diary.bind('click', lambda _: go_to('/escrever-diario.html'))
btn_read_diary.bind('click', lambda _: go_to('/ler-diario.html'))
btn_logout.bind('click', lambda _: logout())

if window.sessionStorage.getItem('login') == 'true':
    btn_record.classList.add('none')
    btn_login.classList.add('none')
    btn_write_diary.classList.remove('none')
    btn_read_diary.classList.remove('none')
    btn_logout.classList.remove('none')
