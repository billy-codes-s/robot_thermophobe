import numpy as n
import sympy as sy
from sympy import symbols

x, y = symbols("x y")
fun = x + y + 1/x + 4/y
derivative_x = diff(fun, x)
derivative_xx = diff(derivative_x, x)
derivative_xy = diff(derivative_x, y)
derivative_y = diff(fun, y)
derivative_yy = diff(derivative_y, y)
derivative_yx = diff(derivative_y, x)
sol = solve((derivative_x, derivative_y), (x,y))

## create the systems of matrix for the critical points found for the function
for points in sol:
    xx_solved = float(derivative_xx.subs(x,points[0]).subs(y, points[1]))
    xy_solved = float(derivative_xy.subs(x,points[0]).subs(y, points[1]))
    yy_solved = float(derivative_yy.subs(x,points[0]).subs(y, points[1]))
    yx_solved = float(derivative_yx.subs(x,points[0]).subs(y, points[1]))
    
    matrix_a1 = n.array([[xx_solved]])
    matrix_a2 = n.array([[xx_solved,xy_solved], [yx_solved,yy_solved]])
    matrix_b1 = n.negative(matrix_a1)
    matrix_b2 = n.negative(matrix_a2)
    
    sign_a = sign_of_system([matrix_a1, matrix_a2])
    print(points)
    if sign_a == 1:
        print("defini positif")
    else:
        sign_b = sign_of_system([matrix_b1, matrix_b2])
        if sign_b == 1:
            print(f"defini_negatif")  
        elif sign_b ==-1 and sign_a == -1:
            print("point de scelle")
        else: ## this is the 0,0,...,0 case
            print("on ne peut pas conclure")
            
            
    print("-----      ------- \n\n")
    
def sign_of_system(list_of_matrix):
    print(list_of_matrix)
    sum_of_matrix = 0
    for elements in list_of_matrix:
        determinant = n.linalg.det(elements)
        print(f"determinant = {determinant}")
        if determinant < 0:
            return(-1)
        elif determinant == 0:
            return(0)
        
    else:
        return(1)
