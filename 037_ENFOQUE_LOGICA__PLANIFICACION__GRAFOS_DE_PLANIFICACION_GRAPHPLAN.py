class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

class NodoGrafo:
    def __init__(self, nivel, estado, acciones_previas=None):
        self.nivel = nivel
        self.estado = estado
        self.acciones_previas = acciones_previas if acciones_previas is not None else set()

def graphplan(acciones, estado_inicial, estado_objetivo):
    # Inicializamos el grafo con el nodo inicial
    grafo = {0: [NodoGrafo(0, estado_inicial)]}
    nivel_maximo = 0

    # Mientras no hayamos encontrado una solución o alcanzado un nivel máximo
    while True:
        nivel_maximo += 1
        grafo[nivel_maximo] = []

        # Expandimos el grafo hacia adelante y hacia atrás en cada nivel
        expandir_grafo_hacia_adelante(acciones, grafo, nivel_maximo)
        expandir_grafo_hacia_atras(grafo, nivel_maximo)

        # Verificamos si se ha alcanzado el estado objetivo en algún nivel
        for nodo in grafo[nivel_maximo]:
            if nodo.estado == estado_objetivo:
                return construir_plan(grafo, nodo)

        # Si hemos alcanzado el nivel máximo sin encontrar una solución, retornamos None
        if nivel_maximo >= len(grafo) - 1:
            return None

def expandir_grafo_hacia_adelante(acciones, grafo, nivel):
    for nodo in grafo[nivel - 1]:
        for accion in acciones:
            if all(precondicion in nodo.estado for precondicion in accion.precondiciones):
                nuevo_estado = nodo.estado.copy()
                nuevo_estado.update(accion.efectos)
                nuevo_nodo = NodoGrafo(nivel, nuevo_estado, {accion.nombre})
                if nuevo_nodo not in grafo[nivel]:
                    grafo[nivel].append(nuevo_nodo)

def expandir_grafo_hacia_atras(grafo, nivel):
    acciones_previas = set()
    for nodo in grafo[nivel]:
        acciones_previas.update(nodo.acciones_previas)
    for nodo in grafo[nivel - 1]:
        nodo.acciones_previas = acciones_previas

def construir_plan(grafo, nodo_objetivo):
    plan = []
    nodo_actual = nodo_objetivo
    while nodo_actual.nivel > 0:
        for nodo in grafo[nodo_actual.nivel - 1]:
            if nodo_actual.acciones_previas.intersection({accion.nombre for accion in nodo.acciones_previas}):
                plan.append(nodo_actual.acciones_previas.pop())
                nodo_actual = nodo
                break
    return plan[::-1]

# Definimos las acciones
acciones = [
    Accion("A", [], ["P"]),
    Accion("B", ["P"], ["Q"]),
    Accion("C", ["Q"], ["R"]),
    Accion("D", ["R"], ["S"]),
    Accion("E", ["S"], ["T"])
]

# Definimos el estado inicial y objetivo
estado_inicial = {"P"}
estado_objetivo = {"T"}

# Ejecutamos el algoritmo GRAPHPLAN
plan = graphplan(acciones, estado_inicial, estado_objetivo)

# Imprimimos el plan
if plan:
    print("Plan encontrado:")
    for accion in plan:
        print(accion)
else:
    print("No se encontró un plan")
