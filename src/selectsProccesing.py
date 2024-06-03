##import pandas as pd # type: ignore
import os
import glob

directory = '../put_data_here/'

# Нахождение всех .txt файлов в этой директории
text_files = glob.glob(os.path.join(directory, '*.txt'))

# Словарь для хранения результатов
where_clauses = {}

# Перебор всех файлов
for file_path in text_files:
    with open(file_path, 'r') as file:
        content = file.read()
        
        # Разделение содержимого на отдельные SQL запросы
        queries = content.split(';')
        
        # Обработка каждого запроса отдельно
        for query in queries:
            where_index = query.upper().find('WHERE')
            
            if where_index != -1:
                # Выделение части запроса после 'WHERE'
                where_clause = query[where_index + 5:]  # +5 для пропуска самого слова 'WHERE'
                
                # Очистка и обрезка условий WHERE до следующего ключевого SQL слова или до конца строки
                for keyword in ['>', '<', '=']:
                    keyword_index = where_clause.upper().find(keyword)
                    if keyword_index != -1:
                        where_clause = where_clause[:keyword_index]
                        break
                
                # Сохранение извлеченной части в словарь
                where_clauses[os.path.basename(file_path)] = where_clauses.get(os.path.basename(file_path), []) + [where_clause.strip()]

# Вывод извлеченных частей условий WHERE
for filename, clauses in where_clauses.items():
    print(f"{filename}:")
    for clause in clauses:
        print(clause)
    print()  # Добавляет пустую строку для разделения вывода по файлам
        




