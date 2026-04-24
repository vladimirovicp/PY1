# TODO написать функцию remove
def remove(list_data, num):

    result = None
    for i, value in enumerate(list_data):
        if value == num:
            result = i


    if result is None:
        raise ValueError("Элемента нет!")
    else:
        return list_data[:result] + list_data[result + 1:]


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
