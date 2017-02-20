#!/usr/bin/python3
# coding: utf-8

a = [0, 10] ; b = [0, 40] ; c = [40, 40]
ab = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
ac = (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2
bc = (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2

if (ab + ac) == bc or (ab + bc) == ac or (ac + bc) == ab:
    print("Треугольник прямоугольный")
else: print("Треугольник не опознан")




