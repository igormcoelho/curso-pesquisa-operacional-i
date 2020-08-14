#!/usr/bin/env python3
#
# See: https://python-mip.readthedocs.io/en/latest/examples.html
#
from mip import Model, xsum, maximize, MAXIMIZE, MINIMIZE, minimize, BINARY, INTEGER, CONTINUOUS

m = Model(sense=MINIMIZE)

x1 = m.add_var(var_type=CONTINUOUS)
x2 = m.add_var(var_type=CONTINUOUS)

m.objective = minimize(1100*x1 + 700*x2)

m += ((2*x1 + 2*x2) >= 16)

m += ((3*x1 + 1*x2) >= 12)

status = m.optimize() #(max_seconds=300)

print("x1 =", x1.x, " x2 =", x2.x, " status =", status, " obj =",m.objective_value)

m.write("ex_prova.lp")
