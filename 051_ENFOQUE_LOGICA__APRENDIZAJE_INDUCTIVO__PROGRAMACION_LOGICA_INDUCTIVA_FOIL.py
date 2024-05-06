from collections import Counter
import itertools

class FOIL:
    def __init__(self, target_predicate, positive_examples, negative_examples, max_literals=3):
        self.target_predicate = target_predicate
        self.positive_examples = positive_examples
        self.negative_examples = negative_examples
        self.max_literals = max_literals
        self.rules = []

    def fit(self):
        self.rules = self._foil(self.target_predicate, self.positive_examples, self.negative_examples)

    def _foil(self, target_predicate, positive_examples, negative_examples):
        rules = []
        for i in range(1, self.max_literals + 1):
            rules.extend(self._foil_iteration(target_predicate, positive_examples, negative_examples, i))
        return rules

    def _foil_iteration(self, target_predicate, positive_examples, negative_examples, num_literals):
        rules = []
        for combination in itertools.combinations(range(len(positive_examples[0])), num_literals):
            rule = self._generate_rule(target_predicate, combination)
            if self._is_consistent(rule, positive_examples, negative_examples):
                rules.append(rule)
        return rules

    def _generate_rule(self, target_predicate, literals):
        rule = [target_predicate] + [f"{literal[0]}={literal[1]}" for literal in literals]
        return rule

    def _is_consistent(self, rule, positive_examples, negative_examples):
        for example in positive_examples:
            if not self._satisfies(example, rule):
                return False
        for example in negative_examples:
            if self._satisfies(example, rule):
                return False
        return True

    def _satisfies(self, example, rule):
        for literal in rule[1:]:
            attribute, value = literal.split("=")
            if example[int(attribute)] != value:
                return False
        return True

# Ejemplo de uso
target_predicate = 'play_tennis'
positive_examples = [
    ['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'],
    ['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes']
]
negative_examples = [
    ['overcast', 'cool', 'normal', 'weak', 'change', 'same', 'yes'],
    ['rainy', 'cool', 'normal', 'weak', 'change', 'same', 'no'],
    ['rainy', 'cool', 'normal', 'weak', 'change', 'change', 'no']
]

foil = FOIL(target_predicate, positive_examples, negative_examples)
foil.fit()

# Imprimir las reglas aprendidas
print("Reglas aprendidas:")
for rule in foil.rules:
    print(" ".join(rule))
