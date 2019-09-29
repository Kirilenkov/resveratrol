import os
import pandas as pd
import numpy as np
fintab = pd.DataFrame()
# referenceDir = input('Введите полный путь к папке, в которой находится файл последовательности шкалирования. Стиль ввода X:/example:\n')
referenceDir = 'C:/Users/Kirill/Desktop/logs/file_seq'
os.chdir(referenceDir)
print('Список файлов:', os.listdir(path='.'))
referenceFile = input('Введите полное имя файла последовательности шкалирования:\n')


def headings_format(pref):
    array = []
    ref_file = open(referenceFile, 'r')
    for string in ref_file:
        if string[-1] == '\n':
            string = string[:len(string)-6]
        else:
            string = string[:len(string)-5]
        indx = string.rindex('\\')
        string = string[indx+1:]
        string = pref + string
        array.append(string)
    return array


headings = headings_format('val_')
headings2 = headings_format('aro_')
headings += headings2
headings = ['participants\stimuli'] + headings
df = pd.DataFrame(columns=headings)
print(df)


def txt_to_numpy(file_with_estims):
    file = file_with_estims
    try:
        file = open(file, 'r')
        arrayagr = []
        for string in file:
            string = string[:len(string)-1]
            try:
                indx = string.index(';')
                a = string[:indx]
                b = string[indx+1:]
                temparr = np.array([a, b], float)
                arrayagr.append(temparr)
            except ValueError:
                print('Неверный формат файла. В строке %s нет разделитя ";"' % string)
        bigarr = np.vstack(arr for arr in arrayagr)
        return bigarr
        #print(bigarr)
    except Exception:
        print('Имя введено некорректно, либо ошибка формата данных')


class Participant:
    def __init__(self, rating, name='noname'):
        if name != 'noname':
            indx1 = name.index('res')
            indx2 = name.index('OBP_')
            if name[indx2+5] == '_':
                visit = name[indx2+4]
            else:
                visit = name[indx2+4:indx2+6]
            name = name[indx1:indx1+5] + ' visit: ' + visit
        self.rating = rating
        self.name = name

    def numpy_to_excel(self):
        num_of_raws = len(self.rating)
        num_of_columns = len(self.rating[0])
        particEstims = [self.name]
        for i in range(num_of_columns):
            for j in range(num_of_raws):
                particEstims.append(self.rating[j][i])
        return particEstims


# rootdir = input('Введите полный путь к папке с файлами оценок. Стиль ввода X:/example:\n')
rootdir = 'C:/Users/Kirill/Desktop/logs/logs'
os.chdir(rootdir)
flist = os.listdir(path='.')
print('Список файлов:', flist)

i = 0
for file_name in flist:
    scaling = txt_to_numpy(file_name)
    obj = Participant(scaling, file_name)
    df.loc[i] = obj.numpy_to_excel()
    i += 1
    # Если объекты потребуется использовать повторно, то можно будет сохранить их в массив.
os.chdir(path='..')
writer = pd.ExcelWriter('scaling.xlsx')
df.to_excel(writer, index=False)
writer.save()