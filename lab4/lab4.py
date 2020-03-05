from tkinter import  *
from random import  randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

img = Canvas(root,bg = 'white')
img.pack(fill=BOTH,expand= 1)

color = ['red','orange','yellow','green','blue']

def new_boll():
    global x,y,r
    img.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd (30,50)
    img.create_oval(x-r,y-r,x+r,y+r,fill=choice(color),width=0)
    root.after(1000,new_boll)

new_boll()

def click(event):
    print(x,y,r)


img.bind('<Button-1>',click)

mainloop()



