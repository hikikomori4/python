#!/usr/bin/python3
# coding: utf-8

import os
import sys
from datetime import datetime

try:
    os.system('clear')
except:
    os.system('cls')


# Задание массива задач #############################3
tasks = {
         
        }

data = {
    'tasks':  [
        {
	    'id': 1,
	    'status': 'executed',
	    'name': 'Урок Python',
	    'body': 'Содержимое задачи...',
	    'time': ('2017-03-01', '18:40')
	    
	},
    ]
}


# Вывод задач #################################

def task_list():
    
    print(data)
    

# Добавление задачи ###############################

def task_add():
    id   = int(input('Введите ID задачи: '))        
    time = (input('Введите время задачи: '))        
    name = (input('Введите имя задачи: '))        
    body = (input('Введите саму задачу: '))        
    status = 'not_executed'
    
    print('\n  ID: ',id,'\nTiME:', time,'\nNAME:', name, '\nTEXT:', body, '\n')


# Редактирование задачи ##############################

def task_edit():
    print('Редактирование задачи')
    
    
# Завершение задачи #######################################

def task_end():
    print('Завершение задачи')
    
        
# Возобновление задачи ######################

def task_resume():
    print('Возобновление задачи')


# Главное меню ####################################

def main_menu():

    print('\n---------------------------------------')
    print('Сегодня: ', datetime.now())
    print('Ежедневник. Выберите действие:')
    print('---------------------------------------')
    print('''
 1. Вывести список задач
 2. Добавить задачу
 3. Отредактировать задачу
 4. Завершить задачу
 5. Начать задачу сначала
 6. Выход
''')
    n = int(input('Введите число: '))

    if n == 1:
        print('\nСписок задач:\n')
        print(task_list())
    elif n == 2:
        print('Добавление задачи...\n')
        task_add()
    elif n == 3:
        print('Редактирование задачи...')
        task_edit()
    elif n == 4:
        print('Завершение задачи...')
        task_end()
    elif n == 5:
        print('Возобновление задачи...')
        task_resume()
    elif n == 6:
        print('Выход...')
        sys.exit(0)
    else:
        print('Неверный ввод, повторите.')


# Основной говнокод #####################################

while True:
    main_menu()
