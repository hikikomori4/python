#!/usr/bin/python3
# coding: utf-8

''' Cинопсис:
План урока Урок №3: Модули и пакеты

1. Что такое модуль?
2. Как импортировать модуль?
2.1. from или частичный импорт, *
2.2. Псевдонимы
3. Компиляция файлов
4. Стандартные модули
5. Что такое пакет?
5.1. Дистрибуция пакетов '''


# Соблюдайте правило: на один импорт - одна библиотека:
# import square_shapes
# Обращение к находящейся в библиотеке square_shapes функции
# calculate_circle_area будет таким:
# square_shapes.calculate_circle_area(n)

# Однострочные конструкции множественного импорта типа:
# import lib1, lib2 
# не рекомендуется делать, так как это снижает читаемость кода.

# однако при частичном импорте из 1го модуля возможен
# множественный импорт нескольких его функций.
# Импорт производится непосредственно в основной код, и не
# требует дополнительной адресации. Вызов функции из библиотеки
# square_shapes в данном случае будет, как если бы она была в
# теле вызывающей программы:
# calculate_circle_area(n)

# Частичный импорт всего (внутрь основного пространства имён)
# from square_shapes import *

# Частичный импорт только выбранных ф-ций (внутрь осн. пр-ва) 

from square_shapes import (
     calculate_circle_area,
     calculate_rectangle_area,
     calculate_square_area,
     calculate_triangle_area
)

print(calculate_circle_area(5))
print(calculate_square_area(2))
print(calculate_rectangle_area(2,4))
print(calculate_triangle_area(3,4,5))

# Если название модуля слишком длинное, или не нравится, то для
# него можно создать псевдоним, с помощью ключевого слова as.
# Импорт модулей, и функций из модуля под своим именем:

# import math as m
# from math import pi as PI


# ПОВТОРИМ кратко:
# Если import... то обращение включая имя библиотеки
# Если from... то прямая адресация функции.

# Описание стандартных модулей: The Python Standard Library
# https://docs.python.org/3/library/
# orderedDict - хранение словарей в упорядоченном виде
# os.path - обращение к путям вне зависимости от версии ОС.
# полезная библиотека: CSV File Reading and Writing
# https://docs.python.org/3/library/csv.html

# Почитать про модули ещё:
# https://pythonworld.ru/osnovy/rabota-s-modulyami-sozdanie-podklyuchenie-instrukciyami-import-i-from.html


# Компиляция библиотеки с оптимизацией. При запуске программы с
# ключём: python3 -O lesson04.py в подкаталоге __pycache__
# появляется оптимизированный .pyc


# Пакеты
#  Файл __init__.py используется для инициализации 2го python

print(__name__)
if __name__ == '__main__':
    print('Модуль ', __name__ ,' используется как запускаемый файл')



# Дистрибуция пакетов
#  https://pypi.org/ The Python Package Index (PyPI) is a
# repository of software for the Python programming language.
#




