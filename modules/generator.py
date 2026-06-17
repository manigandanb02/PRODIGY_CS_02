import secrets
import string


def generate_password(length: int = 16) -> str:
    if length < 8:
        length = 8

    if length > 64:
        length = 64

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%&*"

    password_chars = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_chars = uppercase + lowercase + digits + symbols

    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)
