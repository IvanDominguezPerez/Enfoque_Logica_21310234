class LogicaPorDefecto:
    def __init__(self):
        self.hechos = set()  # Conjunto de hechos conocidos
        self.regla_por_defecto = None  # Regla por defecto

    def agregar_hecho(self, hecho):
        """Método para agregar un hecho conocido."""
        self.hechos.add(hecho)

    def agregar_regla_por_defecto(self, regla):
        """Método para agregar una regla por defecto."""
        self.regla_por_defecto = regla

    def inferir(self):
        """Método para inferir nuevas conclusiones."""
        if self.regla_por_defecto:
            # Aplicar la regla por defecto si no hay evidencia en contra
            if not any(hecho in self.hechos for hecho in self.regla_por_defecto[0]):
                return self.regla_por_defecto[1]
        return set()  # Si no se puede inferir nada, retornar un conjunto vacío

# Crear un objeto de lógica por defecto
logica = LogicaPorDefecto()

# Agregar hechos conocidos
logica.agregar_hecho("pajaro")
logica.agregar_hecho("vuela")

# Definir una regla por defecto: si un animal tiene plumas y no vuela, entonces es un avestruz
logica.agregar_regla_por_defecto(({"plumas", "no vuela"}, {"es un avestruz"}))

# Inferir nuevas conclusiones
nuevas_conclusiones = logica.inferir()

# Mostrar las nuevas conclusiones
print("Nuevas conclusiones inferidas:")
for conclusion in nuevas_conclusiones:
    print("-", conclusion)
