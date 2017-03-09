#!/usr/bin/python3
# coding: utf-8

import sys
import os
from datetime import datetime
from scheduler import storage

conn = storage.connect('scheduler.db')
storage.initialize(conn)


# оформляющий декоратор
def decor_header(func):
    def wrapper(*args, **kwargs):
        result = func()
        print('\n\x1b\x5b\x32\x6dЗадача № {} {}.\x1b\x5b\x30\x6d\n'.format(result[1], result[0]))
    return wrapper


def task_list():
    tasks = storage.find_all(conn)
    print('\n\x1b\x5b\x32\x6d--- Список задач -------------------------------\nid - title - task - body - time - status\x1b\x5b\x30\x6d \n')
    for task in tasks:
        storage.task_print(task)
    print('\n')

@decor_header
def task_add():
    return 'добавлена', storage.task_add(conn)

@decor_header
def task_edit():
    return 'изменена', storage.task_edit(conn)

@decor_header
def task_delete():
    return 'удалена', storage.task_delete(conn)

@decor_header
def task_close():
    return 'закрыта', storage.task_switch(conn, 'Close')

@decor_header
def task_open():
    return 'открыта', storage.task_switch(conn, 'Open')

    
def action_exit():
    conn.close()
    print('\nЗавершение программы...\n')
    sys.exit(0)
   

def show_menu():
    try:
        os.system('clear')
    except:
        os.system('cls')
    print('Ежедневник. Сегодня:', datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M'))
    print('''
 1) Вывести список задач
 2) Добавить задачу
 3) Отредактировать задачу
 4) Удалить задачу
 5) Завершить задачу
 6) Начать задачу сначала
 m) Показать это меню
 q) Выйти
    ''')
    
actions = {
    '1': task_list,
    '2': task_add,
    '3': task_edit,
    '4': task_delete,
    '5': task_close,
    '6': task_open,
    'm': show_menu,
    'q': action_exit
    }
    
    

if __name__== '__main__':
    show_menu()

    while True:
        cmd = input('\x1b\x5b\x37\x6d1\x1b\x5b\x30\x6d-List \x1b\x5b\x37\x6d2\x1b\x5b\x30\x6d-Add \x1b\x5b\x37\x6d3\x1b\x5b\x30\x6d-Edit \x1b\x5b\x37\x6d4\x1b\x5b\x30\x6d-Del \x1b\x5b\x37\x6d5\x1b\x5b\x30\x6d-Terminate \x1b\x5b\x37\x6d6\x1b\x5b\x30\x6d-Resume \x1b\x5b\x37\x6dm\x1b\x5b\x30\x6denu \x1b\x5b\x37\x6dq\x1b\x5b\x30\x6duit  ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('\nНеизвестная команда\n')


'''
Использованные ссылки:
https://ru.wikibooks.org/wiki/Учебник_Python/Дата_и_время 

Пример, на основе которого писалась программа ежедневник
https://bitbucket.org/cdpo-itmo/python2017-1/src/c55456dc4a22721464addc5e8e923f7af5851841/url-shortener/?at=master

'''
