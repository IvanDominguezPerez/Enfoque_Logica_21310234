import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Definir el conjunto de datos de ejemplo
# Cada fila representa un estudiante con sus características y la última columna indica si aprobó (1) o no (0)
datos = np.array([
    [18, 2, 4, 0],
    [20, 1, 3, 1],
    [22, 3, 2, 1],
    [19, 2, 4, 0],
    [21, 3, 3, 1],
    [25, 1, 1, 0],
    [23, 2, 2, 1],
    [24, 3, 1, 1],
    [26, 2, 2, 0],
    [28, 1, 1, 0]
])

# Dividir los datos en características (X) y etiquetas (y)
X = datos[:, :-1]
y = datos[:, -1]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo de árbol de decisión
modelo = DecisionTreeClassifier()
modelo.fit(X_entrenamiento, y_entrenamiento)

# Predecir las etiquetas para el conjunto de prueba
y_prediccion = modelo.predict(X_prueba)

# Calcular la precisión del modelo
precision = accuracy_score(y_prueba, y_prediccion)
print("Precisión del modelo:", precision)
