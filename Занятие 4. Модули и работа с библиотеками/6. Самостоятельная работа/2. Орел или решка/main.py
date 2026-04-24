import random
from random import choice
from collections import Counter

EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    # TODO подсчитать количество выпаданий орлов и решек

    side_list = []
    for _ in range(count):
        side_list.append( choice(coin) )
    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат
    dict_coin = dict(Counter(side_list))

    if dict_coin["Орел"] > dict_coin["Решка"]:
        list_freq.append(dict_coin["Решка"] / dict_coin["Орел"])
    else:
        list_freq.append(dict_coin["Орел"] / dict_coin["Решка"])

print(list_freq)
