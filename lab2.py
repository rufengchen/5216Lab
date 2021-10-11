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
from sympy import *
x,c,p = symbols('x c p')
## Limit questions in lab2
# 1.limit of 1/x, x to 1
print(limit(1/x,x,1))
# 2.limit of 1/x, x to 0
print(limit(1/x,x,0))
# 3.limit of (x^2-1)/(x+1), x to -1
print(limit((x**2-1)/(x+1),x,-1))

## derivatives in lab2
import math
x,c,p,e = symbols('x c p e')
# 1.
print(diff(c*p*(1-p),p))

# 2.
print(diff(sqrt(x),x))

# 3.
expr1 = c*(e**(-p))
print(diff(p*expr1,p))

# 4. partial derivatives
x1,x2 = symbols('x1 x2')
expr2 = (x1+x2)**2
d1 = diff(expr2,x1)
print(d1)
d2 = diff(expr2,x2)
print(d2)
print(diff(d1,x1)) # second derivative to x1
print(diff(d2,x2)) # second derivative to x2
print(diff(d1,x2)) # second derivative to x2
## second method take derivatives with repect
##   to many variables at once
print(diff(expr2,x1,x1))
print(diff(expr2,x2,x2))
print(diff(expr2,x1,x2))

# 5.
x,f = symbols('x f')
x = (sqrt(3000-4*f**5))



