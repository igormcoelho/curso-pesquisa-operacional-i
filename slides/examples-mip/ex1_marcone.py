#!/usr/bin/env python3
#
# See: https://python-mip.readthedocs.io/en/latest/examples.html
#
from mip import Model, xsum, maximize, MAXIMIZE, BINARY, INTEGER

m = Model(sense=MAXIMIZE)

x1 = m.add_var(var_type=INTEGER)
x2 = m.add_var(var_type=INTEGER)

m.objective = maximize(5*x1 + 8*x2)

m += ((x1 + x2) <= 6)

m += ((5*x1 + 9*x2) <= 45)

status = m.optimize() #(max_seconds=300)

print("x1 =", x1.x, " x2 =", x2.x, " status =", status, " obj =",m.objective_value)
