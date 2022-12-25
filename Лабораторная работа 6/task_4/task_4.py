import json

INPUT_FILE = "input.csv"


# Создаем функцию, которая будет конвертировать из csv в json
def csv_to_list_dict(filename: str, delimiter: str = ',') -> list[dict]:
    with open(filename, 'r') as f:
        # Создаем пустой список, читаем первую строку файла и записываем названия столбцов в этот список
        headers_list = []
        line_0 = f.readline()
        headers_list = [word.strip() for word in line_0.split(delimiter) if word]

        # Создаем пустой список, читаем оставшиеся строки, преобразуем их в список
        # Список состоит из списков, в которые записаны строки файла csv
        data = []
        for line in f.readlines():
            data.append([number.strip() for number in line.split(delimiter) if number])

        # Создаем список словарей, в которых ключ - название столбца, значение - значение ячейки в этом столбце
        dict_ = [{headers_list[b]: data[a][b] for b in range(len(headers_list))} for a in range(len(data))]
        return dict_

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
