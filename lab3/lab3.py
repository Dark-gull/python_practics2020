from graph import *
import random as rd



brushColor(128, 255, 255)
# Фон
rectangle(0, 0, 600, 300)
brushColor(0, 128, 0)
rectangle(0, 300, 600, 600)




def house(x1: float = 0, y1: float = 0):
    # Домик
    x2 = x1
    x3 = x1
    y2 = y1
    y3 = y1

    brushColor(102, 51, 0)
    penColor(0, 0, 0)
    rectangle(50 + x1, 250 + y1, 250 + x2, 450 + y2)
    brushColor(255, 0, 0)
    polygon([(50 + x1, 250 + y1), (150 + x2, 200 + y2), (250 + x3, 250 + y3)])
    rectangle(100 + x1, 300 + y1, 200 + x2, 400 + y2)
    brushColor(130, 255, 255)
    rectangle(105 + x1, 305 + y1, 195 + x2, 395 + y2)
    brushColor(0, 0, 0)
    rectangle(147 + x1, 305 + y1, 150 + x2, 395 + y2)
    rectangle(105 + x1, 347 + y1, 195 + x2, 350 + y2)


def cloud(x1:float = 0, y1: float = 0):
    # Облачко
    penColor(0, 0, 0)
    brushColor(255, 255, 255)
    for i in range(9):
        x = rd.randint(350+x1, 500+y1)
        y = rd.randint(100+x1, 150+y1)
        circle(x+x1, y+y1, 30)


# Солнце
penColor(0, 0, 0)
brushColor(255, 255, 0)
circle(100, 100, 50)


def three(x1: float = 0, y1: float = 0):
    # Дерево
    penColor(0, 0, 0)
    brushColor(110, 50, 0)
    rectangle(400+x1, 350+y1, 420+x1, 450+y1)
    brushColor(0, 150, 0)
    for i in range(10):
        x = rd.randint(380+x1, 440+y1)
        y = rd.randint(240+x1, 350+y1)
        circle(x+x1, y+y1, 30)

house(-50)
house(100,100)

cloud()
cloud(-70,0)
three()
three(0,50)
run()
