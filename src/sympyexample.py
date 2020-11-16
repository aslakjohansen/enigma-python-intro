import sympy

s = input('Please enter an expression over i and j: ')
expr = sympy.sympify(s)
symi = sympy.symbols('i')
symj = sympy.symbols('j')

print('expr='+str(expr))
print('diff(expr, i)='+str(sympy.diff(expr, symi)))

for i in range(10):
    j = i % 3
    v = expr.subs([(symi, i), (symj, j)])
    print('i=%d j=%d => result=%f' % (i, j, v))

