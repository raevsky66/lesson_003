# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random as rd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
sd.resolution = (1920, 1080)

def smile(x,y, color):
    sd.circle(sd.get_point(x,y),color=color)
    sd.circle(sd.get_point(x+10,y+15),radius=2)
    sd.circle(sd.get_point(x - 10, y + 15), radius=2)
    sd.line(sd.get_point(x+8,y-15),sd.get_point(x-8,y-15), (20,200,55))

for _ in range(0,10):
    x= rd.randint(0, sd.resolution[0]-100)
    y = rd.randint(0, sd.resolution[1]-100)
    smile(x,y,sd.COLOR_DARK_YELLOW)

sd.pause()
