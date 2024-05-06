from collections import Counter
import numpy as np

class DecisionTree:
    def __init__(self):
        self.tree = None

    def fit(self, X_train, y_train):
        self.tree = self._build_tree(X_train, y_train)

    def predict(self, X_test):
        return [self._classify(x, self.tree) for x in X_test]

    def _build_tree(self, X, y):
        # Si todos los ejemplos tienen la misma etiqueta, devolver esa etiqueta como nodo hoja
        if len(set(y)) == 1:
            return y[0]

        # Si no quedan atributos para dividir, devolver la etiqueta más común como nodo hoja
        if len(X[0]) == 0:
            return Counter(y).most_common(1)[0][0]

        # Encontrar el mejor atributo para dividir y su valor de corte
        best_attribute, best_threshold = self._find_best_split(X, y)

        # Dividir el conjunto de datos en subconjuntos
        left_idxs = [i for i, x in enumerate(X) if x[best_attribute] <= best_threshold]
        right_idxs = [i for i, x in enumerate(X) if x[best_attribute] > best_threshold]

        # Construir subárboles recursivamente
        left_subtree = self._build_tree(X[left_idxs], y[left_idxs])
        right_subtree = self._build_tree(X[right_idxs], y[right_idxs])

        return {'attribute': best_attribute, 'threshold': best_threshold,
                'left': left_subtree, 'right': right_subtree}

    def _find_best_split(self, X, y):
        best_gain = -1
        best_attribute = None
        best_threshold = None

        # Iterar sobre cada atributo
        for i in range(len(X[0])):
            # Obtener todos los valores únicos del atributo
            values = set(x[i] for x in X)

            # Iterar sobre cada par de valores adyacentes
            for val in sorted(values):
                threshold = val
                left_idxs = [j for j, x in enumerate(X) if x[i] <= threshold]
                right_idxs = [j for j, x in enumerate(X) if x[i] > threshold]

                # Calcular la ganancia de información de la división
                gain = self._information_gain(y, y[left_idxs], y[right_idxs])

                # Actualizar el mejor punto de división si es necesario
                if gain > best_gain:
                    best_gain = gain
                    best_attribute = i
                    best_threshold = threshold

        return best_attribute, best_threshold

    def _information_gain(self, parent, left_child, right_child):
        # Calcular la entropía del nodo padre
        entropy_parent = self._entropy(parent)

        # Calcular la entropía ponderada de los nodos hijos
        entropy_children = (len(left_child) / len(parent)) * self._entropy(left_child) + \
                           (len(right_child) / len(parent)) * self._entropy(right_child)

        # Calcular la ganancia de información
        return entropy_parent - entropy_children

    def _entropy(self, y):
        # Calcular la entropía del conjunto de etiquetas
        if len(y) == 0:
            return 0

        counts = Counter(y)
        probs = [count / len(y) for count in counts.values()]
        return -sum(p * np.log2(p) for p in probs)

    def _classify(self, x, tree):
        if isinstance(tree, dict):
            attribute = tree['attribute']
            threshold = tree['threshold']
            if x[attribute] <= threshold:
                return self._classify(x, tree['left'])
            else:
                return self._classify(x, tree['right'])
        else:
            return tree

    def explain(self, x):
        explanation = []
        node = self.tree

        while isinstance(node, dict):
            attribute = node['attribute']
            threshold = node['threshold']
            if x[attribute] <= threshold:
                explanation.append(f"If {attribute} <= {threshold}:")
                node = node['left']
            else:
                explanation.append(f"If {attribute} > {threshold}:")
                node = node['right']

        explanation.append(f"Predicted class: {node}")
        return explanation

# Ejemplo de uso
X_train = np.array([
    [1, 20, 0],
    [2, 25, 1],
    [2, 30, 0],
    [3, 35, 1],
    [3, 40, 0]
])
y_train = np.array([0, 1, 1, 1, 0])

X_test = np.array([
    [2, 27, 0],
    [3, 38, 1]
])

dt = DecisionTree()
dt.fit(X_train, y_train)

# Predicciones
predictions = dt.predict(X_test)
print("Predictions:", predictions)

# Explicaciones
for i, x in enumerate(X_test):
    explanation = dt.explain(x)
    print(f"\nExplanation for instance {i + 1}:")
    for line in explanation:
        print(line)
