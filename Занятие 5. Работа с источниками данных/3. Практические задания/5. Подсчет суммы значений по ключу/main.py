import json


FILENAME = "input.json"


def task() -> int:
    # TODO Десериализуйте содержимое JSON файла
    with open(FILENAME, encoding="utf-8") as f:
        data = json.load(f)


    # TODO Просуммируйте все значения по ключу contains_improvement_appeals
    res = 0
    for contains_improvement_appeals in data:
        res += contains_improvement_appeals['contains_improvement_appeals']

    return res


if __name__ == '__main__':
    print(task())
