from pyDatalog import pyDatalog

# Definir términos y relaciones
pyDatalog.create_terms('diagnostic, cause')

# Definir reglas de diagnóstico y causales
# En este ejemplo, establecemos algunas reglas ficticias para ilustrar el concepto
+diagnostic('Fiebre', 'Gripe')        # Si hay fiebre, el diagnóstico puede ser gripe
+diagnostic('Tos', 'Resfriado')        # Si hay tos, el diagnóstico puede ser resfriado
+cause('Gripe', 'Virus')               # La causa de la gripe puede ser un virus
+cause('Resfriado', 'Virus')           # La causa del resfriado puede ser un virus
+cause('Resfriado', 'Bacterias')       # La causa del resfriado también puede ser bacterias

# Consultas
# Consultamos la base de conocimientos para encontrar posibles diagnósticos y sus causas
diagnosis = diagnostic(X, Y)
causal_relation = cause(Y, Z)

# Mostrar los resultados
print("Posibles diagnósticos y sus causas:")
print(diagnosis)
print("Causalidad de los diagnósticos:")
print(causal_relation)
