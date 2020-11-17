import sympy


a, x, y, o, p = sympy.symbols('a x y o p')
ch = (sympy.exp(p) + sympy.exp(-1 * p)) / 2
sh = (sympy.exp(p) - sympy.exp(-1 * p)) / 2



p1 = int(input('Введите значение p: '))
a1 = int(input('Введите значение a: '))
o1 = int(input('Введите значение o: '))

x = (a1 * sh.subs(p, p1)) / (ch.subs(p, p1) - sympy.cos(o1))
y = (a1 * sympy.sin(p1)) / (ch.subs(p, p1) - sympy.cos(o1))



print(x.evalf())
print(y.evalf())