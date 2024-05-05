from random import choice

class HillClimbingSolver:
    def __init__(self, variables, objective_function, max_iterations=1000):
        self.variables = variables                    # Lista de variables proposicionales
        self.objective_function = objective_function  # Función objetivo a maximizar
        self.max_iterations = max_iterations          # Número máximo de iteraciones

    def solve(self):
        current_assignment = {var: choice([True, False]) for var in self.variables}  # Asignación inicial aleatoria
        current_value = self.objective_function(current_assignment)  # Valor de la función objetivo inicial
        for _ in range(self.max_iterations):
            neighbors = self._generate_neighbors(current_assignment)  # Generar vecinos de la asignación actual
            best_neighbor, best_value = max(neighbors, key=lambda x: self.objective_function(x))  # Encontrar el mejor vecino
            if best_value <= current_value:
                break  # No hay mejora, terminar la búsqueda
            current_assignment, current_value = best_neighbor, best_value  # Actualizar la asignación y el valor
        return current_assignment, current_value

    def _generate_neighbors(self, assignment):
        """Genera vecinos de la asignación actual cambiando el valor de una variable aleatoria."""
        neighbors = []
        for var in self.variables:
            neighbor_assignment = assignment.copy()
            neighbor_assignment[var] = not neighbor_assignment[var]  # Cambiar el valor de una variable aleatoria
            neighbors.append((neighbor_assignment, self.objective_function(neighbor_assignment)))
        return neighbors

# Ejemplo de uso
def objective_function(assignment):
    """Función objetivo: contar el número de variables verdaderas."""
    return sum(1 for value in assignment.values() if value)

variables = ['p', 'q', 'r']  # Variables proposicionales
solver = HillClimbingSolver(variables, objective_function)
solution, value = solver.solve()

print("Solución encontrada:", solution)
print("Valor de la función objetivo:", value)
