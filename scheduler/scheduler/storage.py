#!/usr/bin/python3
# coding: utf-8

import sqlite3


SQL_SELECT = '''
    SELECT
        id, title, body, time, status
    FROM
        scheduler
    '''

def dict_build(cursor, row):
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    return d


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_build
    return conn


def initialize(conn):
    with conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS scheduler (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                title TEXT NOT NULL,
                body TEXT NOT NULL DEFAULT '',
                time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                status TEXT NOT NULL DEFAULT 'Open'
            )
        ''')


def task_print(task):
    print('{task[id]} - {task[title]} - {task[body]} - {task[time]} - {task[status]}'.format(task=task))


def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT)
        return cursor.fetchall()


def task_add(conn):
    cursor = conn.execute('''
    INSERT INTO scheduler (id, title, body, time) 
    VALUES (?,?,?,?)
    ''', (
    int(input('Введите № события: ')),
    input('Введите его название: '),
    input('Введите текст: '),
    input('Введите дату\время (гггг-мм-дд чч:мм): ')
         )
    )
    return cursor.lastrowid


def task_edit(conn):
    task_current = task_select(conn)
    task_print (task_current)
    cursor = conn.execute('''
    UPDATE scheduler 
    SET id = ?, title = ?, body = ?, time = ? 
    WHERE id = ?
    ''', (
    int(input('Введите № события: ')),
    input('Введите его название: '),
    input('Введите текст: '),
    input('Введите дату\время (гггг-мм-дд чч:мм): '),
    task_current['id']
        )
    )
    return task_current['id']


def task_delete(conn):
    task = task_select(conn)
    cursor = conn.execute('DELETE FROM scheduler WHERE id = ?', \
    (task['id'],))
    return task['id']


def task_select(conn):
    task_id = int(input('Введите № задачи: '))
    with conn:
        cursor = conn.execute(SQL_SELECT + ' WHERE id = ?', \
        (task_id,))
        return cursor.fetchone()


def task_switch(conn, status):
    task_current = task_select(conn)
    conn.execute('UPDATE scheduler SET status = ? WHERE id = ?',\
    (status, task_current['id']))
    return task_current['id']



'''
Использованные материалы:

The Python Standard Library
https://docs.python.org/3/library/

Официальная документация по модулю sqlite3
https://docs.python.org/3/library/sqlite3.html

CREATE TABLE - создание таблицы
https://www.tutorialspoint.com/sqlite/sqlite_create_table.htm

INSERT - вставка данных в таблицу
https://www.tutorialspoint.com/sqlite/sqlite_insert_query.htm

UPDATE - обновление данных в таблице
https://www.tutorialspoint.com/sqlite/sqlite_update_query.htm




'''
