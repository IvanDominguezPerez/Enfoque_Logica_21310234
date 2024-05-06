class ModeloProbabilistaRacional:
    def __init__(self):
        self.preferencias = {
            "playa": 0.8,    # Probabilidad de preferir ir a la playa
            "senderismo": 0.6,    # Probabilidad de preferir hacer senderismo
            "cine": 0.7    # Probabilidad de preferir ir al cine
        }

        self.utilidades = {
            "playa": 5,    # Utilidad de ir a la playa
            "senderismo": 4,    # Utilidad de hacer senderismo
            "cine": 3    # Utilidad de ir al cine
        }

    def calcular_utilidad_esperada(self, clima):
        utilidades_esperadas = {}
        for actividad in self.utilidades:
            probabilidad_preferencia = self.preferencias[actividad]
            probabilidad_clima_actividad = self.calcular_probabilidad_clima_actividad(clima, actividad)
            utilidad_actividad = self.utilidades[actividad]
            utilidades_esperadas[actividad] = probabilidad_preferencia * probabilidad_clima_actividad * utilidad_actividad
        return utilidades_esperadas

    def calcular_probabilidad_clima_actividad(self, clima, actividad):
        # Simplemente una función ficticia para calcular la probabilidad, podría ser más elaborada en una implementación real
        if clima == "soleado" and actividad == "playa":
            return 0.8
        elif clima == "nublado" and actividad == "senderismo":
            return 0.6
        elif clima == "lluvioso" and actividad == "cine":
            return 0.7
        else:
            return 0.0

# Creamos una instancia del modelo probabilista racional
modelo = ModeloProbabilistaRacional()

# Simulamos diferentes climas
climas = ["soleado", "nublado", "lluvioso"]

# Calculamos la utilidad esperada para cada actividad en cada clima
for clima in climas:
    print(f"Utilidades esperadas para el clima {clima}:")
    utilidades_esperadas = modelo.calcular_utilidad_esperada(clima)
    for actividad, utilidad in utilidades_esperadas.items():
        print(f"{actividad}: {utilidad}")
