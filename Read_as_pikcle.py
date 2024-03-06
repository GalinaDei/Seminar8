# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.
import pickle

path = 'D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar8\\name_id_hash_json.csv'
with open(path, 'r', encoding='utf-8') as f:
    data = []
    for line in f:
        data.append(line)
    print(pickle.dumps(data))
