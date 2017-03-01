#!/usr/bin/python3
# coding: utf-8

'''
Домашнее задание на пятницу (17.02.17).

Еще раз повторить материал первой лекции и по нему решить задачи:

Задача №1. Закрепляем тернарный оператор
Работа светофора запрограммирована таким образом:
1. с начала каждого часа, в течении трех минут горит зеленый сигнал,
2. следующие две минуты горит красный,
3. дальше в течении трех минут - зеленый и т. д.
Вам нужно разработать программу, которая определяет сигнал какого цвета горит в текущий момент времени.
Результат работы программы вывести на экран.
Подсказка: для получения текущего времени воспользоваться модулем datetime
from datetime import datetime
datetime.now().minute
'''

from datetime import datetime

def light():
    n = 'color'
    min = [i for i in range(1,61,1)]
    green = sorted(min[::5] + min[1::5] + min[2::5])
    if datetime.now().minute in green:
        n = 'зелёный'
    else:
        n = 'красный'
    return n

print('Цвет светофора: ',light())


print ('Green' if (datetime.now().minute % 5) < 3 else 'Red')


