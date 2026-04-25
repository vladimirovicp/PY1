import json
FILENAME = "input.json"

# TODO решите задачу
def task() -> float:
    with open(FILENAME, encoding="utf-8") as f:
        data = json.load(f)

    res = sum( item["score"] * item["weight"] for item in data)

    return round(res,3)


print(task())
