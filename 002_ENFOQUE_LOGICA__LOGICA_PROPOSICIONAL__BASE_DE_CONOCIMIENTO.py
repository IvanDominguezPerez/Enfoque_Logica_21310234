class KnowledgeBase:
    def __init__(self):
        self.clauses = []  # Inicialmente, la base de conocimiento está vacía

    def add_clause(self, clause):
        """Agrega una cláusula a la base de conocimiento."""
        self.clauses.append(clause)

    def remove_clause(self, clause):
        """Elimina una cláusula de la base de conocimiento."""
        if clause in self.clauses:
            self.clauses.remove(clause)
        else:
            print("La cláusula no está en la base de conocimiento.")

    def ask(self, query):
        """Verifica si una consulta es verdadera según la base de conocimiento."""
        for clause in self.clauses:
            if set(query).issubset(set(clause)):
                return True
        return False

# Ejemplo de uso
kb = KnowledgeBase()

# Agregar algunas cláusulas a la base de conocimiento
kb.add_clause(["A", "B"])
kb.add_clause(["C", "-B"])
kb.add_clause(["A", "D", "-C"])

# Consultas
query1 = ["A"]
query2 = ["B", "-D"]

# Verificar las consultas con la base de conocimiento
print("¿La consulta {} es verdadera?".format(query1), kb.ask(query1))
print("¿La consulta {} es verdadera?".format(query2), kb.ask(query2))
