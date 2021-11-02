# "Lab3.pdf", Question 1

from sympy import *

V0, r, min_d, d, max_d, d_i, t, n, val, double_val, r_new = symbols('V0 r min_d d max_d d_i t n val double_val r_new')
f = symbols('f', cls=Function)

V0 = 300        # Initial profit
r = 0.7         # Annual retention rate
d = 0.08        # Annual discount rate
n = 20          # Number of years of stay
min_d = 0.05    # Lowest limit of annual discount rate
max_d = 0.16    # Upper limit of annual discount rate

# Part (a): Value of customer staying for n years
val = (V0*Sum((r/(1+d))**t, (t, 0, n))).doit().evalf()

print('Part (a) Value of customer staying for ',n,' years =',"${:,.3f}".format(val),'(for current annual discount rate of',d,').')
print()


# Part (b): Sensitivity analysis on customer value subject to changes in annual discount rate
print('Part (b):')
steps = int((max_d-min_d)/0.01+1)   # Number of discount rates to be tested
for i in range(steps):
    d_i = min_d + i*0.01            # Discount rate to be tested
    val = (V0*Sum((r/(1+d_i))**t, (t, 0, n))).doit().evalf()
    print('For annual discount rate of', '{:,.2f}'.format(d_i),', the value of customer staying for ',n,' years =',"${:,.3f}".format(val),'.')

print()

# Part (c): Double the current value of a customer staying for n years
print('Part (c):')

for i in range(steps):
    d_i = min_d + i*0.01    # Discount rate to be tested
    val = (V0*Sum((r/(1+d_i))**t, (t, 0, n))).doit().evalf()    # Find value of customer for the current retention rate and discount rate
    double_val = 2*val
    f = (V0*Sum((r_new/(1+d_i))**t, (t, 0, n))).doit().evalf()  # Set up function of new customer value in terms of new retention rate (r_new)

    result=solveset(f-double_val,r_new,Interval(0,1.0))         # Solve equation of new customer value = doubled the current one

    print('For annual discount rate of', '{:,.2f}'.format(d_i),', if the customer value is doubled to', "${:,.3f}".format(double_val),', retention rate needs to be', '{:,.4f}'.format(result.args[0]),'.')
