from sympy import symbols
from sympy import sqrt
from sympy import simplify, expand, factor, trigsimp
from sympy import sin, cos, pi, exp, acos
from sympy.vector import CoordSys3D
from sympy import evalf

N = CoordSys3D('N')

a = 4 * N.i + 3 * N.j + 8 * N.k
b = -2 * N.i + 8 * N.j + 7 * N.k
c = -5 * N.i - 6 * N.j + 12 * N.k

angle1 = a.dot(b)
angle2 = a.dot(c)
angle3 = b.dot(c)


cos1 = angle1 / (sqrt(a.dot(a)) * sqrt(b.dot(b)))
cos2 = angle2 / (sqrt(a.dot(a)) * sqrt(c.dot(c)))
cos3 = angle3 / (sqrt(b.dot(b)) * sqrt(c.dot(c)))

print(acos(cos1).evalf()*57.3)
print(acos(cos2).evalf()*57.3)
print(acos(cos3).evalf()*57.3)