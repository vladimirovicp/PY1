import random

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
quantity = 8
def get_random_password() -> str:
    # TODO написать функцию генерации случайных паролей
    return ''.join(random.sample(ALPHABET, quantity))


print(get_random_password())
