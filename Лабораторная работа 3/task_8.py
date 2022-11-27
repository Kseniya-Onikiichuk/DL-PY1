money_capital = 20000  # финансовая подушка безопасности
salary = 5000  # зарплата
spend = 6000  # расходы на проживание
increase = 0.05  # рост цен

month = 0  # количество месяцев, которое можно прожить

# Определяем количество месяцев без долгов
# В данном случае лучше использовать цикл с условием, так как заранее неизвестно количество шагов цикла
while True:
    delta = spend - salary
    if delta > money_capital:
        break

    month += 1
    money_capital -= delta
    spend *= 1 + increase

print(month)  # 8
