# TODO Напишите функцию get_oldest_participant
def et_oldest_participant(participants):
    result = max(participants, key=lambda p: p["age"] )
    return result

if __name__ == "__main__":
    participants_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]

    oldest_participant = et_oldest_participant(participants_list)  # TODO Найдите самого старшего участника
    print(oldest_participant)
