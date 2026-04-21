list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
mainMax = list_numbers[0]
maxIndex = 0
# TODO Поменяйте местами значения согласно условию
for i, value in enumerate(list_numbers):
    if mainMax <= value:
        mainMax = value
        maxIndex = i


last = len(list_numbers) - 1
list_numbers[maxIndex] = list_numbers[last]
list_numbers[last] = mainMax

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
