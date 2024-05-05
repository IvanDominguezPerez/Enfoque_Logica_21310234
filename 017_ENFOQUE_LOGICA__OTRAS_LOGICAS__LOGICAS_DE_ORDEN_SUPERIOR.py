from sympy import symbols, Function, exists, And, Or, satisfiable

# Definir variables y predicados
x, y = symbols('x y')
P = Function('P')
Q = Function('Q')

# Definir la expresión lógica
expr = Or(exists(x, P(x)), exists(y, Q(y)))

# Verificar si la expresión es satisfacible
satisfacible = satisfiable(expr)

# Imprimir el resultado
if satisfacible:
    print("La expresión es satisfacible.")
    print("Valores de satisfacción:", satisfacible)
else:
    print("La expresión no es satisfacible.")
