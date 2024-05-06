class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

def planificacion_condicional(acciones, estado_inicial, objetivo):
    plan = []
    estado_actual = estado_inicial.copy()

    # Función para verificar si las precondiciones de una acción están satisfechas
    def precondiciones_satisfechas(accion):
        return all(precondicion in estado_actual for precondicion in accion.precondiciones)

    # Función para aplicar los efectos de una acción al estado actual
    def aplicar_efectos(accion):
        estado_actual.update(accion.efectos)

    # Bucle principal para buscar una secuencia de acciones que logren el objetivo
    while estado_actual != objetivo:
        accion_encontrada = False
        for accion in acciones:
            if precondiciones_satisfechas(accion):
                aplicar_efectos(accion)
                plan.append(accion.nombre)
                accion_encontrada = True
                break
        if not accion_encontrada:
            return None  # No se puede encontrar un plan
    return plan

# Definimos las acciones, estado inicial y objetivo
acciones = [
    Accion("A", [], ["P"]),
    Accion("B", ["P"], ["Q"]),
    Accion("C", ["Q"], ["R"]),
    Accion("D", ["R"], ["S"]),
    Accion("E", ["S"], ["T"])
]
estado_inicial = {"P"}
objetivo = {"T"}

# Ejecutamos la planificación condicional
plan = planificacion_condicional(acciones, estado_inicial, objetivo)

# Imprimimos el plan resultante
if plan:
    print("Plan encontrado:")
    print(plan)
else:
    print("No se pudo encontrar un plan")
