import hashlib
import hmac


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')


def hash_password(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        'sha256', password.encode(), int_to_bytes(8), 100000)


def compare_password(pw_hash: bytes, password: str) -> bool:
    return hmac.compare_digest(
        pw_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(),
                            int_to_bytes(8), 100000)
    )
