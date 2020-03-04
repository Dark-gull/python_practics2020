from graph import *




def car():
    """Здесь будет отрисовавоться машина"""
    pass
def background(upcolor:list = [0,0,0],downcolor:list = [0,0,0],size_up_rectangle:list = [0,0,0,0]
               ,size_down_rectangle:list = [0,0,0,0]):
    """Фон"""
    penColor(0,0,0)
    brushColor(upcolor[0],upcolor[1],upcolor[2]) #bacground up color
    rectangle(size_up_rectangle[0],size_up_rectangle[1],size_up_rectangle[2],size_up_rectangle[3])
    brushColor(downcolor[0],downcolor[1],downcolor[2])
    rectangle(size_down_rectangle[0],size_down_rectangle[1],size_down_rectangle[2],size_down_rectangle[3])

def roud():
    """Здесь будет отрисововаться дорога"""
    pass

def cloud():
    """Здесь будет отрисововаться облачко"""
    pass


background([128,255,212],[102,51,0],[0,0,600,300],[0,300,600,600])

run()



