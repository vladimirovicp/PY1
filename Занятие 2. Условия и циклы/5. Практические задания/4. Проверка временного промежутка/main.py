hour = 19

# TODO Реализуйте алгоритм при помощи условных операторов

if 6 <= hour < 12:
    print("Утро")
elif 12 <= hour < 18:
    print("День")
elif 18 <= hour < 24:
    print("Вечер")
elif 0 <= hour < 6:
    print("Ночь")
else:
    print("Недопустимое количество часов")