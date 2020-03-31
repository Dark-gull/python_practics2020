from graph import *

def imager(Car_color:str = "black",Car_size:str = "middle",Car_locate:list=[0,0],cloud_locate:list = [0,0],
           cloud_intetsive:str="middle",roud_width:int=250,roud_color:str="gray", roud_line_color:str="yellow"):
    """Здесь будет выводиться картинка все кроме фона  он статичен, преббразововаться координаты в размеры и пр"""
    Car_color_code = [0,0,0]
    if Car_color == "black":
        Car_color_code = [0,0,0]
    elif Car_color == "red":
        Car_color_code = [255,0,0]
    elif Car_color == "blue":
        Car_color_code = [0,77,230]
    else: print("Такого чвета на завезли. Есть только - black,red,blue")

    car(Car_color_code,Car_size,Car_locate)

    cloud_intetsive_descriptor = 5
    if cloud_intetsive == "middle":
        cloud_intetsive_descriptor = 5
    elif cloud_intetsive == "max":
        cloud_intetsive_descriptor = 7
    elif cloud_intetsive == "min":
        cloud_intetsive_descriptor = 3
    else:
        print("Нет такого значения есть только - middle,max,min")

    cloud(cloud_locate,cloud_intetsive_descriptor)

    roud_color_code = [0,0,0]
    if roud_color == "gray":
        roud_color_code = [138,134,116]
    elif roud_color == "black":
        roud_color_code = [0,0,0]
    else:
        print ("Roud can only <gray> or <black> color ")

    roud_line_color_code = [0,0,0]
    if roud_line_color == "white":
        roud_line_color_code = [255,255,255]
    elif roud_line_color == "yellow":
        roud_line_color_code = [204,204,0]
    else:
        print("Line can only <white> or <yellow> color")

    roud(roud_width,roud_color_code,roud_line_color_code)

    pass

def car(color:list=[0,0,0],size:str ="middle",locate:list=[0,0]):
    """Здесь будет отрисовавоться машина"""
    x:float = 0
    if size == "max":
        x = 0
        y = 0
        o1 = 0
        o2 = 0

    elif size == "middle":
        x = 25
        y = 15
        o1 = 5
        o2 = 1
    elif size == "min":
        x = 50
        y = 25
        o1 = 10
        o2 = 2
# Корпус

    brushColor(color[0],color[1],color[2])

    rectangle(1,50,70,100)
    rectangle(50,1,200,100)
    rectangle(200,50,250,100)
# Колеса
    brushColor(0,0,0)
    penColor(255,255,255)
    circle(25,100,25)
    circle(225,100,25)
    brushColor(255,255,255)
    circle(25,100,15)
    circle(225,100,15)
    brushColor(0,0,0)
    circle(225,100,3)
    circle(25,100,3)
# Фары
    brushColor(255,0,0)
    rectangle(0,55,20,65)
    brushColor(204,204,0)
    rectangle(240,55,250,65)







def background(upcolor:list = [0,0,0],downcolor:list = [0,0,0],size_up_rectangle:list = [0,0,0,0]
               ,size_down_rectangle:list = [0,0,0,0]):
    """Фон"""
    penColor(0,0,0)
    brushColor(upcolor[0],upcolor[1],upcolor[2]) #bacground up color
    rectangle(size_up_rectangle[0],size_up_rectangle[1],size_up_rectangle[2],size_up_rectangle[3])
    brushColor(downcolor[0],downcolor[1],downcolor[2])
    rectangle(size_down_rectangle[0],size_down_rectangle[1],size_down_rectangle[2],size_down_rectangle[3])

def roud(width,color,line_color):
    """Здесь будет отрисововаться дорога"""
    pass

def cloud(locate,intensive):
    """Здесь будет отрисововаться облачко"""
    pass


background([128,255,212],[102,51,0],[0,0,600,300],[0,300,600,600])
imager()

run()



