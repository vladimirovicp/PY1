def is_lucky_number(num: int) -> bool:
    # TODO проверить что число шестизначное и положительное

    if num > 0 and len(str(num)) == 6:
        sum1 = sum(int(n) for n in str(num)[:3])
        sum2 = sum(int(n) for n in str(num)[3:])
    else:
        raise ValueError("Число должно содержать 6 знаков и быть положительным")
    # TODO проверить счастливое число или нет
    return sum1 == sum2


print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
