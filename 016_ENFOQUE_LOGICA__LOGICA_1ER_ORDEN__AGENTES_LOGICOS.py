class AgenteLogico:
    def __init__(self, reglas):
        self.reglas = reglas

    def tomar_decision(self, estado):
        """Función para que el agente tome una decisión basada en el estado actual."""
        for regla, accion in self.reglas.items():
            if self.verificar_condicion(regla, estado):
                return accion
        return None

    def verificar_condicion(self, regla, estado):
        """Función para verificar si una regla se cumple en el estado actual."""
        # Supongamos que las reglas son de la forma (condición, acción)
        for condicion in regla:
            if condicion not in estado:
                return False
        return True


# Definir reglas para el agente lógico
reglas_agente = {
    ('llueve', 'trae_paraguas'): 'trae_paraguas',
    ('hace_sol', 'trae_gorra'): 'trae_gorra',
    ('hace_frio', 'trae_abrigo'): 'trae_abrigo'
}

# Crear un agente lógico con las reglas definidas
agente = AgenteLogico(reglas_agente)

# Estado del entorno (supongamos que hace frío)
estado_actual = {'hace_frio'}

# Tomar una decisión basada en el estado actual
decision = agente.tomar_decision(estado_actual)

# Imprimir la decisión tomada por el agente
if decision:
    print("El agente decide:", decision)
else:
    print("El agente no puede tomar una decisión en este estado.")
