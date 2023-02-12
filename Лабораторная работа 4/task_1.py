class Flower:
    def __init__(self, height: int, quantity: int):
        """
        Создание объекта "Цветок"

        :param height: Высота стебля в мм
        :param quantity: Количество цветков на стебле
        """
        self.height = height  # Инициализация защищенного атрибута
        self.quantity = quantity  # Инициализация защищенного атрибута

    @property
    def height(self) -> int:
        """
        Возвращает высоту стебля в мм

        :return: Высота стебля в мм
        """
        return self._height

    @height.setter
    def height(self, new_height: int) -> None:
        """
        Устанавливает высоту стебля в мм

        :param new_height: Новая высота стебля в мм
        """
        if not isinstance(new_height, int):
            raise TypeError('Введенное значение не является целым числом')
        if new_height <= 0:
            raise ValueError('Высота стебля не может быть равна 0 или быть меньше 0')
        self._height = new_height

    @property
    def quantity(self) -> int:
        """
        Возвращает количество цветков на стебле

        :return: Количество цветков на стебле
        """
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        """
        Устанавливает количество цветков на стебле

        :param new_quantity: Новое количество цветков на стебле
        """
        if not isinstance(new_quantity, int):
            raise TypeError('Количество цветков не является целым числом')
        if new_quantity <= 0:
            raise ValueError('Количество цветков не может быть равно 0 или быть меньше 0')
        self._quantity = new_quantity

    def petals(self, petals_number: int) -> None:
        """
        Устанавливает количество лепестков

        :param petals_number: Количество лепестков
        """
        if not isinstance(petals_number, int):
            raise TypeError('Количество лепестков не является целым числом')
        if petals_number <= 0:
            raise ValueError('Количество лепестков не может быть равно 0 или быть меньше 0')

    def __str__(self):
        return f"Цветок высотой {self._height} мм с количеством цветков {self._quantity}"

    def __repr__(self):
        return f"{self.__class__.__name__}(height={self._height!r}, quantity={self._quantity!r})"


class Chamomile(Flower):
    def __init__(self, height: int, quantity: int, colour: str):
        super().__init__(height, quantity)
        self._colour = colour  # Инициализация защищенного атрибута

    @property
    def colour(self) -> str:
        """
        Возвращает цвет бутонов

        :return: Цвет бутонов
        """
        return self._colour

    def petals(self, petals_number: int) -> str:
        """
        Перегрузка метода базового класса для получения конкретного результата
        Гадает по количеству лепестков в ромашке

        :param petals_number: Количество лепестков
        :return: Нечетное количество лепестков - "Любит", четное - "Не любит"
        """
        if not isinstance(petals_number, int):
            raise TypeError('Количество лепестков не является целым числом')
        if petals_number <= 0:
            raise ValueError('Количество лепестков не может быть равно 0 или быть меньше 0')
        if petals_number % 2 == 1:
            return "Любит"
        else:
            return "Не любит"

    def __str__(self):
        return f"Цветок высотой {self._height} мм с количеством цветков {self._quantity}. Цвет {self._colour}"

    def __repr__(self):
        return f"{self.__class__.__name__}(height={self._height!r}, quantity={self._quantity!r}, colour={self._colour!r})"


if __name__ == "__main__":
    flower_01 = Flower(30, 7)
    print(flower_01)  # Проверяем метод __str__ для базового класса
    print(flower_01.petals(9))  # Проверяем метод petals для базового класса
    flower_02 = Chamomile(25, 5, 'Белый')
    print(flower_02)  # Проверяем метод __str__ для дочернего класса
    flower_02.quantity = 6  # Перезаписываем значение дочернего класса с помощью методов базового класса
    print(flower_02)
    print(flower_02.petals(9))  # Проверяем метод petals для дочернего класса
    pass
