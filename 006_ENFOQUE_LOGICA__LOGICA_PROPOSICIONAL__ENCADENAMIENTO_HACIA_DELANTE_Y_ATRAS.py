class KnowledgeBase:
    def __init__(self):
        self.facts = set()  # Hechos conocidos
        self.rules = []     # Reglas de inferencia

    def add_fact(self, fact):
        """Agrega un hecho a la base de conocimiento."""
        self.facts.add(fact)

    def add_rule(self, antecedent, consequent):
        """Agrega una regla de inferencia a la base de conocimiento."""
        self.rules.append((antecedent, consequent))

    def forward_chaining(self):
        """Encadenamiento hacia adelante para derivar nuevos hechos."""
        new_facts = True
        while new_facts:
            new_facts = False
            for rule in self.rules:
                antecedent, consequent = rule
                if set(antecedent).issubset(self.facts) and consequent not in self.facts:
                    self.facts.add(consequent)
                    new_facts = True

    def backward_chaining(self, query):
        """Encadenamiento hacia atrás para verificar si una consulta es verdadera."""
        return self._backward_chaining(query, set())

    def _backward_chaining(self, query, visited):
        if query in self.facts:
            return True
        for rule in self.rules:
            antecedent, consequent = rule
            if consequent == query:
                if self._backward_chaining(antecedent, visited):
                    return True
        return False

# Ejemplo de uso
kb = KnowledgeBase()

# Agregar hechos y reglas a la base de conocimiento
kb.add_fact("P")
kb.add_fact("Q")
kb.add_rule(["P", "Q"], "R")
kb.add_rule(["R"], "S")

# Realizar encadenamiento hacia adelante para derivar nuevos hechos
kb.forward_chaining()

# Realizar encadenamiento hacia atrás para verificar una consulta
query = "S"
result = kb.backward_chaining(query)

# Imprimir el resultado de la consulta
if result:
    print("La consulta {} es verdadera.".format(query))
else:
    print("La consulta {} es falsa.".format(query))
