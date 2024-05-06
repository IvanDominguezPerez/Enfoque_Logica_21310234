class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        try:
            return self.expression()
        except IndexError:
            raise SyntaxError("Syntax error: Unexpected end of input")

    def expression(self):
        # Analiza una expresión
        return self.disjunction()

    def disjunction(self):
        # Analiza una disyunción
        left = self.conjunction()

        if self.match('OR'):
            self.consume('OR')
            right = self.disjunction()
            return ('OR', left, right)

        return left

    def conjunction(self):
        # Analiza una conjunción
        left = self.negation()

        if self.match('AND'):
            self.consume('AND')
            right = self.conjunction()
            return ('AND', left, right)

        return left

    def negation(self):
        # Analiza una negación
        if self.match('NOT'):
            self.consume('NOT')
            operand = self.negation()
            return ('NOT', operand)
        else:
            return self.atom()

    def atom(self):
        # Analiza un átomo
        if self.match('LPAREN'):
            self.consume('LPAREN')
            result = self.expression()
            self.consume('RPAREN')
            return result
        elif self.match('VAR'):
            var = self.consume('VAR')
            return ('VAR', var[1])  # var[1] contiene el valor del token
        else:
            raise SyntaxError("Syntax error: Unexpected token")

    def match(self, token_type):
        # Verifica si el token actual es del tipo dado
        return self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index][0] == token_type

    def consume(self, token_type):
        # Consume el token actual si es del tipo dado
        if self.match(token_type):
            token = self.tokens[self.current_token_index]
            self.current_token_index += 1
            return token
        else:
            raise SyntaxError("Syntax error: Expected token type '%s'" % token_type)

# Ejemplo de uso
tokens = [('LPAREN', '('), ('VAR', 'A'), ('AND', 'and'), ('VAR', 'B'), ('RPAREN', ')'), ('OR', 'or'), ('NOT', 'not'), ('VAR', 'C')]
parser = Parser(tokens)
parsed_expression = parser.parse()

print("Parsed expression:", parsed_expression)
