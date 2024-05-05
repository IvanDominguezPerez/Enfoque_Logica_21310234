from sympy import symbols, Not, And, Or, Implies, Equivalent, satisfiable

# Definir las variables proposicionales
p, q, r = symbols('p q r')

# Definir algunas expresiones lógicas
expression1 = And(p, q)
expression2 = Or(p, Not(p))
expression3 = Implies(p, q)
expression4 = Equivalent(p, q)

# Verificar la equivalencia entre dos expresiones
equivalence = Equivalent(expression1, expression2)
print("¿{} y {} son equivalentes?".format(expression1, expression2))
print("Respuesta:", equivalence)

# Verificar la validez de una expresión
validity = expression3.is_valid()
print("\n¿{} es válida?".format(expression3))
print("Respuesta:", validity)

# Verificar la satisfacibilidad de una expresión
satisfiability = satisfiable(expression4)
print("\n¿{} es satisfacible?".format(expression4))
print("Respuesta:", satisfiability)
