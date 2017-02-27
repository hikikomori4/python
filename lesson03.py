#!/usr/bin/python3
# coding: utf-8

# === Проверка простых условий ===
x = 2
if x == 2:
    print('Двойка')
else:
    print('Что-то другое')

print()

# === Циклы ===

# Чтобы присвоить значение пременной используется знак «=», 
# а для сравнения — «==». Для увеличения значения переменной,
# или добавления к строке используется оператор «+=», 
# а для уменьшения — «-=».

x = 0
while x < 10:
    x += 1 # инкрементальная конкатенация в цикле, длинее: x=x+1
    print(x, end=' ')  # Вывод без \n в одну строку.

print('\n')


x = 0
while True:
    x += 1
    if x > 20:
       print('— x > 20')
       break  # принудительное завершение цикла при x > 20
    print(x, end=' ')

print()

# === Обработка списка в цикле ===
# Проверка возраста people на +18

people = [
    ['Иван', 10, 120],
    ['Мария',18, 160],
    ['Григорий', 13, 110],
    ['Ирина', 26, 167],
    ['Кирилл',27, 170],
]

print('Совершеннолетние в группе:')

i = 0; count = 0

while True:
    if i == len(people):
       break   # завершить цикл при достижении последней персоны
    man = people[i]
    if man[1] >= 18:
        print(man[0], end=' ')
        count += 1
    i += 1


print()

# === for - Перечисление элементов массива === 

i = 0; count = 0

for man in people:
    if man[1] >= 18:
        count += 1
print('Кол-во совершеннолетних в группе: ', count)

print()

count = 0

for man  in people:
    if man[1] <= 13:
        print(count,man[1],'- детям низзя!')
        continue # Перейти к следующей итерации в цикле
    if man[1] > 18:
        count+= 1
    print(count, man[1])

# (лат. iteratio — повторяю) — повторение какого-либо действия. 

# https://pythonworld.ru/osnovy/cikly-for-i-while-operatory-break-i-continue-volshebnoe-slovo-else.html


lst = [ [1,2], [3,4, None], [5,6] ]
for a in lst:
    break  # досрочно прерывает цикл
    for b in a:
        print(a, b)
else:  # выполнится только в том случае, если 
       # выход из цикла произошел без помощи break.
    print('else выполнен!')


summa = 0

for man in people:
    summa += man[2]
print('средний рост на количество людей: ',summa/len(people)) 

print()


# === Экскурс в файлы ===

fl = open('data.txt', 'w') # Создается новый файл для вывода
fl.write('\nАз есмь содержимое файла\n') # Запись строки в файл
fl.close() # Закрывает файл и выталкивает выходные буферы на диск

fl = open('data.txt') # r – режим доступа к файлу по умолчанию
text = fl.read() # Файл читается целиком в строку
print(text)

flb = open('data.bin', 'wb')
flb.write(b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\xf0') # Запись строки кодов в файл
flb.close()

flb = open('data.bin', 'rb').read() # Открытие бинарного файла
print(flb)

# r'' указывает на неформатированную строку, чтобы символы в
# пути не были восприняты как управляющие коды \n и \t
myfile = open(r'C:\new\text.dat', 'w')

# Или можно дублировать слэши:
myfile = open('C:\\new\\text.dat', 'w')

# === Функции ===

print()

def some_other_func():
    print('Я бесполезная функция :(') 

def funtik():
    f = open('funtik.log', 'a')
    f.write('Первая запись\n')
    f.close()
    print('В файл funtik.log записано log1')
    some_other_func()

funtik()  # запуск этой функции


# === Аргумент функции ===

def funtik2(text):  # Ф-ции передаётся text 
    f = open('funtik.log', 'a')
    f.write(text + '\n')
    f.close()

funtik2('Не забыть указывать время записи!')


# === Более 1-го аргумента и различные способы вызова ф-ции ===

def funtik3(time, text):
    # локальная область видимости!
    # переменные внутри ф-ции не видны извне
    print(locals())
    f = open('funtik.log', 'a')
    f.write(time + ' ' + text + '\n')
    f.close()

# print(globals()) # показывает все глобальные переменные пр-мы

# не именнованные параметры указываются по-порядку:
funtik3('09:30', 'В серверной.')  

# именованные параметры могут указываться в любом порядке:
funtik3(text='Меняю маршруты.', time='10:45') 

# при указании смешанного типа параметров, сперва не именованные:
funtik3('14:00', text='Ушёл обедать')

print()

# === небольшой экскурс в ф-цию формат ===

print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))
print('Hello, {}!'.format('Vasya'))
# Преобразование в oct\hex\bin оператором форматирования строк
print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))
# Преобразование в oct\hex\HEX методом строкового форматирования
print('%o, %x, %X' % (255, 255, 255))

# имя_переменной.format() позволяет изменять кортежи{} внутри неё
# Шаблон с порядковыми номерами позиционных аргументов
template = '{0}, {1} and {2}' 
print(template.format('spam', 'ham', 'eggs')) 

template = '{motto}, {0} and {food}' # Оба варианта
print(template.format('ham', motto='spam', food='eggs'))

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

print()

# ===  Функции с параметрами по умолчанию ===

def funtik4 (a, b, c=100, d=200): # c,d имеют значения по умолч.
    print('a:{} b:{} c:{} d:{}'.format(a,b,c,d))
 
funtik4(1,2) # задаются только отсутствующие параметры.
funtik4(1, 2, 20, 30) # явно задаются все параметры.
funtik4(2, 20, 30, d=21) # именованный параметр d= только справа!


print()

# === Функция *args - любое кол-во аргументов ===
# Проверка наличия '4' в аргументах.

def func(*args):
    print(args, 'Кол-во арг-тов:',len(args), end=' ')
    if 4 in args:
        print('Цифра 4 в наличии.')
    else:
        print('Цифры 4 нет.')
    
func(1, 2, 3)
func(1, 2, 3, 4, 5)
func(1, 2, 3, 4, 5, 6, 'hello')

print()


# === Функция **kwargs - передача аргументов ===

def func_2(**kwargs):
    print(kwargs)
    
func_2(name='max', age=20)    

print()

def func_3(x, *args, **kwargs):
    print('x:',x)
    print('args:', args)
    print('kwargs:', kwargs)
    
func_3(10, 12, 13, 14, name='max', age=30)


print()

# НЕ ПОНЯЛ сакрального смысла, зачем это и почему x=None

def func_4(text):
    print(text)

x =  func_4('Проверка')
print('x:', x)

print()


# === возврат переменных из функции в основную программу ===

def get_some_dict():
    x = 10
    y = 20
    return x, y 

# ВНИНАНИЕ! Одного return сделать мало! следует присвоить переменной значение!
print(get_some_dict()) # Возврат x,y в виде кортежа   

x,y = get_some_dict() #  Возврат x,y в переменные основной прогр.

print(x,y)




# === рекировка, где 'x' становится 'y', а 'y' становится 'x' ===

x,y = y, x
print(x,y)


# Вставка exit() в код вызывает прерывание програмы в этом месте
