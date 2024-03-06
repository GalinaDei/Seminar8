# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json


def to_json(url):
    with open(url, 'r', encoding='Utf-8') as f, open('js_file.json', 'w', encoding='Utf-8') as jf:
        data = []
        for line in f:
            data.append(line.capitalize())
        data = ''.join(data)
        json.dump(data, jf, indent=4)


url = 'D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar7\passw.txt'
to_json(url)