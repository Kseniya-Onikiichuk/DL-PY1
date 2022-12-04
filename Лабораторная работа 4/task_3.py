def delete(list_, index=None):
    # Если индекс не задан или задан индекс последнего элемента, удаляем последний элемент списка
    # Если индекс положительный, удаляем элемент с помощью слайсирования
    # Если индекс отрицательный, удаляем элемент с помощью слайсирования в обратном порядке
    if index is None or index == -1:
        list_.pop()
        return list_
    elif index >= 0:
        return list_[:index] + list_[index + 1:]
    elif index < -1:
        return list_[-1:index:-1] + list_[index - 1::-1]


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
