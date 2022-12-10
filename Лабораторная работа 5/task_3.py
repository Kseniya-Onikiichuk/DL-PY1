# Импортируем содержимое модуля random.shuffle
from random import shuffle

# Задаем значения переменным: диапазону случайных чисел и размеру списка
start = -10
stop = 10
quantity = 15


# Создаем функцию, которая будет возвращать список уникальных целых чисел
def get_unique_list_numbers() -> list[int]:
    list_ = [number for number in range(start, stop + 1)]

    # Перемешиваем значения в сгенирированном списке, ограничиваем размер списка слайсированием
    shuffle(list_)
    return list_[:quantity]


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
