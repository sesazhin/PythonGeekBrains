# Задача-1:
# def create_dir(dir):
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.

# def delete_dir(dir):
# И второй скрипт, удаляющий эти папки.

import os
import sys

dir_list = ["dir_1", "dir_2", "dir_3", "dir_4", "dir_5", "dir_6", "dir_7", "dir_8", "dir_9"]

def create_dir(dir):
        if dir:
            dir_full_path = os.path.join(os.getcwd(), dir)

            try:
                os.mkdir(dir_full_path)
            except:
                print("Невозможно создать директорию")

        else:
            print("Невозможно создать директорию. Вы пытаетесь создать директорию с пустым названием!")

def delete_dir(dir):
    if dir:
        dir_full_path = os.path.join(os.getcwd(), dir)

        try:
            os.rmdir(dir_full_path)
        except:
            print("Невозможно удалить директорию")

    else:
        print("Невозможно удалить директорию. Вы пытаетесь удалить директорию с пустым названием!")


do = {
    "rmdir": create_dir,
    "mkdir": delete_dir,
}

try:
    key = sys.argv[1]
    print("key = ",key)
    if len(sys.argv) > 2:
        print("Вы передали более одного аргумента!")
        sys.exit(-1)

except IndexError:
    print("Вы не ввели ключ!")
    sys.exit(-1)

if do.get(key) and key == "mkdir":
    for dir in dir_list:
        create_dir(dir)

    print("\nВыполнение mkdir завершено!")

elif do.get(key) and key == "rmdir":
    for dir in dir_list:
        delete_dir(dir)

    print("\nВыполнение rmdir завершено!")

else:
    #print("do.get(key) = {} , key = {}".format(do.get(key),key))
    print("Вы не ввели корректный (rmdir/mkdir) ключ!")
