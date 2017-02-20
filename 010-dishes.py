#!/usr/bin/python3
# coding: utf-8

''' Домашнее задание на понедельник (20.02.17)

Для решения задач вам пригодится две функции:
1) print() - отображает на экран все, что ей передали
2) input() - позволяет получить введенные данные с клавиатуры
input('Количество тарелок: ') - с аргументом отображает строку приветствия (подсказки) для ввода. Возвращает всегда строку. Если нужно число, то необходимо выполнить явное приведение типов:
plates = int(input('Количество тарелок: '))

Задача №1. Закрепляем цикл while
Спросить количество тарелок и количество моющего средства.
Моющее средство расходуется из расчета 0.5 на одну тарелку.
В цикле выводить сколько моющего средства осталось после мытья каждой тарелки.
В конце вывести сколько тарелок осталось, когда моющее средство закончилось или наоборот. '''


plates = 10 # int(input('Количество тарелок: '))
cleaner = 4 # int(input('количество моющего средства: '))

while True:
    print('тарелок', plates, 'мыла', cleaner)
    plates -=1
    cleaner -=0.5
    if plates == 0:
       print('Закончились тарелки. Мыла осталось: ',cleaner)
       break 
    if cleaner == 0:
       print('Закончилось мыло. Тарелок осталось: ',plates)
       break 

print()