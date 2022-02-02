import hashlib
import hmac


def int_to_bytes(x: int) -> bytes:
    '''
    Função que transforma um número inteiro em bytes
    '''
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes: bytes) -> int:
    '''
    Função que transforma bytes em um número inteiro
    '''
    return int.from_bytes(xbytes, 'big')


def hash_password(password: str) -> bytes:
    '''
    Função que retorna uma senha criptografada
    '''
    return hashlib.pbkdf2_hmac('sha256', password.encode(), int_to_bytes(8), 100000)


def compare_password(pw_hash: bytes, password: str) -> bool:
    '''
    Função que compara uma senha criptografada com uma senha não criptografada
    '''
    return hmac.compare_digest(pw_hash, hash_password(password))
