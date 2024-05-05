class KnowledgeBase:
    def __init__(self):
        self.clauses = []  # Lista de cláusulas en la base de conocimiento

    def add_clause(self, clause):
        """Agrega una cláusula a la base de conocimiento."""
        self.clauses.append(clause)

    def resolve(self, clause1, clause2):
        """Realiza la operación de resolución entre dos cláusulas."""
        resolvents = []  # Lista para almacenar los resolventes resultantes
        for literal in clause1:
            if literal.startswith("-"):
                pos_literal = literal[1:]
                if pos_literal in clause2:
                    resolvent = [l for l in clause1 if l != literal] + [l for l in clause2 if l != pos_literal]
                    if not resolvent in resolvents:
                        resolvents.append(resolvent)
        return resolvents

    def ask(self, query):
        """Realiza la inferencia sobre una consulta en la base de conocimiento."""
        new_clause = query  # La nueva cláusula es la consulta
        while True:
            clauses_to_resolve = [clause for clause in self.clauses if any(literal in clause for literal in new_clause)]
            new_clauses = []
            for clause in clauses_to_resolve:
                for res_clause in self.resolve(clause, new_clause):
                    if not res_clause:
                        return True  # Se ha llegado a una contradicción, la consulta es verdadera
                    if not res_clause in new_clauses:
                        new_clauses.append(res_clause)
            if not new_clauses:
                return False  # No se puede inferir la consulta
            for clause in new_clauses:
                if not clause in self.clauses:
                    self.clauses.append(clause)
            new_clause = new_clauses[0]  # Actualizar la nueva cláusula para continuar la resolución

# Ejemplo de uso
kb = KnowledgeBase()

# Agregar algunas cláusulas a la base de conocimiento
kb.add_clause(["A", "B"])
kb.add_clause(["-A", "C"])
kb.add_clause(["-B", "D"])
kb.add_clause(["-C", "E"])

# Consulta
query = ["D", "E"]

# Realizar la inferencia sobre la consulta
result = kb.ask(query)

# Imprimir el resultado de la inferencia
if result:
    print("La consulta es verdadera.")
else:
    print("La consulta es falsa.")
