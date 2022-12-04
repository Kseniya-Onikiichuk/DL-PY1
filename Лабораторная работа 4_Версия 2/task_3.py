def delete(list_, index=None):
    # Если индекс не задан или задан индекс последнего элемента, удаляем последний элемент списка
    # В противном случае удаляем элемент с помощью слайсирования и сложения списков
    if index is None or index == -1:
        return list_[:-1]
    else:
        return list_[:index] + list_[index + 1:]


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
