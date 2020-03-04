from graph import *

def imager(Car_color:str = "black",Car_size:int = 100,Car_locate:list=[0,0],cloud_locate:list = [0,0],
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



def car(color:list,size:int,locate:list):
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

def roud(width,color,line_color):
    """Здесь будет отрисововаться дорога"""
    pass

def cloud(locate,intensive):
    """Здесь будет отрисововаться облачко"""
    pass


background([128,255,212],[102,51,0],[0,0,600,300],[0,300,600,600])

run()



