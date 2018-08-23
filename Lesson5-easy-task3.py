# Задача-3:
# def get_file_copy():
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import shutil

def get_file_copy():
    file_to_copy = sys.argv[0]
    backup_file = sys.argv[0]+"_copy"

    try:
        shutil.copy(file_to_copy,backup_file)
        print("Бэкап файла создан в: {}".format(backup_file))
    except:
        print("Не удалось создать бэкап файл!")

get_file_copy()