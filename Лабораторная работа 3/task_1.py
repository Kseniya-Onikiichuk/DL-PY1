class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """
        Возвращает название книги

        :return: Название книги
        """
        return self._name

    @property
    def author(self) -> str:
        """
        Возвращает автора книги

        :return: Автор книги
        """
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        """
        Возвращает количество страниц книги

        :return: Количество страниц книги
        """
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """
        Устанавливает количество страниц в книге

        :param new_pages: Добавляемое количество страниц в книге
        """
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        """
        Возвращает продолжительность книги

        :return: Продолжительность книги
        """
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """
        Устанавливает продолжительность книги

        :param new_duration: Добавляемая продолжительность книги
        """
        if not isinstance(new_duration, (int, float)):
            raise TypeError('Продолжительность книги должна быть задана числом int или float')
        if new_duration <= 0:
            raise ValueError('Продолжительность книги не может быть равна 0 или быть меньше 0')
        self._duration = new_duration
