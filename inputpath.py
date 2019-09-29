import os
#most used directory:
default = 'Введите полный путь к папке с логфайлами: \n'
def path_setter(link, massage=default, stage=False):
    if massage[-1] != '\n':
        massage += '\n'
    try:
        os.chdir(link)
    except FileNotFoundError:
        if not stage:
            print('Hard path not found')
        else:
            print('Cannot find the specified path')
        path_setter(input(massage), massage=massage, stage=True)