def is_long_enough(pw):
    return len(pw) >= 8

def has_number(pw):
    return any(char.isdigit() for char in pw)

def has_uppercase(pw):
    return any(char.isupper() for char in pw)

def is_strong_password(pw):
    return is_long_enough(pw) and has_number(pw) and has_uppercase(pw)