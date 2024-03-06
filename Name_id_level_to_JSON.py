# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.
import json
import os

def name_id_level_toJS(url):
    if os.path.exists(url):
        with open(url, 'r', encoding='utf-8') as f:
            dct = json.load(f)
    else:
        dct = {'1': {},
               '2': {},
               '3': {},
               '4': {},
               '5': {},
               '6': {},
               '7': {}}
    while True:
        print(dct)
        name = input('Enter name: ')
        while True:
            flag = False
            id = input('Enter id: ')
            for k, v in dct.items():
                if id in v.keys():
                    print('Such id exists. Enter new id: ')
                    flag = True
            if not flag:
                break

        while True:
            level = input('Enter access level: ')
            if level in dct.keys():
                break

        dct[level][id] = name
        print(dct)
        x = input('Continue? y/n')
        if x == 'n'.lower():
            break

    with open('name_id.json', 'w', encoding='utf-8') as f:
        json.dump(dct, f)


if __name__ == '__main__':
    url = 'D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar8\\name_id.json'
    dct = {1: {},
           2: {},
           3: {},
           4: {},
           5: {},
           6: {},
           7: {}}
    name_id_level_toJS(url)

