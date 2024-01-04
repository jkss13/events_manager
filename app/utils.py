import re

def validar_senha(senha):
    if 8 <= len(senha) <= 10 and re.match("^(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])", senha):
        return True
    return False

def validar_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False