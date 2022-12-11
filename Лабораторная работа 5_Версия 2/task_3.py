# Импортируем содержимое модуля random.randint
from random import randint


# Создаем функцию, которая будет возвращать список уникальных целых чисел
# Аргументами функции будут начало и конец диапазона, размер списка
def get_unique_list_numbers(start: int = -10, stop: int = 10, quantity: int = 15) -> list[int]:
    list_ = []
    # Заводим цикл, который остановится, когда длина списка будет равна заданному значению
    while True:
        if len(list_) == quantity:
            break

        # Заводим переменную, в которую генерируется случайное число
        # Если такого числа еще нет в списке, добавляем его туда
        number = randint(start, stop)
        if number not in list_:
            list_ += [number]
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
