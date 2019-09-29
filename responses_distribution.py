import os
import pandas as pd
from inputpath import path_setter
message =  'Введите полный путь к папке с файлами статистики ответов: '
hard_path = 'C:/Users/Kirill/Desktop/results/res'
path_setter(hard_path, message=message)
files = os.listdir(path='.')
print('File list: ')
for i in files:
    print(i)


class Participant:

    def __init__(self, name, values):
        self.name = name
        self.values = values

    def add_to_df(self, df):
        df[self.name] = self.values

headings = []
objects = []
for file in files:
    if file == files[0]:
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                headings.append(line.split(':')[0])
    par = file.find('res')
    visit = file.find('BP_')
    name = 'par_' + file[par + 3 : par + 5] + '_visit_' + file[visit + 3]
    with open(file, 'r', encoding='utf8') as f:
        values = []
        for line in f:
            values.append(line.split(':')[1][1:-1])
        objects.append(Participant(name=name, values=values))

df = pd.DataFrame(index=headings)
for obj in objects:
    obj.add_to_df(df)

print(df)

os.chdir(path='..')
writer = pd.ExcelWriter('responses.xlsx')
df.to_excel(writer, index=True)
writer.save()