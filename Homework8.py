#  Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
#  Результаты обхода сохраните в файлы json, csv и pickle.
#  Для дочерних объектов указывайте родительскую директорию.
#  Для каждого объекта укажите файл это или директория.
#  Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
#  с учётом всех вложенных файлов и директорий.
#  Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import os
from pathlib import Path
import json, csv, pickle


class NotDirError(Exception):
    def __str__(self):
        return "Directory not exists"


def bypass_directory(path, obj_list=None):
    if obj_list is None:
        obj_list = []
    if not os.path.exists(path) or not os.path.isdir(path):
        raise NotDirError

    for obj in Path(path).iterdir():
        dct = {}
        if os.path.isdir(obj):
            dct['Type'] = 'directory'
        else:
            dct['Type'] = 'file'

        dct['Size'] = os.path.getsize(obj)
        parents_name = os.path.dirname(obj).split("\\")[-1]
        dct['Parents_dir_Name'] = f'{parents_name}'
        name = os.path.basename(obj).split("\\")[-1]
        dct['Name'] = name
        obj_list.append(dct)
    with open('object_list.json', 'w', encoding='utf-8') as json_f:
        json.dump(obj_list, json_f)
    with open('object_list.csv', 'w', newline='', encoding='utf-8') as csv_f:
        csv_writer = csv.writer(csv_f, dialect='excel')
        csv_f.write(f"{'Type'}, {'Size'}, {'Parents_dir_Name'}, {'Name'}\n")
        for line in obj_list:
            csv_writer.writerow(list(line.values()))
    with open('object_list.pickle', 'wb') as pickle_f:
        pickle.dump(obj_list, pickle_f)
    for obj in Path(path).iterdir():
        if os.path.isdir(obj):
            bypass_directory(os.path.join(os.path.dirname(obj), os.path.basename(obj)), obj_list)


if __name__ == '__main__':
    path = 'D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar8'
    bypass_directory(path)