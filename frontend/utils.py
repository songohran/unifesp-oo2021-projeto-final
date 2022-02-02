from browser import window


def go_to(path: str):
    '''
    Função utilizada para navegar no site
    Exemplos:

        Supondo que o nome do host do site seja localhost:8000

        go_to('/pagina.html') vai navegar para http://localhost:8000/pagina.html

        go_to('/index.html') vai navegar para http://localhost:8000/index.html
    '''
    window.location.pathname = path


def toggle_password(eye_icon, closed_eye_icon, input):
    '''
    Função utilizada para deixar a senha visível e invisível, também alterna entre o ícone de olho aberto e fechado
    '''
    # Garantindo que ícone de olho aberto não apareça em primeiro momento
    if eye_icon.style.display == '':
        eye_icon.style.display = 'none'

    # Garantindo que ícone de olho fechado apareça em primeiro momento
    if closed_eye_icon.style.display == '':
        closed_eye_icon.style.display = 'block'

    # Se ícone de olho aberto estiver invisível faço-o visível caso contrário faço-o invisível
    if eye_icon.style.display == 'none':
        eye_icon.style.display = 'block'
    elif eye_icon.style.display == 'block':
        eye_icon.style.display = 'none'

    # Se ícone de olho fechado estiver invisível faço-o visível caso contrário faço-o invisível
    if closed_eye_icon.style.display == 'none':
        closed_eye_icon.style.display = 'block'
    elif closed_eye_icon.style.display == 'block':
        closed_eye_icon.style.display = 'none'

    # Se ícone de olho aberto estiver visível e o ícone de ohlo fechado estiver invisível então mostre a senha, senão escondaa senha
    if eye_icon.style.display == 'block' and closed_eye_icon.style.display == 'none':
        input.type = 'text'
    else:
        input.type = 'password'
