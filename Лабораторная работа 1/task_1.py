import doctest


class Square:
    def __init__(self, side: int, thickness: float):
        """
        Создание объекта "Квадрат"

        :param side: Сторона квадрата
        :param thickness: Толщина стороны квадрата

        Примеры:
        >>> square_01 = Square(30, 5) #инициализация экземпляра класса
        """
        if not isinstance(side, int):
            raise TypeError('Введенное значение не является целым числом')
        if side <= 0:
            raise ValueError('Сторона квадрата не может быть равна 0 или быть меньше 0')
        self.side = side

        if not isinstance(thickness, (int, float)):
            raise TypeError('Толщина должна быть задана числом int или float')
        if thickness <= 0:
            raise ValueError('Толщина не может быть равна 0 или быть меньше 0')
        self.thickness = thickness

    def perimeter(self) -> int:
        """
        Функция для нахождения периметра квадрата

        :return: Значение периметра квадрата

        Примеры:
        >>> square_01 = Square(30, 5)
        >>> square_01.perimeter()
        """
        return self.side * 4


class Manicure:
    def __init__(self, finger: int, colour: str):
        """
        Создание объекта "Маникюр"

        :param finger: Номер пальца, считая с мизинца левой руки
        :param colour: Цвет или ассоциация с цветом

        Примеры:
        >>> manic_01 = Manicure(5, "green") #инициализация экземпляра класса
        """
        if not isinstance(finger, int):
            raise TypeError('Введенное значение не является целым числом')
        if finger <= 0 or finger > 10:
            raise ValueError('Номер пальца должен быть задан числом от 1 до 10')
        self.finger = finger

        if not isinstance(colour, str):
            raise TypeError('Цвет должен быть задан с помощью str')
        self.colour = colour

    def nail_colouring(self) -> dict:
        """
        Функция, которая окрашивает ноготь заданного пальца в нужный цвет

        :return: Словарь, в котором запоминается цвет каждого ногтя

        Примеры:
        >>> manic_01 = Manicure(5, "green")
        >>> manic_01.nail_colouring()
        """
        ...


class Flower:
    def __init__(self, height: int, quantity: int):
        """
        Создание объекта "Цветок"

        :param height: Высота стебля в мм
        :param quantity: Количество цветков на стебле

        Примеры:
        >>> flower_01 = Flower(30, 4) #инициализация экземпляра класса
        """
        if not isinstance(height, int):
            raise TypeError('Введенное значение не является целым числом')
        if height <= 0:
            raise ValueError('Высота стебля не может быть равна 0 или быть меньше 0')
        self.height = height

        if not isinstance(quantity, int):
            raise TypeError('Количество цветков не является целым числом')
        if quantity <= 0:
            raise ValueError('Количество цветков не может быть равно 0 или быть меньше 0')
        self.quantity = quantity

    def bud_opening(self, number: int, opening: bool) -> dict:
        """
        Функция, которая записывает в словарь, открылся ли бутон
        True - бутон открыт, False - бутон закрыт

        :param number: Номер цветка
        :raise TypeError: Если номер цветка задан не целым числом
        :raise ValueError: Если номер цветка больше количества цветков
        :param opening: Раскрытие бутона
        :raise TypeError: Если раскрытие бутона задано не булевой переменной

        :return: Словарь с описанием состояния бутонов цветков

        Примеры:
        >>> flower_01 = Flower(30, 4)
        >>> flower_01.bud_opening(2, True)
        """
        ...


if __name__ == "__main__":
  doctest.testmod() # тестирование примеров, которые находятся в документации
