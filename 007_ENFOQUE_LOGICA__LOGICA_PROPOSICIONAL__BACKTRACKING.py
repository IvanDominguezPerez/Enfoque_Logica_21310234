class BacktrackingSolver:
    def __init__(self, variables, clauses):
        self.variables = variables  # Lista de variables proposicionales
        self.clauses = clauses      # Lista de cláusulas en forma de listas de literales

    def is_satisfiable(self):
        assignment = {}  # Diccionario para almacenar las asignaciones de variables
        return self._backtrack(assignment)

    def _backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            # Se ha asignado un valor a todas las variables, verificar si todas las cláusulas son verdaderas
            return all(self._evaluate_clause(clause, assignment) for clause in self.clauses)
        
        variable = self._select_unassigned_variable(assignment)
        for value in [True, False]:
            assignment[variable] = value
            if self._is_consistent(assignment):
                if self._backtrack(assignment):
                    return True
            del assignment[variable]
        return False

    def _evaluate_clause(self, clause, assignment):
        # Evaluar si una cláusula es verdadera dada una asignación de variables
        return any(assignment[literal[0]] if literal[1] else not assignment[literal[0]] for literal in clause)

    def _select_unassigned_variable(self, assignment):
        # Seleccionar una variable no asignada para asignarle un valor
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def _is_consistent(self, assignment):
        # Verificar si la asignación actual de variables es consistente con las cláusulas
        for clause in self.clauses:
            if not self._evaluate_clause(clause, assignment):
                return False
        return True

# Ejemplo de uso
variables = ['p', 'q', 'r']
clauses = [[('p', True), ('q', True)], [('p', False), ('r', False)], [('q', True), ('r', True)]]

solver = BacktrackingSolver(variables, clauses)
is_satisfiable = solver.is_satisfiable()

if is_satisfiable:
    print("La fórmula es satisfacible.")
else:
    print("La fórmula no es satisfacible.")
