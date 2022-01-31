from browser import window


def go_to(path: str):
    window.location.pathname = path


def toggle_password(eye_icon, closed_eye_icon, input):
    if eye_icon.style.display == '':
        eye_icon.style.display = 'none'

    if closed_eye_icon.style.display == '':
        closed_eye_icon.style.display = 'block'

    if eye_icon.style.display == 'none':
        eye_icon.style.display = 'block'
    elif eye_icon.style.display == 'block':
        eye_icon.style.display = 'none'

    if closed_eye_icon.style.display == 'none':
        closed_eye_icon.style.display = 'block'
    elif closed_eye_icon.style.display == 'block':
        closed_eye_icon.style.display = 'none'

    if eye_icon.style.display == 'block' and closed_eye_icon.style.display == 'none':
        input.type = 'text'
    else:
        input.type = 'password'
