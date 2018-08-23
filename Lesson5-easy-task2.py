# Задача-2!:
# def list_dir():
# Напишите скрипт, отображающий папки текущей директории!!.

import os

def list_dir():

    curr_dir = os.getcwd()

    try:

        for elem in os.listdir(curr_dir):

            dir_full_path = os.path.join(os.getcwd(),elem)

            if os.path.isdir(dir_full_path):
                print("directory = ",dir_full_path)
    except:
        print("Невозможно прочитать содержимое директории")

list_dir()
