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

#
expanded_expr = expand(x*expr)
print(expanded_expr)

## Limit questions in lab2
# 1.limit of 1/x, x to 1
print(limit(1/x,x,1))
# 2.limit of 1/x, x to 0
print(limit(1/x,x,0))
# 3.limit of (x^2-1)/(x+1), x to -1
print(limit((x**2-1)/(x+1),x,-1))
