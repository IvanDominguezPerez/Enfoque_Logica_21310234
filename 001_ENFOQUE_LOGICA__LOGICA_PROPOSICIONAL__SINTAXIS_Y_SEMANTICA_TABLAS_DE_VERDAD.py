import itertools

# Función para evaluar una expresión lógica dada
def evaluate_expression(expression, variable_values):
    # Reemplazar las variables en la expresión con sus valores correspondientes
    for var, val in variable_values.items():
        expression = expression.replace(var, str(val))
    # Evaluar la expresión lógica utilizando la función eval de Python
    result = eval(expression)
    return result

# Función para generar y mostrar una tabla de verdad para una expresión dada
def truth_table(expression, variables):
    # Generar todas las combinaciones posibles de valores de las variables
    variable_combinations = list(itertools.product([0, 1], repeat=len(variables)))

    # Imprimir el encabezado de la tabla de verdad
    print('|', end=' ')
    for var in variables:
        print(var, '|', end=' ')
    print(expression, '|')

    # Imprimir la línea separadora
    print('|', end=' ')
    for _ in range(len(variables) + 1):
        print('-', '|', end=' ')
    print()

    # Imprimir los valores de verdad para cada combinación de variables
    for values in variable_combinations:
        variable_values = dict(zip(variables, values))
        result = evaluate_expression(expression, variable_values)
        print('|', end=' ')
        for val in values:
            print(val, '|', end=' ')
        print(result, '|')

# Ejemplo de uso
expression = "(A and B) or (not C)"
variables = ["A", "B", "C"]
truth_table(expression, variables)
