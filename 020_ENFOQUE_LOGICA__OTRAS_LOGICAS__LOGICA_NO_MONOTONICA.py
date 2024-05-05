class LogicaNoMonotonica:
    def __init__(self):
        self.hechos = set()  # Conjunto de hechos conocidos
        self.reglas = []      # Lista de reglas de inferencia

    def agregar_hecho(self, hecho):
        """Método para agregar un hecho conocido."""
        self.hechos.add(hecho)

    def agregar_regla(self, antecedente, consecuente):
        """Método para agregar una regla de inferencia."""
        self.reglas.append((antecedente, consecuente))

    def inferir(self):
        """Método para inferir nuevas conclusiones."""
        nuevas_conclusiones = set()
        for antecedente, consecuente in self.reglas:
            if antecedente.issubset(self.hechos):
                nuevas_conclusiones.update(consecuente)
        return nuevas_conclusiones

# Crear un objeto de lógica no monotónica
logica = LogicaNoMonotonica()

# Agregar hechos conocidos
logica.agregar_hecho("pajaro")
logica.agregar_hecho("vuela")

# Agregar reglas de inferencia
logica.agregar_regla({"pajaro"}, {"puede volar"})
logica.agregar_regla({"pajaro", "no vuela"}, {"es un pinguino"})

# Inferir nuevas conclusiones
nuevas_conclusiones = logica.inferir()

# Mostrar las nuevas conclusiones
print("Nuevas conclusiones inferidas:")
for conclusion in nuevas_conclusiones:
    print("-", conclusion)
