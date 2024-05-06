class SemanticAnalyzer:
    def __init__(self, parsed_expression):
        self.parsed_expression = parsed_expression

    def analyze(self):
        try:
            return self.validate(self.parsed_expression)
        except ValueError as e:
            raise ValueError("Semantic error: " + str(e))

    def validate(self, expression):
        if expression[0] == 'VAR':
            # Verifica si una variable está bien definida
            if expression[1] in {'A', 'B', 'C'}:
                return True
            else:
                raise ValueError("Undefined variable: {}".format(expression[1]))
        elif expression[0] == 'NOT':
            # Verifica la negación de una expresión
            return self.validate(expression[1])
        elif expression[0] in {'AND', 'OR'}:
            # Verifica la disyunción o conjunción de dos expresiones
            return self.validate(expression[1]) and self.validate(expression[2])
        else:
            raise ValueError("Invalid expression: {}".format(expression))

# Ejemplo de uso
parsed_expression = ('AND', ('VAR', 'A'), ('OR', ('VAR', 'B'), ('NOT', ('VAR', 'C'))))
analyzer = SemanticAnalyzer(parsed_expression)
is_valid = analyzer.analyze()

print("Is the expression valid?", is_valid)
