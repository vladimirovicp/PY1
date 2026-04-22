# TODO Напишите функцию `is_palindrome`

def is_palindrome(str):
    str_lower = str.lower()
    str_split = str_lower.split()
    revers_str = str_split[::-1]

    for i, data in enumerate(revers_str):
        revers_str[i] = data[::-1]

    old_str = "".join(str_split)
    new_str = "".join(revers_str)

    # print(old_str)
    # print(new_str)

    if new_str == old_str:
        return True
    else:
        return False


print(is_palindrome('А роза упала на лапу Азора'))