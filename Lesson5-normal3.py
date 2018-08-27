import sys
import os

import easy

def change_dir(dir):
    if dir:
        dir_full_path = os.path.join(os.getcwd(), dir)

        print("dir_full_path = ",dir_full_path)

        try:
            os.chdir(dir_full_path)
            print("\nУспешно перешёл в директорию: ",dir)

        except:
            print("\nНевозможно перейти в директорию")

    else:
        print("\nНевозможно создать директорию. Вы пытаетесь создать директорию с пустым названием!")

dir_actions = ["1","3","4"]
no_args = ["2"]

do = {
    "1": change_dir,
    "2": easy.list_dir,
    "3": easy.delete_dir,
    "4": easy.create_dir
}

input_first = 1

while True:
    try:
        if input_first:
            action = sys.argv[1]
            #print("action = ",action)
        else:
            #print("action = ",action)
            action = input("\nВведите действие, которое Вы хотели бы выполнить:\n1. Перейти в папку\n2. Просмотреть содержимое текущей папки\n3. Удалить папку\n4. Создать папку\n5. Выйти\n")

    except IndexError:
        action = None #empty string

    if action in dir_actions:
        dir_name = input("Введите название директории: ")
        do[action](dir_name)

    elif action in no_args:
        do[action]()

    elif action == "5":
        sys.exit()

    else:
        print("do.get(action) = {} , action = {}".format(do.get(action),action))
        print("Параметр не задан либо не 1-5! Попробуйте ещё раз!\n")

    input_first = 0