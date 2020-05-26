# -*- coding: utf-8 -*-
# testing sublime3

# print('it works!')

'''
import sys
for arg in sys.argv:
    print(arg)
    print(type(arg))
'''

# DZ1
# Создать модуль, в нём создать функцию создающие
# директории dir_1 - dir_9 в папке из которой запущен скипт
# и функцию удаляющую эти папки 

'''
import os

def create_folders():
	for i in range(1,10):
		folder_name = f'dir_{i}'
		os.mkdir(folder_name)

def del_folders():
	for i in range(1,10):
		folder_name = f'dir_{i}'
		os.rmdir(folder_name)


create_folders()
del_folders()
'''
# DZ 2
# создать модуль, в нём создать функцию, которая принимает список
# и возвращает из него случайный элемент. Если список пустой
# функция должная вернуть None; проверить в этом же модуле