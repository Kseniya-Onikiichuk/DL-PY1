# Импортируем содержимое модуля pprint.pprint
from pprint import pprint

# Создаем список из словарей, перебирая числа от 0 до 15 с помощью list comprehension
list_ = [{'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)} for number in range(16)]

# Печатаем список в отформатированном представлении
pprint(list_)
