#!/usr/bin/python3
# coding: utf-8

from random import randrange

'''



[ | | | ] - Линкор, 1
[ | | ] - Крейсер, 2
[ | ] - Эсминец, 3
[ ] - Катер, 4
                    
  А Б В Г Д Е Ж З И К    А Б В Г Д Е Ж З И К
1                      1                      
2                      2                      
3                      3                      
4                      4                      
5                      5                      
6                      6                      
7                      7                      
8                      8                      
9                      9                      
0                      0                    
                    

'''


class Sea(object):
    def __init__():
        area = []
        return area
        

class Ships(object):
    def __init__(self, stype, cells, x_coord, \
                 y_coord, orient, status):
        self.stype = stype
        self.cells = cells
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.orient = orient
        self.status = status
    


battleship = Ships('Линкор',4, randrange(10), randrange(10), randrange(2),1)
cruiser = Ships('Крейсер',3, randrange(10), randrange(10), randrange(2),1)
destroyer = Ships('Эсминец',2, randrange(10), randrange(10), randrange(2),1) 
boat = Ships('Катер',1, randrange(10), randrange(10), randrange(2),1)

print(battleship.stype, battleship.cells, battleship.x_coord, \
      battleship.y_coord, battleship.orient, battleship.status)
      
# Все свойства
# print(battleship.__dict__)


sea = []
      
      
# Размещение кораблей

pass





# обмен ударами

pass

# проверка

pass


