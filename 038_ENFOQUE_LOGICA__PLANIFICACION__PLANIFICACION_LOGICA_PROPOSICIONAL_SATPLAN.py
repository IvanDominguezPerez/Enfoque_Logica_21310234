from pysat.solvers import Glucose3
from itertools import combinations

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

def satplan(acciones, estado_inicial, estado_objetivo):
    # Crear el solucionador SAT
    solver = Glucose3()

    # Crear variables proposicionales para cada acción en cada nivel temporal
    variables = {}
    for nivel in range(len(estado_objetivo)):
        variables[nivel] = {}
        for accion in acciones:
            variables[nivel][accion.nombre] = len(variables) + 1
            solver.add_clause([-variables[nivel][accion.nombre]])

    # Agregar cláusulas para el estado inicial
    for prop in estado_inicial:
        solver.add_clause([variables[0][accion.nombre] for accion in acciones if accion.efectos == prop])

    # Agregar cláusulas para el estado objetivo
    for nivel, estado in enumerate(estado_objetivo):
        for prop in estado:
            solver.add_clause([variables[nivel][accion.nombre] for accion in acciones if accion.efectos == prop])

    # Agregar cláusulas para la validez de las acciones
    for nivel in range(len(estado_objetivo) - 1):
        for accion1, accion2 in combinations(acciones, 2):
            if set(accion1.efectos).intersection(set(accion2.precondiciones)):
                solver.add_clause([-variables[nivel][accion1.nombre], -variables[nivel][accion2.nombre]])

    # Resolver el problema SAT
    if solver.solve():
        plan = []
        for nivel in range(len(estado_objetivo)):
            for accion in acciones:
                if solver.get_values([variables[nivel][accion.nombre]])[0]:
                    plan.append(accion.nombre)
                    break
        return plan
    else:
        return None

# Definir acciones, estado inicial y estado objetivo
acciones = [
    Accion("A", [], ["P"]),
    Accion("B", ["P"], ["Q"]),
    Accion("C", ["Q"], ["R"]),
    Accion("D", ["R"], ["S"]),
    Accion("E", ["S"], ["T"])
]
estado_inicial = {"P"}
estado_objetivo = [{"T"}]

# Ejecutar SATPLAN
plan = satplan(acciones, estado_inicial, estado_objetivo)

# Imprimir el plan
if plan:
    print("Plan encontrado:")
    print(plan)
else:
    print("No se encontró un plan")
