from pyDatalog import pyDatalog

# Declarar las variables y funciones de la lógica
pyDatalog.create_terms('P, Q, x, y, z')

# Declarar algunas relaciones entre variables
# Por ejemplo, afirmamos que P(x) es verdadero para algunos valores de x
+P('a')
+P('b')
+P('c')

# Declarar una regla utilizando cuantificadores
# Por ejemplo, afirmamos que Q(y) es verdadero si para todo z, P(z) es verdadero
Q(y) <= (P(z)) 

# Consultar la base de conocimiento para encontrar valores que satisfacen la regla
result = Q(y).data

# Imprimir el resultado
print("Valores de y que satisfacen la regla Q(y):", result)
