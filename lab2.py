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
x = symbols('x')
print(limit(1/x,x,1))
# 2.limit of 1/x, x to 0
print(limit(1/x,x,0))
# 3.limit of (x^2-1)/(x+1), x to -1
print(limit((x**2-1)/(x+1),x,-1))

## derivatives in lab2

x,c,p,e = symbols('x c p e')
# D
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
f = ((x**2-3000)/-4)**(1/5)
print(diff(f,x))

# E: find integrals
# 1.
x, n, e = symbols('x n e')
print(integrate(x**n,(x,1,3)))
# 2.
print(integrate(1/x,(x,1,3)))
# 3.
print((integrate(e**x,(x,1,3))))
# 4.
t = symbols('t')
R = 60*t/((t+2)*(t+1)**2)
print(integrate(R,(t,1)))
print(integrate(R,(t,3)))
# 5.
e,t = symbols('e t')
f = 0.21*e**(-0.21*t)
# first year:
print(integrate(f,(t,0,1)))
# second year:
print(integrate(f,(t,1,2)))

## F. Use solver to solve equations
# 1.
f, a, b, c =symbols('f a b c')
print(solve(Eq(a*x**2+b*x+c,0),x))
print(solveset(Eq(a*x**2+b*x+c,0),x))
# 2.

# 3.
y,t,e =symbols('y t e')
 #diff(y,t) = 100+e**-t-y

