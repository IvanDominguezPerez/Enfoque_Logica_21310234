class KnowledgeBase:
    def __init__(self):
        self.facts = set()    # Conjunto de hechos
        self.rules = []       # Lista de reglas

    def add_fact(self, fact):
        """Añade un hecho a la base de conocimiento."""
        self.facts.add(fact)

    def add_rule(self, rule):
        """Añade una regla a la base de conocimiento."""
        self.rules.append(rule)

    def forward_chaining(self, query):
        """Encadenamiento hacia adelante para buscar una respuesta."""
        agenda = list(self.facts)  # Inicializar la agenda con los hechos conocidos

        while agenda:
            fact = agenda.pop(0)   # Tomar un hecho de la agenda
            if fact == query:      # Comprobar si hemos alcanzado la respuesta
                return True
            for rule in self.rules:    # Aplicar todas las reglas a los hechos conocidos
                if rule[0] == fact:    # Si la premisa de la regla coincide con el hecho
                    new_fact = rule[1] # Obtener la conclusión de la regla
                    if new_fact not in self.facts:  # Si la conclusión no es un hecho conocido
                        agenda.append(new_fact)     # Añadirlo a la agenda
                        self.facts.add(new_fact)     # Añadirlo a los hechos conocidos
        return False

    def backward_chaining(self, query):
        """Encadenamiento hacia atrás para buscar una respuesta."""
        return self._backward_chaining(query, set())

    def _backward_chaining(self, query, visited):
        """Función auxiliar recursiva para encadenamiento hacia atrás."""
        if query in self.facts:   # Si el query es un hecho conocido, retornamos True
            return True

        for rule in self.rules:  # Recorremos todas las reglas
            if rule[1] == query: # Si la conclusión de la regla coincide con el query
                premises = rule[0]   # Tomamos las premisas de la regla
                if all(premise in self.facts or self._backward_chaining(premise, visited) for premise in premises): # Si todas las premisas se cumplen
                    return True
        return False


# Crear una base de conocimiento
kb = KnowledgeBase()

# Agregar algunos hechos a la base de conocimiento
kb.add_fact('A')
kb.add_fact('B')

# Agregar algunas reglas a la base de conocimiento (premisa, conclusión)
kb.add_rule(('A', 'C'))
kb.add_rule(('B', 'C'))
kb.add_rule(('C', 'D'))

# Realizar consultas utilizando encadenamiento hacia adelante y hacia atrás
print("Encadenamiento hacia adelante:")
print("Resultado de la consulta 'D':", kb.forward_chaining('D'))
print("Resultado de la consulta 'E':", kb.forward_chaining('E'))

print("\nEncadenamiento hacia atrás:")
print("Resultado de la consulta 'D':", kb.backward_chaining('D'))
print("Resultado de la consulta 'E':", kb.backward_chaining('E'))
