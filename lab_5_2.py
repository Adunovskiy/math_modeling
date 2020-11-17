import sympy as sm

x, y, z, a = sm.symbols('x y z a')

ans1 = sm.simplify((x * y ** 2 - 2 * x * y * z + x * z ** 2 \
                    + y ** 2 - 2 * y * z + z ** 2) / (x ** 2 - 1))
print(ans1)

ans2 = sm.trigsimp(sm.sqrt((1 + sm.sin(a)) / (1 \
                           - sm.sin(a))) + sm.sqrt((1 - sm.sin(a)) / (1 + sm.sin(a))))
print(ans2)  