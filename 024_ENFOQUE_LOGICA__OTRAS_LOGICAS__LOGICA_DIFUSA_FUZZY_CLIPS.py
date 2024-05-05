from pyclips import Environment, Symbol

# Crear un nuevo entorno CLIPS
env = Environment()

# Cargar la extensión de lógica difusa
env.load('fuzzy.clp')

# Definir las variables difusas
env.assert_string("(deffuzzy calidad (bajo 0 0 5) (medio 0 5 10) (alto 5 10 10))")
env.assert_string("(deffuzzy servicio (bajo 0 0 5) (medio 0 5 10) (alto 5 10 10))")
env.assert_string("(deffuzzy propina (bajo 0 0 13) (medio 0 13 25) (alto 13 25 25))")

# Definir las reglas difusas
env.assert_string("(defrule regla1 (calidad bajo) (servicio bajo) => (assert (propina bajo)))")
env.assert_string("(defrule regla2 (calidad medio) (servicio medio) => (assert (propina medio)))")
env.assert_string("(defrule regla3 (calidad alto) (servicio alto) => (assert (propina alto)))")

# Insertar hechos
env.assert_string("(assert (calidad bajo))")
env.assert_string("(assert (servicio medio))")

# Ejecutar el motor de inferencia difusa
env.run()

# Obtener el valor de la propina
propina = env.find_template("propina").fact_list[0].slots["value"]

print("Valor de la propina difusa:", propina)
