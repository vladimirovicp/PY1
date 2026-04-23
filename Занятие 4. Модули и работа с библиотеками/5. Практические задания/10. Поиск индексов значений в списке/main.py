# TODO написать функцию index
def index(list:list[int], num:int)->list[int]:

    result = [i for i, n in enumerate(list) if n == num]

    if not  result:
        raise ValueError("Значение не найдено!")

    return result



if __name__ == '__main__':
    list_items = [1, 2, "3", 1]
    print(index(list_items, 1) == [0, 3])  # True
