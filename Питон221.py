from turtle import *

title('Группа Python221')
setup(1000, 400)
setworldcoordinates(-20, -100, 960, 300)
pensize(12)
pencolor("cyan")

python221 = [
    (0,210), (100, 210), (100, 0), # "П"
    penup, (120, 100), pendown, # Пробел
    (120, 0), (190, 100), (190, 0), # "и"
    penup, (210, 100), pendown, # Пробел
    (280, 100), penup, (245, 100), pendown, (245,0), # "т"
    penup, (300, 100), pendown, # Пробел
    (300, 0), (370, 0), (370, 100), (300, 100), # "о"
    penup, (390, 100), pendown, # Пробел
    (390, 0), penup, (460, 100), pendown, (460, 0), penup, (390, 50), pendown, (460, 50), # "н"
    penup, (500, 180), pendown, # Пробел
    (590, 180), (590, 90), (500, 90), (500, 0), (590, 0), # "2"
    penup, (620, 180), pendown, # Пробел
    (710, 180), (710, 90), (620, 90), (620, 0), (710, 0), # "2"
    penup, (740, 130), pendown, # Пробел
    (785, 180), (785, 0), # "1"
    penup, (860, 210), pendown # Пробел
]

for i in python221:
    if type(i) == tuple:
        goto(i[0], i[1])
    else:
        i()
else:
    pensize(18) # "!"
    goto(860, 40), # "!"
    penup(), # "!"
    goto(860, 0), # "!"
    pendown(), # "!"
    circle(7) # "!"
    color("cyan", "yellow") # "!"

bgcolor('yellow')

exitonclick()
