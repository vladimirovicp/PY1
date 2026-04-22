# TODO реализовать функцию
def insert(list, value, index = 0):

    # print(list, value,  index)

    new_list = []

    for i, v in enumerate(list):
        if i == index:
            new_list.append(value)
            new_list.append(v)
        else:
            new_list.append(v)

    if index + 1  > len(list):
        new_list.append(value)

    return new_list


print(insert([1], value=0))  # [0, 1]
print(insert([0, 2], value=1, index=1))  # [0, 1, 2]
print(insert([0, 1, 2], value=3, index=3))  # [0, 1, 2, 3]
