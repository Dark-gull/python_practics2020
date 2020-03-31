from tkinter import  *
from random import  randrange as rnd, choice
import  math as mat
import time
"""Лабораторная №4 Проэкт игры "Поймай шарик" """

def init():
    global root,img
    root = Tk()
    root.geometry('800x600')
    img = Canvas(root,bg = 'white')
    img.pack(fill=BOTH,expand= 1)

color = ['red','orange','yellow','green','blue'] # цвета шариков
result = [] # здесь хранится пожсчет очков

def new_boll():
    """Вызов нового мяча
    cлучайно выбирается цвет и примерное расположение шарика"""
    global x,y,r,bool
    img.delete(ALL)

    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    bool  = img.create_oval(x-r,y-r,x+r,y+r,fill = choice(color),width = 0)
    root.after(1000,new_boll)




def click(event):
    """Подчет расстояния между точками"""
    coord_boll = img.coords(bool)
    boll_center_x = (coord_boll[2] - coord_boll[0])*0.5 + coord_boll[0]
    boll_center_y = (coord_boll[3] - coord_boll[1]) * 0.5 + coord_boll[1]
    print("Всего очков",sum(result))
    distanse = mat.sqrt((boll_center_x - event.x)**2 + ((boll_center_y - event.y)**2))
    if distanse <=  (r*25)/100 :
        print("10")
        result.append(10)
    elif distanse <= (r*50)/100:
        print("7")
        result.append(7)
    elif distanse <= (r*75)/100:
        print("5")
        result.append(5)
    elif distanse <= r:
        print("2")
        result.append(2)
    else: print("miss")

def res():
    img.create_text(750, 550, text=sum(result), fill="grey")
    root.after(100,img.delete(res))
    root.after(1,res)

img.bind('<Button-1>', click)



new_boll()
res()

mainloop()



