from tkinter import *

colors = ['#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#007dff', '#0000ff', '#7d00ff']

root = Tk()
l1 = Label(text = 'Выбери цвет', font = "Times 16",width = 50)
e1 = Entry( font = "Timew 16",width = 50)

def But(color):
    mb = Button (width = 50,bg = color)
    mb.bind('<Button-1>', Ev)
    mb.pack()

def Ev():

    l1['text'] = color_name
    e1.delete(0,END)
    e1.insert(0,color_name)

l1.pack()
e1.pack()
But(colors[0])
But(colors[1])
But(colors[2])
But(colors[3])
But(colors[4])
But(colors[5])
But(colors[6])


mainloop()
