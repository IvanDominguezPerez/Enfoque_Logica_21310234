from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import numpy as np

class ClasificadorBoosting:
    def __init__(self, n_estimators=50, max_depth=1):
        self.n_estimators = n_estimators  # Número de estimadores (árboles de decisión)
        self.max_depth = max_depth  # Profundidad máxima de cada árbol
        self.estimadores = []  # Lista para almacenar los estimadores
        self.alphas = []  # Lista para almacenar los pesos de los estimadores

    def fit(self, X, y):
        n_samples, _ = X.shape
        # Inicializar los pesos de las muestras
        pesos = np.full(n_samples, (1 / n_samples))

        for _ in range(self.n_estimators):
            # Crear un árbol de decisión débil
            arbol = DecisionTreeClassifier(max_depth=self.max_depth)
            # Entrenar el árbol con los pesos de las muestras
            arbol.fit(X, y, sample_weight=pesos)
            # Predecir las etiquetas para calcular el error ponderado
            predicciones = arbol.predict(X)
            # Calcular el error ponderado
            error = np.sum(pesos * (predicciones != y))
            # Calcular el peso del estimador
            alpha = 0.5 * np.log((1 - error) / (error + 1e-10))
            # Actualizar los pesos de las muestras
            pesos *= np.exp(-alpha * y * predicciones)
            # Normalizar los pesos
            pesos /= np.sum(pesos)
            # Guardar el árbol y el peso asociado
            self.estimadores.append(arbol)
            self.alphas.append(alpha)

    def predict(self, X):
        # Inicializar las predicciones como ceros
        predicciones = np.zeros(X.shape[0])
        for alpha, arbol in zip(self.alphas, self.estimadores):
            # Agregar las predicciones ponderadas de cada árbol
            predicciones += alpha * arbol.predict(X)
        # Convertir las predicciones a etiquetas binarias
        return np.sign(predicciones)

# Ejemplo de uso
# Generar un conjunto de datos sintéticos
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un clasificador Boosting
boosting = ClasificadorBoosting(n_estimators=50, max_depth=1)

# Entrenar el clasificador
boosting.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
predicciones = boosting.predict(X_test)

# Evaluar la precisión del clasificador
precision = np.mean(predicciones == y_test)
print("Precisión del clasificador Boosting:", precision)
