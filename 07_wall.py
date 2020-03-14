# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
leng = 100
height = 50
init_point = 100, 100

for i in range(0,10): # в длину
    for h in range(0,4): # в высоту
        sd.rectangle(sd.get_point(init_point[0]+leng*i, init_point[1]+height*h), sd.get_point(init_point[0]+leng*(i+1),init_point[1]+height*(h+1)),width=1)

sd.pause()
