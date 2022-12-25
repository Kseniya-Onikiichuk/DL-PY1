import json

INPUT_FILE = "input.csv"


# Создаем функцию, которая будет конвертировать из csv в json
def csv_to_list_dict(filename: str, delimiter: str = ',') -> list[dict]:
    with open(filename, 'r') as f:
        # Записываем в список названия столбцов из файла
        headers_list = [word.strip() for word in f.readline().split(delimiter)]

        # Создаем список словарей, в которых ключ - название столбца, значение - значение ячейки в этом столбце
        dict_ = [dict(zip(headers_list, [num.strip() for num in line.split(delimiter)])) for line in f.readlines()]
        return dict_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
