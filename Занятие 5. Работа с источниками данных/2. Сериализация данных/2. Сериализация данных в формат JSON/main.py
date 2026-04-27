import json

filename = 'output.json'
indent = None  # TODO Подставьте любое целое число
ensure_ascii = True  # TODO Замените на значение True

data = {
    'name': 'John',
    'age': 25,
    'город': 'Нью-Йорк'
}

# Запись данных в файл в формате JSON
with open(filename, 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=" ", ensure_ascii=False)

# Сериализация данных в строку JSON
json_data = json.dumps(data, indent=" ", ensure_ascii=False)
print("Сериализация данных с помощью метода `dumps`:", json_data)

# Чтение данных из файла в формате JSON
with open(filename, encoding="utf-8") as file:
    data = json.load(file)
print("Десериализованные данные из JSON файла в python объект:", data)

# Десериализация данных из строки JSON
data = json.loads(json_data)
print("Десериализованные данные из JSON строки в python объект:", data)
