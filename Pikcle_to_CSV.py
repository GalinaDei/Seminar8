# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import csv
import pickle
import os

def pikcle_to_csv(path1, path2):
    with open(path1, 'rb') as f1, open(os.path.join(path2, path1.split('\\')[-1]. replace('.pickle', '.csv')), 'w', newline='') as f2:
        list = pickle.load(f1)
        for i in range(len(list)):
            if i == 0:
                col_names = []
                for k, v in list[i].items():
                    col_names.append(k)
                data = csv.writer(f2, dialect='excel')
                data.writerow(col_names)
            else:
                col_names = []
                for k, v in list[i].items():
                    col_names.append(v)
                data = csv.writer(f2, dialect='excel')
                data.writerow(col_names)



if __name__ == '__main__':
    path1 = 'D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar8\Pikcle_files\\name_id_hash_json.pickle'
    path2 = 'D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar8'
    pikcle_to_csv(path1, path2)