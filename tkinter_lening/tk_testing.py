from tkinter import *

root = Tk()
root.geometry('50x250')
colors = [['#ff0000','красный'],['#ff7d00','оранжевый'],['#ffff00','желтый'],['#00ff00','зеленый'],
          ['#007dff','голубой'],['#0000ff','синий'],['#7d00ff','фиолетовый']]


l1 = Label(text = 'Выбери цвет', font = "Times 16",width = 50)
e1 = Entry( font = "Timew 16",width = 50)



def my_button (color_code):
    global color_code_glob
    color_code_glob = color_code
    mbut = Button(bg = color_code,width = 50)
    mbut.bind('<Button-1>', my_event)
    mbut.pack()

def my_event (event):
    l1.config(text = color_code_glob)
    e1.delete(0,END)
    e1.insert(0,color_code_glob)

l1.pack()
e1.pack()
my_button(colors[0][0])
my_button(colors[1][0])



mainloop()
