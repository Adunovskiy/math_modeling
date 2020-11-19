from sympy import symbols
from sympy import sqrt
from sympy import symbols
from sympy import simplify, expand, factor, trigsimp
from sympy import sin, cos, pi, exp
from sympy.vector import CoordSys3D
from sympy import evalf

q, x, y, z, i, k, j = symbols('q x y z i k j')
N = CoordSys3D('N')
q1 = 1
q2 = -0.5

E1 = (q * x) / sqrt(((x ** 2 + y ** 2 + z) ** 2) ** 3) * N.i \
+ (q * y) / sqrt(((x ** 2 + y ** 2 + z ** 2) ** 3)) * N.j \
+ (q * z) / sqrt(((x ** 2 + y ** 2 + z ** 2) ** 3)) * N.k

E2 = (q * (x - 1)) / sqrt(((x - 1) ** 2 + (y - 1) ** 2 + (z - 1) ** 2) ** 3) * N.i \
+ (q * (y - 1)) / sqrt(((x - 1) ** 2 + (y - 1) ** 2 + (z - 1) ** 2) ** 3) * N.j \
+ (q * (z - 1)) / sqrt(((x - 1) ** 2 + (y - 1) ** 2 + (z - 1) ** 2) ** 3) * N.k

E1 = E1.subs(q, q1)
E2 = E2.subs(q, q2)
E = E1 + E2
E = E.subs(x, 3)
E = E.subs(y, 4)
E = E.subs(z, 5)
E = sqrt(E.dot(E))
print(E.evalf())
