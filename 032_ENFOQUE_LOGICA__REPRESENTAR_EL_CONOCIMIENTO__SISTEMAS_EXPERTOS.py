class SistemaExperto:
    def __init__(self):
        self.base_conocimiento = {
            "soleado": "ir a la playa",
            "nublado": "hacer senderismo",
            "lluvioso": "ver una película en casa"
        }

    def recomendar_actividad(self, clima):
        # Verificamos si el clima está en nuestra base de conocimiento
        if clima in self.base_conocimiento:
            return self.base_conocimiento[clima]
        else:
            return "No se puede determinar una actividad para este clima"

# Creamos una instancia del sistema experto
sistema_experto = SistemaExperto()

# Consultamos por una recomendación para diferentes tipos de clima
print("Recomendación para clima soleado:", sistema_experto.recomendar_actividad("soleado"))
print("Recomendación para clima nublado:", sistema_experto.recomendar_actividad("nublado"))
print("Recomendación para clima lluvioso:", sistema_experto.recomendar_actividad("lluvioso"))
print("Recomendación para clima ventoso:", sistema_experto.recomendar_actividad("ventoso"))
