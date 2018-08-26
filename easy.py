import os
import sys

def create_dir(dir):
        if dir:
            dir_full_path = os.path.join(os.getcwd(), dir)

            try:
                os.mkdir(dir_full_path)
                print("\nУспешно создал директорию: ",dir)
            except:
                print("\nНевозможно создать директорию",dir)

        else:
            print("\nНевозможно создать директорию. Вы пытаетесь создать директорию с пустым названием!")

def delete_dir(dir):
    if dir:
        dir_full_path = os.path.join(os.getcwd(), dir)

        try:
            os.rmdir(dir_full_path)
            print("\nУспешно удалил директорию: ", dir)
        except:
            print("\nНевозможно удалить директорию", dir)

    else:
        print("\nНевозможно удалить директорию. Вы пытаетесь удалить директорию с пустым названием!")

def list_dir():

    dir_full_path = os.path.join(os.getcwd())

    try:
        for elem in os.listdir(dir_full_path):
            print(elem)
    except:
        print("\nНевозможно прочитать содержимое директории")