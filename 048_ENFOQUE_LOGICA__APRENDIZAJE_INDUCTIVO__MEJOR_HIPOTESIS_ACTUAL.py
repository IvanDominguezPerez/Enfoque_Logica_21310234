from collections import defaultdict

class MostFrequentHypothesis:
    def __init__(self):
        self.hypothesis = defaultdict(int)

    def fit(self, X_train, y_train):
        for features, label in zip(X_train, y_train):
            self.hypothesis[tuple(features)] += label

    def predict(self, X_test):
        y_pred = []
        for features in X_test:
            label = self.hypothesis[tuple(features)] > 0
            y_pred.append(label)
        return y_pred

# Ejemplo de uso
X_train = [[1, 0], [0, 1], [1, 1], [0, 0]]
y_train = [1, 0, 1, 0]

X_test = [[1, 0], [0, 1], [1, 1], [0, 0]]

mfc = MostFrequentHypothesis()
mfc.fit(X_train, y_train)
y_pred = mfc.predict(X_test)

print("Predicciones:", y_pred)
