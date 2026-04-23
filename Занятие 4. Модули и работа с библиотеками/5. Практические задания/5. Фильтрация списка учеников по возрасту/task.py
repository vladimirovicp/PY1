def calculate_average_age(students):
    students_ages = [student["age"] for student in students]
    return sum(students_ages) / len(students_ages)

# TODO Напишите функцию filter_students_by_age

def filter_students_by_age(students, average_age):

    return [student for student in students if student["age"] < average_age]

if __name__ == '__main__':
    # Пример списка учеников
    students_list = [
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

    # Вычисление среднего возраста
    # TODO Вычислите средний возраст учеников
    students_average_age = calculate_average_age(students_list)
    print("Средний возраст учеников:", students_average_age)


    # Фильтрация учеников по возрасту
    # TODO Офильтруйте учеников
    print("Список учеников с возрастом меньше среднего:")

    list_students_average_age = filter_students_by_age(students_list, students_average_age)

    for current_student in list_students_average_age:
        print(current_student['name'])
