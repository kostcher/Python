import os
import shutil

colors = {
    'error': '\033[91m',
    'end': '\033[0m'
}

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def mkdir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)

    try:
        os.mkdir(dir_path)
        print('Директория %s создана' % dir_name)
    except OSError as e:
        print(colors['error'] + e.strerror + colors['end'])


# mkdir('dir_1')
# mkdir('dir_9')


def rm(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)

    try:
        shutil.rmtree(dir_path)
        print('Директория %s удалена' % dir_name)
    except OSError as e:
        print(colors['error'] + e.strerror + colors['end'])


# rm('dir_1')
# rm('dir_9')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def ls():
    for name in os.listdir(os.getcwd()):
        print(name)


# ls()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def cpf(src, dsc):
    src_path = os.path.join(os.getcwd(), src)
    dsc_path = os.path.join(os.getcwd(), dsc)

    try:
        shutil.copy2(src_path, dsc_path)
        print('Фаил %s скопирован' % src)
    except OSError as e:
        print(colors['error'] + e.strerror + colors['end'])


# cpf('hw05_easy.py', 'hw05_easy_2.py')


def cd(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)

    try:
        os.chdir(dir_path)
        print('Директория %s выбрана' % dir_name)
    except OSError as e:
        print(colors['error'] + e.strerror + colors['end'])