import numpy as np

class Agente:
    def __init__(self, nombre, posicion_inicial):
        self.nombre = nombre
        self.posicion_actual = posicion_inicial

    def planificar_accion(self, entorno):
        # En este ejemplo simple, el agente elige una acción aleatoria
        return np.random.choice(["Moverse", "Esperar"])

class Entorno:
    def __init__(self, dimensiones):
        self.dimensiones = dimensiones

    def ejecutar_accion(self, accion, agente):
        if accion == "Moverse":
            # Simulamos el movimiento del agente
            nueva_posicion = tuple(np.random.randint(0, dim) for dim in self.dimensiones)
            agente.posicion_actual = nueva_posicion
            print(f"{agente.nombre} se ha movido a la posición {nueva_posicion}")
        elif accion == "Esperar":
            print(f"{agente.nombre} está esperando")

def planificacion_continua_multiagente(agentes, entorno, duracion_simulacion):
    tiempo = 0
    while tiempo < duracion_simulacion:
        for agente in agentes:
            accion = agente.planificar_accion(entorno)
            entorno.ejecutar_accion(accion, agente)
        tiempo += 1

# Creamos el entorno y los agentes
dimensiones_entorno = (10, 10)
entorno = Entorno(dimensiones_entorno)
agente1 = Agente("Agente 1", (0, 0))
agente2 = Agente("Agente 2", (9, 9))

# Ejecutamos la planificación continua y multiagente
planificacion_continua_multiagente([agente1, agente2], entorno, duracion_simulacion=5)
