from browser import document

from utils import *

# Botão que leva para página de criar cadastro
btn_record = document['btn-create-record']
# Botão que leva para página de fazer login
btn_login = document['btn-login']

btn_record.bind('click', lambda _: go_to('/cadastro.html'))
btn_login.bind('click', lambda _: go_to('/login.html'))
