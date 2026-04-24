import random

# TODO написать функцию, которая выдает трехзначное число

def generate_number():
    number_list = []
    for _ in range(3):
        number_list.append(random.randint(0,9))

    return int(''.join(map(str,number_list)))


print(generate_number())