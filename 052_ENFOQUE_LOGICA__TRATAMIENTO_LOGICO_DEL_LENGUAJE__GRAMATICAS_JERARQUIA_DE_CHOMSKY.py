class ChomskyGrammar:
    def __init__(self, terminals, nonterminals, start_symbol, productions):
        self.terminals = terminals
        self.nonterminals = nonterminals
        self.start_symbol = start_symbol
        self.productions = productions

    def is_regular(self):
        """
        Verifica si la gramática es regular (Tipo 3 de la jerarquía de Chomsky).
        """
        for production in self.productions:
            left, right = production.split("->")
            left = left.strip()
            right = right.strip()

            # Solo se permiten las siguientes formas de producción en una gramática regular:
            # - A -> aB
            # - A -> a
            if len(left) != 1 or left not in self.nonterminals:
                return False

            if len(right) == 1 and right in self.terminals:
                continue

            if len(right) == 2 and right[0] in self.terminals and right[1] in self.nonterminals:
                continue

            return False

        return True

# Ejemplo de uso
terminals = {'a', 'b'}
nonterminals = {'S', 'A'}
start_symbol = 'S'
productions = ['S -> aA', 'S -> b', 'A -> bS', 'A -> a']

grammar = ChomskyGrammar(terminals, nonterminals, start_symbol, productions)

if grammar.is_regular():
    print("La gramática es regular.")
else:
    print("La gramática no es regular.")
