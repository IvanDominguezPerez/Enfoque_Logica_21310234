class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

class Estado:
    def __init__(self, nombre, acciones):
        self.nombre = nombre
        self.acciones = acciones

def planificacion_orden_parcial(acciones, estado_inicial, estado_objetivo):
    plan = []

    while estado_inicial != estado_objetivo:
        accion_aplicable = None

        for accion in acciones:
            if all(condicion in estado_inicial.acciones for condicion in accion.precondiciones):
                accion_aplicable = accion
                break

        if accion_aplicable is None:
            return None  # No se encontró una acción aplicable

        plan.append(accion_aplicable)
        estado_inicial.acciones.append(accion_aplicable.efectos)
        estado_inicial.acciones = [accion for accion in estado_inicial.acciones if accion not in accion_aplicable.precondiciones]

    return plan

# Definimos las acciones
acciones = [
    Accion("A1", [], ["A"]),
    Accion("A2", ["A"], ["B"]),
    Accion("A3", [], ["C"]),
    Accion("A4", ["B", "C"], ["D"]),
    Accion("A5", ["D"], ["E"]),
]

# Definimos el estado inicial y objetivo
estado_inicial = Estado("Inicial", [])
estado_objetivo = Estado("Objetivo", ["E"])

# Planificamos
plan = planificacion_orden_parcial(acciones, estado_inicial, estado_objetivo)

# Imprimimos el plan
if plan:
    print("Plan encontrado:")
    for accion in plan:
        print(f"Acción: {accion.nombre}")
else:
    print("No se encontró un plan")
