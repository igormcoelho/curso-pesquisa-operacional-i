#!/usr/bin/env python3
#
# See: https://python-mip.readthedocs.io/en/latest/examples.html
#
from mip import Model, xsum, maximize, MAXIMIZE, BINARY, INTEGER, CONTINUOUS

m = Model(sense=MAXIMIZE)

#x1 = m.add_var(var_type=CONTINUOUS)
#x2 = m.add_var(var_type=CONTINUOUS)
#x3 = m.add_var(var_type=CONTINUOUS)
#x4 = m.add_var(var_type=CONTINUOUS)
x1 = m.add_var(var_type=INTEGER)
x2 = m.add_var(var_type=INTEGER)
x3 = m.add_var(var_type=INTEGER)
x4 = m.add_var(var_type=INTEGER)

m.objective = maximize(400*x1 + 900*x2 + 500*x3 + 200*x4)

m += ((40*x1 + 75*x2 + 30*x3 + 15*x4) <= 800)

m += ((300*x1 + 400*x2 + 200*x3 + 100*x4) >= 2000)

m += ((40*x1 + 75*x2) <= 500)

m += (x1 >= 3)
m += (x2 >= 2)

m += (x3 >= 5)
m += (x4 >= 5)

m += (x3 <= 10)
m += (x4 <= 10)

status = m.optimize() #(max_seconds=300)

print("x1 =", x1.x, " x2 =", x2.x, "x3 =", x3.x, " x4 =", x4.x, " status =", status, " obj =",m.objective_value)

m.write("ex1_prova_ex.lp")

#Best objective 1.090000000000e+04, best bound 1.090000000000e+04, gap 0.0000%
#x1 = 3.0  x2 = 3.0 x3 = 10.0  x4 = 10.0  status = OptimizationStatus.OPTIMAL  obj = 10900.0
