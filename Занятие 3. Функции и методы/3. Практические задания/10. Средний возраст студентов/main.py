# TODO Напишите функцию calculate_average_age для расчета среднего возраста студентов
def calculate_average_age(students):
    total = sum(students.values())
    n = len(students)
    return round(total/n, 1)




students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}

# print(f"Средний возраст студентов: {calculate_average_age(students_dict)} лет")  # TODO Распечатайте средний возраст студентов
print(f"Средний возраст студентов: {calculate_average_age(students_dict)}")  # TODO Распечатайте средний возраст студентов