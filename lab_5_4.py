from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import simplify, expand, factor, trigsimp
from sympy import Eq, solve, solveset, linsolve, nonlinsolve
from sympy.solvers.inequalities import reduce_abs_inequality, reduce_rational_inequalities
from sympy import Abs

x = symbols('x')
sol = reduce_abs_inequality(Abs(x ** 2 + 2 * x - 3) \
                            + 3 * (x + 1),'<', x)

print(sol)

sol = reduce_rational_inequalities([[((x-1)*(x+2)) / ((x-3)*(x+4)) <= 0]], x)
print(sol)