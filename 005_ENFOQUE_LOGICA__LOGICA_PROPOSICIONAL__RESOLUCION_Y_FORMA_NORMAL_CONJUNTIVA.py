from sympy import symbols, Not, And, Or, Equivalent, to_cnf

# Definir las variables proposicionales
p, q, r = symbols('p q r')

# Definir algunas expresiones lógicas
expression1 = Or(And(p, q), Not(r))
expression2 = Equivalent(p, q)

# Convertir las expresiones a FNC
fnc_expression1 = to_cnf(expression1)
fnc_expression2 = to_cnf(expression2)

# Mostrar las expresiones originales y su versión en FNC
print("Expresión 1 original:", expression1)
print("Expresión 1 en FNC:", fnc_expression1)
print("\nExpresión 2 original:", expression2)
print("Expresión 2 en FNC:", fnc_expression2)
