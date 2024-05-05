from pyDatalog import pyDatalog

# Definir términos y relaciones
pyDatalog.create_terms('estudiante, asignatura, aprueba, necesita, aprobar')

# Definir algunos hechos sobre estudiantes y asignaturas
+estudiante('Juan')
+estudiante('María')
+asignatura('Inteligencia Artificial')
+asignatura('Bases de Datos')

# Definir reglas y relaciones
# Por ejemplo, definir una regla que indica que un estudiante necesita aprobar una asignatura para aprobar otra
necesita(X, Y) <= aprueba(X, Z) & aprobar(Z, Y)

# Agregar información sobre qué estudiantes aprueban qué asignaturas
+aprueba('Juan', 'Inteligencia Artificial')
+aprueba('María', 'Bases de Datos')

# Consultar la base de conocimiento para encontrar qué asignaturas necesita aprobar un estudiante
result = necesita('Juan', Y)

# Imprimir el resultado
print("Juan necesita aprobar las siguientes asignaturas:", result)
