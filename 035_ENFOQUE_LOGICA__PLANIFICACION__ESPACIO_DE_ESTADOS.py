class Estado:
    def __init__(self, ubicacion_objeto, ubicacion_agente):
        self.ubicacion_objeto = ubicacion_objeto
        self.ubicacion_agente = ubicacion_agente

    def __eq__(self, otro_estado):
        return (isinstance(otro_estado, Estado) and
                self.ubicacion_objeto == otro_estado.ubicacion_objeto and
                self.ubicacion_agente == otro_estado.ubicacion_agente)

    def __hash__(self):
        return hash((self.ubicacion_objeto, self.ubicacion_agente))

class Accion:
    def __init__(self, precondiciones, efectos):
        self.precondiciones = precondiciones
        self.efectos = efectos

class EspacioEstados:
    def __init__(self, acciones):
        self.acciones = acciones

    def generar_sucesores(self, estado):
        sucesores = []

        for accion in self.acciones:
            if all(condicion in estado for condicion in accion.precondiciones):
                nuevo_estado = estado.copy()
                nuevo_estado.update(accion.efectos)
                sucesores.append((accion, Estado(nuevo_estado["ubicacion_objeto"], nuevo_estado["ubicacion_agente"])))

        return sucesores

# Definimos las acciones
acciones = [
    Accion({"ubicacion_objeto": "A", "ubicacion_agente": "A"}, {"ubicacion_objeto": "B"}),
    Accion({"ubicacion_objeto": "B", "ubicacion_agente": "A"}, {"ubicacion_objeto": "C"}),
    Accion({"ubicacion_objeto": "C", "ubicacion_agente": "A"}, {"ubicacion_objeto": "C", "ubicacion_agente": "C"})
]

# Creamos el espacio de estados
espacio = EspacioEstados(acciones)

# Definimos el estado inicial
estado_inicial = Estado("A", "A")

# Generamos los sucesores del estado inicial
sucesores_estado_inicial = espacio.generar_sucesores(estado_inicial)

# Imprimimos los sucesores del estado inicial
print("Sucesores del estado inicial:")
for accion, estado_sucesor in sucesores_estado_inicial:
    print(f"Acción: {accion.precondiciones} -> {accion.efectos}, Nuevo estado: {estado_sucesor.ubicacion_objeto}, {estado_sucesor.ubicacion_agente}")
