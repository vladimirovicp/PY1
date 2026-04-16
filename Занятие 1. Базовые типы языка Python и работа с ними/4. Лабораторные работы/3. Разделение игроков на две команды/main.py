list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

width_ = int(len(list_players) / 2)

print(list_players[:width_])
print(list_players[width_:])