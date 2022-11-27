salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

# Определяем подушку безопасности
# В данном случае лучше использовать цикл с заданным количеством шагов цикла, так как у нас есть это значение
for current_month in range(months):
    delta = spend - salary
    money_capital += delta
    spend *= 1 + increase

# Выводим ответ на задачу с округлением до целого числа
print(round(money_capital))
