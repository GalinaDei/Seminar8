# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import csv
import json
import os

def to_csv(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f, open('name_id.csv', 'w', encoding='utf-8') as f1:
            dct = json.load(f)
            print(dct)
            f1.write(f"{'id'}, {'name'}, {'access_level'}\n")
            for k, v  in dct.items():
                for k1, v1 in v.items():
                    print(f'{k1}, {v1}, {k}\n')
                    f1.write(f'{k1}, {v1}, {k}\n')
    else:
        print('path no exists')

if __name__ == '__main__':
    path = 'D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar8\\name_id.json'
    to_csv(path)

