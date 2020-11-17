
from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import simplify, expand, factor, trigsimp
from sympy import Eq, solve, solveset, linsolve, nonlinsolve
x = symbols('x')
expr = [x ** 2 + x + 1 / x + 1 / x ** 2 - 4]
solve = nonlinsolve(expr, (x))
print(solve)

e1 = 0.8
M1 = 9
e, E, M = symbols('e E M')
expr = [E - 0.8 * sympy.sin(E) - 9]
solve = nonlinsolve(expr, (E))
print(solve)