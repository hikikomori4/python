#!/usr/bin/python3
# coding: utf-8

'''Задача №1.
Написать функцию, которая возвращает количество дней, оставшихся до нового года.
Функция должна корректно работать при запуске в любом году, т. е. грядущий год должен вычисляться программно.'''

import calendar
from datetime import datetime

year = datetime.now().year 

print('Сегодня: ', datetime.now())
# Проверка високосного года
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            yeard = 365; print(year, '- обычный год')
        else:
            yeard = 366; print(year, '- високосный год!')
    else:
        yeard = 365; print(year, '- обычный год')
    return yeard

yeard = leap_year(year)

print('Количество дней:', yeard)
print('Сегодняшний день:',datetime.now().day)
print('В текущем месяце', calendar.monthrange(year, 2)[1],'дней')
print('номер текущего месяца', datetime.now().month)

# Вычислить уже прошедшие дни

months = 1
dayspass = 0

while months <= datetime.now().month: # с 1 по текущий месяц
    dayspass += calendar.monthrange(year, months)[1]
    months +=1 # добавить кол-во дней тек. месяца

months += datetime.now().day

print('С начала года прошло дней: ', dayspass)
print('До нового года осталось дней: ', yeard-dayspass)


