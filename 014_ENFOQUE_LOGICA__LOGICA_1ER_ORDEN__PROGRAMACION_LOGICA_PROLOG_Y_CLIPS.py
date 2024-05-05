from pyswip import Prolog

# Crear un objeto Prolog
prolog = Prolog()

# Definir hechos y reglas en Prolog
prolog.assertz("hombre(socrates)")          # Sócrates es un hombre
prolog.assertz("mortal(X) :- hombre(X)")    # Todos los hombres son mortales

# Consultar en Prolog
for result in prolog.query("mortal(socrates)"):  # Consultar si Sócrates es mortal
    print("Sócrates es mortal:", result)
