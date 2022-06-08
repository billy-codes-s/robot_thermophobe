import sympy as sy
from sympy import symbols

height = 50
width = 50

from PIL import Image
from sympy import *


def main():
    x,y = symbols("x y")
    fun = (15*sin(0.2*x)*cos(0.2*y))**2 + (8*sin(0.05*(x+y)))**2
    function_generation(fun)

global max, min
max, min = -10000, 10000
    
def function_generation(fun):
    global max, min
    img = Image.new("RGB", (height, width))
    x,y = symbols("x y")
    array_output = []
    number = 0
    for x1 in range(width):
        for y1 in range(height):
            sub_1 = fun.subs(x, x1)
            sub_1 = sub_1.subs(y, y1)
            img.putpixel((x1,y1), (int(sub_1), 0, 255-int(sub_1)))
            number +=1
            print(number)
    img.save("hot.png")
