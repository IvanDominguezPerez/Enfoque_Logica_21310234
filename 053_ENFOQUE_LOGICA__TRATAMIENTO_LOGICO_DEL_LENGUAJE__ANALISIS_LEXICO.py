import re

class Lexer:
    def __init__(self, expression):
        self.expression = expression
        self.tokens = []

    def tokenize(self):
        # Definición de tokens mediante expresiones regulares
        patterns = [
            (r'\(', 'LPAREN'),
            (r'\)', 'RPAREN'),
            (r'and', 'AND'),
            (r'or', 'OR'),
            (r'not', 'NOT'),
            (r'[a-zA-Z_]\w*', 'VAR'),  # Identificadores de variables
        ]

        # Construcción de la expresión regular combinada
        combined_patterns = '|'.join('(?P<%s>%s)' % pair for pair in patterns)
        pattern = re.compile(combined_patterns)

        # Tokenización de la expresión
        for match in pattern.finditer(self.expression):
            token_type = match.lastgroup
            token_value = match.group()

            self.tokens.append((token_type, token_value))

        return self.tokens

# Ejemplo de uso
expression = "(A and B) or not C"
lexer = Lexer(expression)
tokens = lexer.tokenize()

print("Tokens:")
for token in tokens:
    print(token)
