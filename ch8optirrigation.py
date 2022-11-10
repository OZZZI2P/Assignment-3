"""
Description: - This script will find the least cost feed ration as determined by linear programming.

Requirements:
- Python 3
- PuLP library

@author: Nick Kuznetsov
"""

from pulp import *

prob = LpProblem("ch8irrigation", LpMinimize)
x1 = LpVariable("i(t42)", 0)
x2 = LpVariable("i(t43)", 0)
x3 = LpVariable("i(t44)", 0)
x4 = LpVariable("n(t42)", 0)
x5 = LpVariable("n(t43)", 0)
x6 = LpVariable("n(t44)", 0)
x7 = LpVariable("r(t42)", 0)
x8 = LpVariable("r(t43)", 0)
x9 = LpVariable("r(t44)", 0)
x10 = LpVariable("s(t42)", 0)
x11 = LpVariable("s(t43)", 0)
x12 = LpVariable("s(t44)", 0)
x13 = LpVariable("s(t45)", 0)

prob += 1 * x1 + 1 * x2 + 1 * x3, "Irrigation"

prob += 1 * x4 == 1.1, "N(t42)"
prob += 1 * x7 == .2, "R(t42)"
prob += 1 * x10 == .4, "S(t42)"
prob += 1 * x4 - 1 * x7 - 1 * x10 - 1 * x1 <= 0, "I(t42)"
prob += 1 * x1 >= 0, "I(ZeroMint42)"

prob += 1 * x5 == 1.2, "N(t43)"
prob += 1 * x8 == 0, "R(t43)"
prob += (1 - .4) * x10 + .5 * x8 - 1 * x11 == 0, "S(t43)"
prob += 1 * x5 - 1 * x8 - 1 * x11 - 1 * x2 <= 0, "I(t43)"
prob += 1 * x2 >= 0, "I(ZeroMint43)"

prob += 1 * x6 == 1.2, "N(t44)"
prob += 1 * x9 == .5, "R(t44)"
prob += (1 - .4) * x11 + .5 * x9 - 1 * x12 == 0, "S(t44)"
prob += 1 * x6 - 1 * x9 - 1 * x12 - 1 * x3 <= 0, "I(t44)"
prob += 1 * x3 >= 0, "I(ZeroMint44)"

prob += 1 * x6 == 1.2, "N(t45)"
prob += 1 * x9 == .5, "R(t45)"
prob += (1 - .4) * x11 + .5 * x9 - 1 * x12 == 0, "S(t45)"
prob += 1 * x6 - 1 * x9 - 1 * x12 - 1 * x3 <= 0, "I(t45)"
prob += 1 * x3 >= 0, "I(ZeroMint45)"

prob.solve()
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Irrigation = ", value(prob.objective))