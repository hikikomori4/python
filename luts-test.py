#!/usr/bin/python3
# coding: utf-8
# Другой вариант указания кодировки:
# -*- coding: utf-8 -*-
# Форумы: http://python.su/forum/
# Документация по питону: http://slav0nic.org.ua/static/books/python/

# Автозапуск этой програмы после сохранения
# так
# while true; do inotifywait -qqe close_write test.py; ./test.py; done;
# или
# while true; do inotifywait -qqe close_write test.py; pkill -f 'python3 test.py'; echo -e '\n***\n'; { python3 test.py& }; done

# В одинарных ковычках '' строки (str)
# В квадратных скобках [] списки (list)
# В фигурных скобках {} словари (dict)
# В круглых скобках () кортежи (tuple)

# Основные базовые типы данных в языке Python делятся на:
# Неизменяемые (числа, строки, кортежи, фиксированные множества)
# Изменяемые (списки, словари, множества)

# две звездочки ** – возведение в степень

# input("Press any key to exit") # ожидание any key

import sys
import os
import lib
# или
# from lib import title
# и прямое обращение к переменной print(title)
try:
    os.system('clear')
except:
    os.system('cls')

print(lib.title)


exec(open('lib.py').read())

u1 = u"Unicode literal"
u2 = u'\u0410\u0434\u0440\u0435\u0441'
s5 = '\x73\65\65'
s6 = b'sp\x01am' # Строки байтов в версии 3.0
s2 = r'\1\2\t' #  вывод как есть. Спецсимволы не обрабатываются.

print('knight"s', "knight's") # Ковычки в середине строки
print('knight\'s', "knight\"s") # экранирование ковычек слешем \

s4 = """Перевод
строки"""

print (u1, "\n", u2)
print (s5,s4,s2)

print ("A" + "B","A"*5, "%s" % "A")

s = "This is parta!"; print(s)
print (s.split(' ')) # разбить содержимое s по разделителю ' '.
s.join(s); print(s)  # Снова объединить в строку.
lst = s.upper()      # Преобразование символов в верхний регистр
print (lst)
sys.exit(0)
a = 'The Matrix has You\n\n'
a=a.rstrip();print(a)  # Удаление лишних переводов строк
print(a.endswith('You')) # Оканчивается ли строка на 'You'?
print(a.startswith('The')) # Начинается ли строка с 'The'?
print('Matrix' in a) # Присутствует ли 'Matrix' в строке?



g = "Старый пример."
g = g.replace("Старый", "Новый")
print (g)

print ("Это слово я повторю"+" трижды"*3)

import math
print ('Это число Пи',math.pi,'здец, товарищи!')
print ('Ф-ция math.pi выводит всего', len(str(math.pi)), 'первых цифр числа Пи.')

import random
print('Случайный бросок кубика:', random.choice([1, 2, 3, 4, 5, 6]))

# Строки. Функции и методы строк
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

s = 'Буковки'

print('поле'[:-1])  # Вывод без последнего символа 
print('победы'[2:]) # Вывод без первых двух символов

print(s[0])  # вывод первой буквы слова
print(s[-1]) # вывод последней буквы слова
print(s[-1]) # вывод последней буквы слова
print(s[len(s)-1]) # вывод последней буквы слова (сложнее)
print(s[0:3])  # Вывод со смещения 0 и до 2 (не 3)
               # «извлечь из s все, начиная со смещения 0 
               # и до смещения J, но не включая его»
print(s[1:])   # Все, кроме первого элемента. Или (1:len(S))
print(s[0:6])  # Все, кроме последнего элемента. Или (s[:6])
print(s[:-1])  # Все, кроме последнего элемента, но проще (0:-1)
print(s[:])    # Все содержимое s, как обычная копия (0:len(S))

print(s[0:3] + s[3:7]) # Конкатенация - соединение фрагментов
print (s * 3) # Повторение
# Плюс "+" для чисел – сложение, а для строк – конкатенация.

s = 'Л' + s[1:] # Замена 1й буквы в переменной.
print(s)

f='ков'

print(s.find(f)) # поиск начала смещения подстроки
print(s.find(f)+len(f)) # прибавление к нему её длины
print(s[s.find(f):s.find(f)+len(f)]) # поиск фрагмента в слове
print(s.replace('вк', 'вочк') ) # поиск и замена фрагмента



print (s.isalpha()) # Проверка буквенная ли строка s
print (s.isdigit()) # Проверка цифровая ли строка s

line = '       aaa,bbb,ccccc,dd\n'
print(line)
line = line.strip() # Удаляет пробельные символы.
line = line.lstrip() # Удаляет пробельные символы слева\в начале
line = line.rstrip() # Удаляет пробельные символы справа\в конце
print(line)


# Строковой метод подстановки. Не вкурил.
# https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html

print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))
print('Hello, {}!'.format('Vasya'))

#ф-ция возвращает список всех доступных атрибутов объекта.
# print(dir(f)) 

print('Табуляция:\tконец строки:\n')
print(ord('\n'), ord(' '), ord('\t')) # вывести коды символов.


# Слишком сложно, не понял куда его
import re
match = re.match('Hello[ \t]*(.*)world', 'Hello crazy Python world')
print(match.group(1),'\n')


# Списки - являются аналогом массивов в других языках прогр-ния.
# Функции и методы списков
# https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html


#  создание списка
spsk = ['Смерть','Поросёнок', 'Пётр', 'Голод','Чума']
print(spsk) # вывод списка со всеми скоочками и ковычками
print(*spsk) # вывод списка без лишних символов.

spsk.append('Война') # Добавление нового объекта в конец списка 
spsk.pop(1) # Удаление объекта. Вариант: del spsk[1]
spsk.remove('Пётр') # Удаление по имени
spsk.insert(0,'Сатана Адский')
print(spsk[0]) # вывод элемента по индексу.
spsk.sort()  # алфавитная сортировка (изменяет сам список)
spsk.reverse() # обратная сортировка

spsk.clear() # очистка списка. Apocalypse Now!
# print(spsk) # А нечего уже показывать =)

#  создание ВЛОЖЕННЫХ списков

matr = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print(matr[0]) # отобразить строку 1
print(matr[1][1]) # отобразить 2й элемент из строки 2
print([row[1] for row in matr]) # отобразить только 2ю колонку
print ([row[2] + 10 for row in matr]) # +10 ко всем числам
                                      # в колонке 3.
print([row[2] for row in matr if row[1] % 2 == 0])
                 # вывести только НЕчётные значения колонки 3.
print([row[2] for row in matr if row[1] % 2 != 0])
      # вывести только чётные значения колонки 3.
      # операция деления по модулю – % (остаток от деления)

print([matr[i][i] for i in [0, 1, 2]])
      # вывод по диагонали от 1 к 9.

dbl = [c * 2 for c in 'double']
print(dbl) # дублирование букв в слове.

# форматированный вывод списка через запятую:
print('%s.' % ',' .join(dbl)) 



# Cловари

print('\n')
d = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(d['food']) # Получить значение, связанное с ключом food
d['quantity'] += 1 # Прибавить 1 к значению ключа quantity
print(d)

d2 ={} # Создание пустого словаря
d2['name'] = 'Max' # В результате присваивания создается name
d2['job'] = 'progr'
d2['age'] = 39
print(d2)

d3 = {'name': {'first': 'Bob', 'last': 'Smith'},
      'job': ['dev', 'mgr'],
      'age': 40.5}
print(d3['name']) # Name – это вложенный словарь
print(d3['name']['last']) # Обращ к элмнту вложенного словаря
d3['job'].append('janitor') # Расширение списка должностей Боба
print(d3['job']) # Job – это вложенный список
print(d3['job'][-2]) # Обращение к элементу вложенного списка mgr

print(list(d3.keys()))


# обход всех символов в строке и вывод их в верхнем регистре:
for c in 'spam':
    print(c.upper())

#  циклическое повторение spam 4,3,2, и 1 раз.
x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

# Вычисление квадратов чисел 1-5 двумя способами:

squares = [x ** 2 for x in [1, 2, 3, 4, 5]] 
print(squares)

squares = []
for z in [1, 2, 3, 4, 5]:
    squares.append(z ** 2)
print(squares)

z = 1, 2, 3, 4, 5
print(z)
if not 6 in z:
    print('6 missing')

# Кортежи

tuple = (1,2,3,4) # Кортеж из 4 элементов
tuple = tuple + (5,6) # Конкатенация к кортежу
print(tuple, 'Длина кортежа: ', len(tuple))
print(tuple[5]) # Извлечение элемента из кортежа

print(tuple.index(6)) # в какой позиции по счёту с 1-цы
                      # находится число 6.
print(tuple.count(4)) # подсчёт сколько 4-рок в кортеже.

# кортежи способны хранить объекты разных типов 
# и допускают возможность вложения:
tuple = ('spam', 3.0, [11, 22, 33])
print(tuple[2][0]) # вывод вложенного объекта 0 из объекта 2


# Файлы

fl = open('data.txt', 'w') # Создается новый файл для вывода
fl.write('\nАз есмь содержимое файла\n') # Запись строки байтов в файл
fl.close() # Закрывает файл и выталкивает выходные буферы на диск

fl = open('data.txt') # r – режим доступа к файлу по умолчанию
text = fl.read() # Файл читается целиком в строку

print(text)

print(text.split()) # Разбитие переменной на отдельные слова


flb = open('data.bin', 'rb').read() # Открытие бинарного файла
print(flb)

l = [None] * 10 # Забить l  десяткой значений None
print (l)

# r'' указывает на неформатированную строку, чтобы символы в
# пути не были восприняты как управляющие коды \n и \t
myfile = open(r'C:\new\text.dat', 'w')

# Или дублировать слэши:
myfile = open('C:\\new\\text.dat', 'w')

# Проверки типа переменной

print(type(l)) # Определить тип переменной l
print (type(type(l))) # вывести тип переменной type ^_^

if type(d2) == type({}): # Проверка типа, если есть необходимость
    print('d2 is dict')
if type(l) == list:      # Или == str,list,tuple,dict,bytes
    print('l is list')
if isinstance(l, list):  # Проверка в объектно-ориентир-м стиле
    print('l is list')



# Классы, определяемые пользователем


class Worker:
    def __init__(self, name, pay): # Инициализация при создании
        self.name = name           # self – это сам объект
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1] # Разбить строку по пробелу 
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)  # Обновить сумму выплат


bob = Worker('Bob Smith', 50000) # Создаются 2 экз и для каждого
sue = Worker('Sue Jones', 60000) # опред. имя и сумма выплат

print(bob.lastName()) # Вызов метода: self – это bob
print(sue.lastName()) # self – это sue
sue.giveRaise(.10) # Обновить сумму выплат для sue
print(sue.pay)


# Числа


print(13) # Число 13 записанное в десятичной форме
print(0x0d) # Число 13 записанное в шестнадцатеричном виде
print(0o15) # Число 13 в восьмеричном виде
print(0b00001101) # Число 13 в бинарном виде

# указать систему счисления можно во 2м параметре int:
print(int('64')) # Число 64 записанное в десятичной форме
print(int('100', 8)) # число 64 в восьмеричном виде
print(int('40', 16))  # число 64 в шестнадцатеричном виде
print(int('1000000', 2)) # число 64 в бинарном виде

# Преобразовать десятичное число 13 в hex, oct, bin
n = 13
print(hex(n))
print(oct(n))
print(bin(n))

print(oct(0x0d)) # изврат - преобразовать hex в oct

# a=int(input()) # Запрос числа в десятичном виде
# print(bin(a)[2:]) # вывод без префикса 0b

# Преобразование в oct\hex\HEX методом строкового форматирования
print('%o, %x, %X' % (255, 255, 255))

# Преобразование в oct\hex\bin оператором форматирования строк
print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))


# Операторы выражений с числами: (+-/ и прочие)

print('\n')

a = 0b00001111 << 1 # Побитовый сдвиг  ВЛЕВО: a=00011110
a = 0b00001111 >> 1 # Побитовый сдвиг ВПРАВО: a=00000111

a = 0b00001111 & 0b10001111 # Логическое И (AND)
print(bin(a)) # остаются только совпадающие биты: a=00001111

a = 0b00001111 | 0b10001111 # Логическое ИЛИ (OR)
print(bin(a)) # любые включённые биты остаются: a=10001111

a = 0b00001111 ^ 0b10001111 # логическое Искючающее ИЛИ (XOR)
print(bin(a)) # Совпадающие биты выключаются: a = 10000000

x = 1
y = 1
z = 1

x if y else z # Трехместный оператор выбора 
# значение x вычисляется, только если значение y истинно

x or y # Логическая операция ИЛИ 
# значение y вычисляется, только если значение x ложно

x and y # Логический оператор И 
# значение y вычисляется, только если значение x истинно

not x # Логическое отрицание

x is y  # Проверка идентичности объектов
x is not y

print(10 / 3) # обычное деление
print(10 // 3) # деление с округлением вниз

# Остаток от деления чисел
print(10 % 2) # 10 / 2 делится без остатка
print(10 % 3) # 10 / 3 делится на 3 с остатком 0.33


print(2 ** 5) # Возведение в степень

x != y # Проверка на неравенство


print(int(3.1415)) # Усекает дробную часть вещественного числа
print(float(3))    # Преобразует целое число в вещественное
                   # Например 1 в 1.0


# полиморфизм — означает, что выполняемая операция зависит 
# от типов объектов-операндов, над которыми она выполняется.

print(2 **200) # Возведение в степень


# Вычисление длины числа в битах:
print(0b11111111.bit_length())
# Вычисление ф-цией len,менее эффективно: -2 отсекает 0b
print(len(bin(0b11111111))-2)

print(sum((20,15,5,50)))  # суммирование группы чисел
print(min(1, 2, 3,4)) # выбор наименьшего числа из группы
print(max(1, 2, 3,4)) # выбор наибольшего числа из группы

print(math.floor(-2.99)) # Округление числа вниз 
print(int(-2.99)) # Округление числа 
print(math.trunc(2.99))  # Усечение дробной части
print(round(2.567), round(2.467), round(2.567, 2)) # округление

# Случайные числа

print(random.random()) # случайное число 0.nnnnnnnnnnn
print(random.random()+random.randint(1, 10)) # n.nnnnnnnnnnn
print(random.randint(1, 10)) # одно из 0..10
print(random.choice(['яблоко', 'груша', 'апельсин'])) # случайно

# Такой рассчёт в 0 не получится из-за недостаточного числа 
# битов в представлении вещественных чисел:
print(0.1 + 0.1 + 0.1 - 0.3)

# Необходимо делать так:

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

# Задание точности отображения чисел после точки
import decimal
decimal.getcontext( ).prec = 3  # только три цифры после точки 
print(decimal.Decimal(1) / decimal.Decimal(7))


# Рациональные (делимые) числа. 1/2 - одна вторая, итд. 
# 4/6 будут упрощены до 2, 3 с помощью функции gcd


from fractions import Fraction
x = Fraction(1, 2)  # Числитель, знаменатель
y = Fraction('0.5') # Представление 1/2 в виде веществ-го числа
z = x + y
print(x, '+', y, '=', z)  # 1/2 + 0.5 = 1

# 1/3 + 6/12
print(decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12)))



# Множества ПРОПУСКАЮ - ниасилил!
'''
И не зря я решил забить на них, ибо: Поскольку для дальнейшего обсуждения генераторов необходимо знание некоторых базовых концепций, которые мы еще не рассматривали, мы отложим его до последующих глав книги.
'''

# Использование множества для удаления повторяющихся значений:
L = [5, 1, 2, 1, 3, 2, 4, 5]
print (L) # значения дублированы
print(set(L)) # коллекцию в множество {} 
print(list(set(L))) # и обратно []

# Чтобы изменить неизменяемый объект строку, сначала следует
# преобразовать его в изменяемый объект список, затем изменить,
# и преобразовать обратно в строку.

s = 'Mummy'; print(s)
s = list(s); print(s) # преобразование строки в список
s[0] = 'D' # Изменение первого символа списка
s = ''.join(s); print(s) # преобразование списка обратно в строку
# Метод join объединяет строки из списка, вставляя строку
# разделитель '' между элементами списка.



# Применение множеств для обработки базы данных:

engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}
print('bob' in engineers) # bob – инженер?
print(engineers & managers) # Кто одновременно является
                            # инженером и менеджером?
print(engineers | managers) # Все сотрудники из обеих категорий
print(engineers - managers) # Инженеры, не являющиеся менеджерами
print(managers - engineers) # Менеджеры, не являющиеся инженерами
print(engineers > managers) # Все менеджеры являются инженерами?
                            # (надмножество)
print({'bob', 'sue'} < engineers) # Оба сотрудника - инженеры?
                            # (подмножество)
print((managers | engineers) > managers) # Множество всех
                            # сотрудников является надмножеством
                            # менеджеров?
print(managers ^ engineers) # Сотрудники, принадлежащие к 
                            # какой-то одной категории
print((managers | engineers) - (managers ^ engineers)) # Пересечение!


# Глубокий метафизический смысл True + 4
print(True+4) # Равно 5. Ибо True = 1, False = 0



# переменные

a = 3
b = a
a = 'spam'   # изменение 'a' не затрагивает 'b' 
print(a, b)

L1 = [2, 3, 4]
L2 = L1       # L1 и L2 ссылки на один и тот же объект.
L1[0] = 24    # изменение элемента '2' на '24' в объекте 'L1'
print(L1, L2) # касается и 'L1' и 'L2'!

''' мы не изменяем сам объект L1, изменяется компонент объекта, на который ссылается L1 '''

# полная поверхностная копия объекта, то есть объект с тем же
# значением, но расположенный в  другой области памяти.
L2 = L1[:] 

# копировать объекты любых типов, включая вложенные структуры
import copy
L3 = copy.copy(L2) # Создание “поверхностной” копии L2
L3 = copy.deepcopy(L2) # Создание полной копии: 
                       # копируются все вложенные части



# Можно сравнивать по содержимому, или по ссылкам, ведут ли они
# в одно или разные места, пусть даже с одинаковым содержимым.

# Первый способ, основанный на использовании оператора ==,
# проверяет, равны ли значения объектов:

L = [1, 2, 3]
M = L          # M и L – ссылки на один и тот же объект
print(L == M)  # Одно и то же значение
print(L is M)  # Один и тот же объект

# Второй способ, основанный на использовании оператора is,
# проверяет, ссылаются ли имена на один и тот же объект:

L = [1, 2, 3]
M = [1, 2, 3]  # Теперь M и L ссылаются на разные объекты
print(L == M)  # значение по-прежнему одинаковое
print(L is M)  # а объекты теперь разные, поэтому False


''' из-за того, что малые целые числа и строки кэшируются и используются повторно, оператор is сообщает, что переменные ссылаются на один и тот же объект. '''

X = 666
Y = 666
print(X == Y)
print(X is Y) # Один и тот же объект - кэширование в действии!

# запросить у интерпретатора количество ссылок на объект Y:
# import sys
print(sys.getrefcount(Y))



'''
S = '' # Пустая строка
S1 = "spam's" # Строка в кавычках
S2 = 's\np\ta\x00m' # Экранированные последовательности
block = """""" # Блоки в тройных кавычках
S = r'\temp\spam' # Неформатированные строки
S = b'spam' # Строки байтов в версии 3.0 (глава 36)
# S = u'spam' # Строки с символами Юникода.Только в версии 2.6  
S1 + S2 # Конкатенация
S * 3 # повторение
S[i]  # Обращение к символу по индексу
S[i:j] # извлечение подстроки (среза)
len(S) # длина
"a %s parrot" % kind # Выражение форматирования строки
"a {0} parrot".format(kind) #Строковый метод форматирования в 2и3
S.find('pa') # Вызов строкового метода: поиск
S.rstrip() # Удаление ведущих и конечных пробельных символов
S.replace('pa', 'xx') # Замена
S.split(',') # Разбиение по символу-разделитлю
S.isdigit() # Проверка содержимого
S.lower() # Преобразование регистра символов
S.endswith('spam') # Проверка окончания строки
'spam'.join(strlist) # Сборка строки из списка
S.encode('latin-1') # Кодирование строк Юникода
'''


print('22/7 - Пи = ?')
print(decimal.Decimal(str(22/7)), '-', math.pi, '=', decimal.Decimal(str(22/7)) - decimal.Decimal(str(math.pi)) )


# \b  забой последнего символа в строке
# \r Возврат каретки в начало строки без её стирания
# \v вертикальная табуляция (\t горизонтальная )


print(len(str(math.pi))) # Количество знаков в ф-ции math.pi
print('-——' * 20) # Вывести черту из 20 короткихи длинных тире

myjob = 'Python programmer\n'
for c in myjob: print(c, end=' ') # Добавить каждой букве пробел
print('Python' in myjob) # В myjob есть 'Python' ? True!

# Использование операции получения среза с тремя пределами для
# пропуска элементов и изменения порядка их следования.
x = '0123456789'
print(x[::]) # просто вывести как есть
print(x[:-1:]) # вывести без последнего символа
print(x[::-1]) # вывести задом-наперёд с конца к началу.
print(x[::2]) # извлечь каждый 2й символ от начала и до конца
print(x[1::2]) #  со 2го и до конца
print(x[1:5:3]) # извлечь каждый 3й символ со 2го до 5го.

# Фраза задом-наперёд
smile = 'улыбок тебе детских макар'
print(smile[::-1])

# import sys
print (sys.argv) # выводит с какими параметрами командной строки был запущен интерпретатор python.
print(sys.argv[1:]) # извлечёт со 2го пункта, минуя имя .py файла

a = str(42)   # Преобразование числа в символьную строку
b = int('42') # Преобразование символьной строки в число
print(a + 'число') # Теперь можно добавить к строке строку
print(b + 42)      # Теперь можно сложить два числа.

a = ord('z') # Преобразование символа в код
b = chr(122)  # Преобразование кода в символ
# конвертация символа в его код и обратно
print('Код символа', "[",b,"]", 'это число:', str((a)) )

# Открытие файла, печать содержимого на экран, и закрытие файла
with open('data.txt') as my_file:
    print(my_file.read())


# Метод find возвращает смещение, по которому найдена подстрока
# (по умолчанию поиск начинается с  начала строки), или значение
# -1, если искомая подстрока не найдена.

# Поиск и замена слова в строке.
s = 'Это вражеская подлодка'; d = 'вражеская'; f = 'советская'
where = s.find(d) # получаем смещение начала слова
s = s[:where] + f + s[(where+len(f)):] # замена нарезкой
print(s) # на фрагменты до, замещаемый, и после. 

# Обратите внимание: метод replace возвращает новую строку. 
# Так как строки являются неизменяемыми, методы никогда в 
# действительности не изменяют оригинальную строку!

a = 'old-old-old-old'; a = a.replace('old','new',2)
print(a) # Замена old на new только 2 раза. По умолчанию - все.


# Не делать import string - это УСТАРЕЛО! Стр 233.

# Выражения форматирования строк -------------

# Варианты подстановки значений на место % 
# Более 1го вставляемого значения группируются в кортеж ()
# Преобразование в число (%d - decimal) и строку (%s - string) 
# стр 236 - список прочих значений

print('That is %d %s bird!' % (1, 'dead')) 
print('%d %s %d you' % (1, 'spam', 4))
word = 'превед'; print('Из кустов сказал %s!' % word)

# %d    вывод по умолчанию
# %-6d  вывод в поле в 6 символов и выравниванием по левому краю
# %06d  вывод в поле в 6 символов с дополнением ведущими нулями

x = 666
res = 'Целые числа(integers): [%d] [%-6d] [%06d]' % (x, x, x)
print(res)

# Отображение вещественного числа в экспоненциальной форме: %e
#                               в десятичном представлении: %f
#                               в .: %g
#                      количество знаков после точки - два: %.2f
x = math.pi
print('%e - %f - %g' % (x, x, x))
print('%-6.2f - %05.2f - %+06.1f' % (x, x, x))
print('%f, %.2f, %.*f' % (x, x, 4, x))
print(math.pi)
print('%.*f' % (4, x)) # 3.1416 потому, что округление.
# http://python.su/forum/topic/31752/?page=1#post-172710


# Как и str, ф-ция repr преобразует объект в строковое 
# представление, но возвращает объект в виде строки программного
# кода, который можно выполнить, чтобы воссоздать объект.
print(str('spam'), repr('spam'))


# Форматирование строк из словаря -------------------

# (n) и (x) ссылаются на ключи в словаре в правой части выражения
print("%(n)d %(x)s" % {"n":12, "x":"негритят"})

# Шаблон с замещаемыми спецификаторами формата
reply = 'Приветствую Вас, %(name)s! \nВаш возраст - %(age)s лет.'

values = {'name': 'Max', 'age': 40} # Подготовка значений
print( reply % values)              # Подстановка значений

# print(vars()) # Вывести все ранее назначенные переменные
# вывод, используя через vars ранее назначенные переменные 
print("%(d)s или %(f)s" % vars())


# Метод форматирования строк ----------------
# имя_переменной.format() позволяет изменять кортежи{} внутри неё

# Шаблон с порядковыми номерами позиционных аргументов
template = '{0}, {1} and {2}' 
print(template.format('spam', 'ham', 'eggs')) 

template = '{motto}, {pork} and {food}' # Имена именованных арг-в
print(template.format(motto='spam', pork='ham', food='eggs'))

template = '{motto}, {0} and {food}' # Оба варианта
print(template.format('ham', motto='spam', food='eggs'))

print(
'{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2]))

print(
'My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'})
,'\n'
'My {config[spam]} runs {sys.platform}'.format(sys=sys,
config={'spam': 'laptop'})
)

print(list('0123456789')) # Разбиение строки на список (чрез зпт)

pi = math.pi
print ('{0:e}, {1:.4e}, {2:g}, {3:f}, {4:.2f}, {5:06.2f}' 
.format(pi, pi, pi, pi, pi, pi))



# Вывод чисел методом .format() отображение {номер_числа : метод}
# 
# 0:e       
# 1:.4e   Ограничить кол-во чисел после точки 
# 2:g}     
# 3:f}     использовать f для представления вещественных чисел
# 4:.2f}   Ограничить вывод двумя знаками после десятичной точки
# 5:06.2f} ограничить ширину поля вывода 6 символами и 
#          дополнить число ведущими нулями слева


# Вывод методом .format чисел в различных системах счисления:
# Шестнадцатеричное, восьмеричное и двоичное представление 255
print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))

# Другие способы работы с двоичным представлением
print(bin(255), int('11111111',2), 0b11111111)
# Другие способы работы с шестнадцатеричным представлением
print(hex(255), int('FF', 16), 0xFF)
# Другие способы работы с восьмеричным представлением
print(oct(255), int('377', 8), 0o377)

# вывод результата деления с 2 знаками после запятой
print('{0:.2f}'.format(1 / 3.0)) # параметры определены в строке

# Тоже самое методом форматирование строк из словаря: 
print('%.2f' % (1 / 3.0))

print('{0:.{1}f}'.format(1 / 3.0, 3)) # Значение извлекается из списка аргументов

# Как то же самое делается в выражениях
print('%.*f' % (4, 1 / 3.0))

print('{0:.4f}'.format(pi)) # Строковый метод
print(format(pi, '.4f'))    # Встроенная функция
print('%.4f' % pi)          # Выражение форматирования

# Вывод оператором форматирования и методом format
print('%s=%s' % ('spam', 42 ))      # выражение форматирования
print('{0}={1}'.format('spam', 42)) # метод format

# метод format предлагает дополнительные потенциальные
# преимущества. Например, оператор % не позволяет использовать
# именованные аргументы, ссылки на атрибуты и выводить числа 
# в двоичном представлении, хотя возможность использования
# словарей в операторе % помогает добиться тех же целей.

print('{0:,d}'.format(1200300)) # Разбиение числа по разрядам.

# Одинаковый вывод тремя способами, методом и функцией.
# Использование возможности автоматической нумерации {} 
# снижает преимущества метода format.
print(  
'The {0} {1} {2}'.format('Call', 'of', 'Cthulhu')
,'\n'
'The {} {} {}'.format('Call', 'of', 'Cthulhu')
,'\n'
'The %s %s %s' % ('Call', 'of', 'Cthulhu')
)

# единственными потенциальными преимуществами метода format
# остаются замена оператора % более говорящим названием метода
# и отсутствие различий между операциями с заменой единственного
# или нескольких значений.


print(math.pi,
'\n',
math.pi * 1
,'\n',
 int(math.pi * 10000) / 10000
)
# Вывод Пи с 4 знаками после точки, БЕЗ округления.


spsk=['Трус','Балбес', 'Бывалый', 'Первый', 'Второй', 'Лишний']

print(spsk)
del spsk[5] ; print(spsk) # Удалить 6й элемент списка
del spsk[3:]; print(spsk) # Удалить всё, начиная с 4го

print('Трус' in spsk) # Проверка наличия Труса в spsk
for x in spsk:
    print(x, end=' ') # обход элементов списка в цикле

spsk.sort(); print(spsk) # Сортировка с учетом регистра символов

# Добавление нескольких элементов в конец списка
spsk.extend(['Первый', 'Второй']) 

# Удаляет и возвращает последний элемент списка
print(spsk.pop()) 

# Изменяет порядок следования элементов на обратный
spsk.reverse()
print(spsk)

d = {'spam': 2, 'ham': 1, 'eggs': 3} # Словарь
print (d.get('spam')) # Возвращает значение ключа 'spam'
print (d.get('spm'))  # Возвращает None, т.к. ключ не существует
d['brunch'] = 'Bacon' # Добавление нового элемента
d['brunch'] = 'fish'  # Изменение элемента
del d['brunch']       # Удаление элемента
d.pop('ham')

# Метод словаря values возвращают список значений элементов 
# Метод items — кортежи пар: 'key' : 'value'
print(list(d.values()))
print(list(d.items()))


# удаление элементов списка по номеру позиции
L = ['aa', 'bb', 'cc', 'dd']
L.pop()  # Удаляет и выводит последний элемент списка
L.pop(0) # Удаляет и выводит элемент из заданной позиции
print(L)


# задав язык узнать его автора
table = {'Python': 'Guido van Rossum',
         'Perl': 'Larry Wall',
         'Tcl': 'John Ousterhout' }
language = 'Python'
creator = table[language]
print(creator,'\n')


sys.exit(0) # Завершение програмы с кодом 0
# http://ru.stackoverflow.com/questions/459170
#os.abort(13) # Аварийное завершение с созданием дампа.
# exit(0) # для удобства работы в интерактивном режиме,
          # использовать внутри скриптов не рекомендуется




