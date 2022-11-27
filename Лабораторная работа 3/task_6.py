list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Задаем переменные для хранения информации об индексе максимального элемента и о самом элементе
max_index = 0
max_number = list_numbers[max_index]

# Находим индекс последнего максимального элемента, итерируя входной список
for i, current_number in enumerate(list_numbers):
    max_number = list_numbers[max_index]
    if current_number >= max_number:
        max_index = i
        max_number = list_numbers[max_index]

# Меняем местами последний максимальный и последний элементы с помощью множественного присваивания
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
