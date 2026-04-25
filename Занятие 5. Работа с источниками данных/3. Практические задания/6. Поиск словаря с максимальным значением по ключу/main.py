import json


FILENAME = "input.json"


def task() -> dict:
    # TODO считать содержимое JSON файла
    with open(FILENAME, encoding="utf-8") as f:
        data = json.load(f)

    # TODO найти максимальный элемент по ключу score
    return max(data, key=lambda item:item["score"])

if __name__ == '__main__':
    print(task())
