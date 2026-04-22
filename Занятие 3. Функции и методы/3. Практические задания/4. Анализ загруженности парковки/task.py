# TODO Напишите функцию `calculate_parking_load`

def calculate_parking_load(total_parking_spaces, occupied_parking_spaces):
    load_percentage = (occupied_parking_spaces / total_parking_spaces) * 100
    return round(load_percentage)

total = 150
occupied = 37
result = calculate_parking_load(total, occupied)
print(f"Загруженность парковки: {result}%")