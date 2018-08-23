# Задача-2:
# def list_dir():
# Напишите скрипт, отображающий папки текущей директории.

import os

def list_dir():

    dir_full_path = os.path.join(os.getcwd())

    try:
        for elem in os.listdir(dir_full_path):
            print(elem)
    except:
        print("Невозможно прочитать содержимое директории")

list_dir()