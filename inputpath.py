import os
#most used directory:
default = 'Введите полный путь к папке с логфайлами: \n'
def path_setter(link, message=default, stage=False):
    if message[-1] != '\n':
        message += '\n'
    try:
        os.chdir(link)
    except FileNotFoundError:
        if not stage:
            print('Hard path not found')
        else:
            print('Cannot find the specified path')
        path_setter(input(message), message=message, stage=True)