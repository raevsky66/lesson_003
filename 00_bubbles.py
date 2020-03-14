# -*- coding: utf-8 -*-
import random as rd

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
center_position = sd.get_point(50, 50)
radius = 50
for _ in range(0, 3):
    sd.circle(center_position, radius)
    radius -= 5


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def circle(point, step, radius = 50, one_circle = False):
    for _ in range(0, 3):
        sd.circle(point, radius)
        if one_circle == True:
            break
        radius -= step

# center_position = sd.get_point(150, 150)
# circle(center_position, 15)

# Нарисовать 10 пузырьков в ряд
# center_position = sd.get_point(150, 150)
# radius = 20

# for x in range(150, 650,50):
#     center_position = sd.get_point(x, 350)
#     circle(center_position, 15, radius, one_circle=True)
# Нарисовать три ряда по 10 пузырьков
# radius = 20
# for y in range(150,251,50):
#     for x in range(150, 650,50):
#         center_position = sd.get_point(x, y)
#         circle(center_position, 15, radius, one_circle=True)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
radius = 20
for _ in range(0,100):
    # x = rd.randint(40,1500)
    # y = rd.randint(40,1500)
    # center_position = get_point(x, y)
    center_position = sd.random_point()
    circle(center_position, 15, radius, one_circle=True)

sd.pause()
