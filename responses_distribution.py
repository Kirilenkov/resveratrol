import os
from inputpath import path_setter
message =  'Введите полный путь к папке с файлами статистики ответов: '
hard_path = 'C:/Users/Kirill/Desktop/results'
path_setter(hard_path, message=message)
print(os.listdir(path='.'))