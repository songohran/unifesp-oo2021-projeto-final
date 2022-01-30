from browser import document

from utils import *

btn_record = document['btn-create-record']
btn_login = document['btn-login']

btn_record.bind('click', lambda _: go_to('/cadastro.html'))
btn_login.bind('click', lambda _: go_to('/login.html'))
