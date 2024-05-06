class Accion:
    def __init__(self, precondiciones, efectos):
        self.precondiciones = precondiciones
        self.efectos = efectos

class ProblemaPlanificacion:
    def __init__(self, inicial, objetivo, acciones):
        self.inicial = inicial
        self.objetivo = objetivo
        self.acciones = acciones

    def planificar(self):
        plan = []
        estado_actual = self.inicial

        while estado_actual != self.objetivo:
            accion_aplicable = None

            for accion in self.acciones:
                if all(condicion in estado_actual for condicion in accion.precondiciones):
                    accion_aplicable = accion
                    break

            if accion_aplicable is None:
                return None  # No se encontró una acción aplicable

            plan.append(accion_aplicable)
            estado_actual = estado_actual.union(accion_aplicable.efectos)

        return plan

# Definimos las acciones
acciones = [
    Accion({"ubicacion_objeto": "A", "ubicacion_agente": "A"}, {"ubicacion_objeto": "B"}),
    Accion({"ubicacion_objeto": "B", "ubicacion_agente": "A"}, {"ubicacion_objeto": "C"}),
    Accion({"ubicacion_objeto": "C", "ubicacion_agente": "A"}, {"ubicacion_objeto": "C", "ubicacion_agente": "C"})
]

# Definimos el estado inicial y objetivo
estado_inicial = {"ubicacion_objeto": "A", "ubicacion_agente": "A"}
estado_objetivo = {"ubicacion_objeto": "C"}

# Creamos el problema de planificación
problema = ProblemaPlanificacion(estado_inicial, estado_objetivo, acciones)

# Planificamos
plan = problema.planificar()

# Imprimimos el plan
if plan:
    print("Plan encontrado:")
    for i, accion in enumerate(plan):
        print(f"Paso {i+1}: {accion.precondiciones} -> {accion.efectos}")
else:
    print("No se encontró un plan")
