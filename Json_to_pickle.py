# Напишите функцию, которая ищет json файлы в указанной директории и
# сохраняет их содержимое в виде одноимённых pickle файлов.
import json
import os
import pickle


class NotDirError(Exception):
    def __str__(self):
        return "Directory not exists"

def json_to_pickle(dir_name1, dir_name2):
    if not os.path.exists(dir_name1) or not os.path.isdir(dir_name1):
        raise NotDirError

    for file_name in os.listdir(dir_name1):
        if file_name.endswith('.json'):
            with open(os.path.join(dir_name1, file_name), 'r', encoding='utf-8') as f:
                data = json.load(f)
            with open(os.path.join(dir_name2, file_name.replace('.json', '.pickle')), 'wb') as f1:
                pickle.dump(data, f1)

if __name__ == '__main__':
    path = 'D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar8'
    path2 = 'D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar8\Pikcle_files'
    json_to_pickle(path, path2)
