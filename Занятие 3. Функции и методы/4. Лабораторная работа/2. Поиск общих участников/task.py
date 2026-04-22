# TODO Напишите функцию find_common_participants

def find_common_participants(participant1, participant2, separator = ','):
    set_participant1 = set(participant1.split(separator))
    set_participant2 = set(participant2.split(separator))
    set_participant =   set_participant1.intersection(set_participant2)
    list_participant = list(set_participant)
    list_participant.sort()


    return list_participant


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, '|')

print(result)