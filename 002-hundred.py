#!/usr/bin/python3
# coding: utf-8

''' 
Задача №2. Закрепляем математические операторы
На садовом участке площадью 10 соток, разбили грядки 15 на 25 метров. Сколько м2 осталось незанято?
Результат работы программы вывести на экран. '''

area = 100*100 ; print('Площадь огорода:', area)
bed = 15 * 25  ; print('Площадь грядки: ', bed)
free = area % bed ; print('Осталось ' + str(free) + ' м2')
