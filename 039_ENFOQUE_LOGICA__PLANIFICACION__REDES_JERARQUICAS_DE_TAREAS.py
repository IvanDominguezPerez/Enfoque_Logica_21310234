class Tarea:
    def __init__(self, nombre, subtasks=None):
        self.nombre = nombre
        self.subtasks = subtasks if subtasks else []

def planificar(red_tareas, objetivo):
    plan = []

    # Función recursiva para buscar la tarea objetivo
    def buscar_tarea(tarea_actual):
        # Si la tarea actual es el objetivo, agregamos la tarea al plan
        if tarea_actual.nombre == objetivo:
            plan.append(tarea_actual.nombre)
            return True
        # Buscamos en las subtareas recursivamente
        for subtask in tarea_actual.subtasks:
            if buscar_tarea(subtask):
                plan.append(tarea_actual.nombre)
                return True
        return False

    # Buscamos el objetivo desde la raíz de la red de tareas
    buscar_tarea(red_tareas)

    # Invertimos el plan para que esté en el orden correcto
    plan.reverse()
    return plan

# Definimos la red de tareas
tarea1 = Tarea("Tarea1")
tarea2 = Tarea("Tarea2")
tarea3 = Tarea("Tarea3")
tarea4 = Tarea("Tarea4")
tarea5 = Tarea("Tarea5", [tarea1, tarea2])
tarea6 = Tarea("Tarea6", [tarea3, tarea4])
tarea7 = Tarea("Tarea7", [tarea5, tarea6])

# Definimos el objetivo
objetivo = "Tarea4"

# Planificamos la tarea para alcanzar el objetivo
plan = planificar(tarea7, objetivo)

# Mostramos el plan resultante
if plan:
    print("Plan encontrado para alcanzar el objetivo '{}':".format(objetivo))
    print(plan)
else:
    print("No se pudo encontrar un plan para alcanzar el objetivo '{}'".format(objetivo))
