class SistemaInferencia:
    def __init__(self):
        self.probabilidades = {}

    def agregar_probabilidad(self, evento, probabilidad):
        self.probabilidades[evento] = probabilidad

    def calcular_probabilidad_conjunta(self, eventos):
        probabilidad_conjunta = 1.0
        for evento in eventos:
            probabilidad_conjunta *= self.probabilidades.get(evento, 0)
        return probabilidad_conjunta

# Creamos una instancia del sistema de inferencia
sistema_inferencia = SistemaInferencia()

# Agregamos algunas probabilidades
sistema_inferencia.agregar_probabilidad("llueve", 0.3)
sistema_inferencia.agregar_probabilidad("nublado", 0.5)
sistema_inferencia.agregar_probabilidad("fresco", 0.4)

# Calculamos la probabilidad conjunta de varios eventos
probabilidad_llueve_y_nublado_y_fresco = sistema_inferencia.calcular_probabilidad_conjunta(["llueve", "nublado", "fresco"])
print("Probabilidad de que llueva, esté nublado y fresco:", probabilidad_llueve_y_nublado_y_fresco)
