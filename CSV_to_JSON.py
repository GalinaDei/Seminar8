# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена
# как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.
import json
import csv

def csv_to_js(path1, path2):
    with open(path1, 'r', newline='') as f, open(path2, 'w') as f1:
        csv_file = csv.reader(f)
        list = []
        for i, line in enumerate(csv_file):

            if i == 0:
                pass
            else:
                lst = [line[0].zfill(10), line[1].capitalize(), line[2],line[1].capitalize()+line[0].zfill(10)]
                key_list = ['id', 'name', 'access_level', 'hash']
                dct = {}
                for i in range(len(lst)):
                    dct[key_list[i]] = lst[i]
                list.append(dct)
        json.dump(list, f1)

if __name__ == '__main__':
    path1 = 'D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar8\\name_id.csv'
    path2 = 'name_id_hash_json.json'
    csv_to_js(path1, path2)