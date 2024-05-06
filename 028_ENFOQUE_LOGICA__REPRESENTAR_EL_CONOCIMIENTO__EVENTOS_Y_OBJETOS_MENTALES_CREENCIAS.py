class Creencias:
    def __init__(self):
        self.creencias = {}

    def agregar_creencia(self, objeto, evento):
        if objeto not in self.creencias:
            self.creencias[objeto] = []
        self.creencias[objeto].append(evento)

    def obtener_creencias(self, objeto):
        return self.creencias.get(objeto, [])

# Creamos una instancia de la clase Creencias
creencias_agente = Creencias()

# El agente cree que el objeto "libro" está en la habitación "sala"
creencias_agente.agregar_creencia("libro", "en la sala")

# El agente cree que el objeto "llaves" está en la habitación "cocina"
creencias_agente.agregar_creencia("llaves", "en la cocina")

# El agente cree que el objeto "libro" ha sido leído
creencias_agente.agregar_creencia("libro", "leído")

# El agente quiere verificar sus creencias
print("Creencias del agente:")
print("El agente cree que el libro está:", creencias_agente.obtener_creencias("libro"))
print("El agente cree que las llaves están:", creencias_agente.obtener_creencias("llaves"))
