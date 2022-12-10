# Импортируем содержимое модулей string и random.sample
import string
from random import sample


# Создаем функцию для генерации случайных паролей с длиной 8 символов по умолчанию
def get_random_password(n: int = 8) -> str:
    # Создаем алфавит из букв и цифр, генерируем список из алфавита и меняем тип данных на строку
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(sample(alphabet, n))


print(get_random_password())
