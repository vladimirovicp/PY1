salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
summa = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

for i in range(months):
    summa = summa + salary - spend
    spend = spend + spend * increase

summa = round(-1 * summa, 2)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", summa)
