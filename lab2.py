import sympy
# sqrt
n = sympy.sqrt(3)
print(n)

# represent mathematical expression: (x+2y)
from sympy import *
x,y = symbols('x y')
expr = x + 2*y
print(expr)
# add a constant term in the expression
print(expr + 1)
# remove the x in the expression
print(expr - x)
