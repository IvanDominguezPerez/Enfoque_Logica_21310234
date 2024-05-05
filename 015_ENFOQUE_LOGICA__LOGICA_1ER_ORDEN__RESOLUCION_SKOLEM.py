from sympy import symbols, Or, And, Not, satisfiable, ask, to_cnf

# Definimos las variables universales y existenciales
x, y = symbols('x y')
A = symbols('A', cls=Not)
B = symbols('B')

# Expresión lógica con variables existenciales
expr = Or(And(A, x), And(B, y))

# Convertimos la expresión a forma clausal
cnf_expr = to_cnf(expr)

# Resolvemos la expresión para encontrar una sustitución
sustitucion = satisfiable(cnf_expr)

# Verificamos si la sustitución es válida
if ask(cnf_expr.subs(sustitucion)):
    print("Sustitución válida:", sustitucion)
else:
    print("No se encontró una sustitución válida.")
