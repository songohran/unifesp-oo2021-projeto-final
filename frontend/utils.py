from browser import window


def go_to(path: str):
    window.location.pathname = path
