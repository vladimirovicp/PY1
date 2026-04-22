# TODO Напишите функцию find_common_items
def find_common_items(last_week_purchases, current_week_purchases):
    set1 = set(last_week_purchases)
    set2 = set(current_week_purchases)
    general = list(set1.intersection(set2))
    general.sort()
    return general


last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']

print(f"Общие товары: {find_common_items(last_week_items, current_week_items)}")  # TODO Распечатайте общие товары
