#!/usr/bin/python3
# coding: utf-8

# Импорт модуля целиком
# import math

# Импорт функции из модуля
#from math import pi

# Импорт функции из модуля под своим именем
from math import pi as PI

def calculate_square_area(a):
    return a ** 2
    
def calculate_rectangle_area(a, b):
    return a * b
    
def calculate_triangle_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p-a) * (p -b) * (p-c)) ** 0.5
    
def calculate_circle_area(r):
    return PI * r ** 2
    
    
# Список того, что будет импортировано из этого модуля по звездочке:
# from square_shapes import *
# Остальное импортированно не будет!!!!

__all__ = [
'calculate_square_area',
'calculate_rectangle_area',
'calculate_triangle_area',
'calculate_circle_area'
]

# Проверка, запускается модуль как отдельная программа, 
# или вызывается из другой:

print('Имя модуля: ', __name__)

if __name__ == '__main__':
    print('Модуль используется как запускаемый файл')

