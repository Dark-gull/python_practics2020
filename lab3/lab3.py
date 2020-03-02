from graph import *
import random as rd
brushColor(128,255,255)
# Фон
rectangle(0,0,600,300)
brushColor(0,128,0)
rectangle(0,300,600,600)

def house():
    # Домик
    brushColor(102, 51, 0)
    penColor(0, 0, 0)
    rectangle(50, 250, 250, 450)
    brushColor(255, 0, 0)
    polygon([(50, 250), (150, 200), (250, 250)])
    rectangle(100, 300, 200, 400)
    brushColor(130, 255, 255)
    rectangle(105, 305, 195, 395)
    brushColor(0, 0, 0)
    rectangle(147, 305, 150, 395)
    rectangle(105, 347, 195, 350)

def cloud():
    # Облачко
    brushColor(255, 255, 255)
    for i in range(9):
        x = rd.randint(350, 500)
        y = rd.randint(100, 150)
        circle(x, y, 30)



# Солнце
brushColor(255,255,0)
circle(100,100,50)

def three:
    # Дерево
    brushColor(110, 50, 0)
    rectangle(400, 350, 420, 450)
    brushColor(0, 150, 0)
    for i in range(10):
        x = rd.randint(380, 440)
        y = rd.randint(240, 350)
        circle(x, y, 30)







run()