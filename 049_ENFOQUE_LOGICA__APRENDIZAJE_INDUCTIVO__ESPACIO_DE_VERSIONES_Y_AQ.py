class VersionSpace:
    def __init__(self):
        self.version_space = None

    def fit(self, X_train, y_train):
        # Inicializamos el espacio de versiones con la primera instancia
        self.version_space = [X_train[0]]

        for i in range(1, len(X_train)):
            # Para cada instancia en el conjunto de entrenamiento
            x = X_train[i]
            y = y_train[i]

            # Si la instancia es positiva, eliminamos todas las hipótesis en el espacio de versiones que no la cubren
            if y == 1:
                self.version_space = [v for v in self.version_space if self.cubre(v, x)]

            # Si la instancia es negativa, eliminamos la instancia del espacio de versiones
            elif y == 0:
                self.version_space = [v for v in self.version_space if not self.cubre(v, x)]

    def predict(self, X_test):
        y_pred = []
        for x in X_test:
            # Si hay al menos una hipótesis en el espacio de versiones que cubre la instancia, la predicción es positiva
            if any(self.cubre(v, x) for v in self.version_space):
                y_pred.append(1)
            else:
                y_pred.append(0)
        return y_pred

    def cubre(self, hipotesis, instancia):
        # Verifica si la hipótesis cubre la instancia (todos los valores coinciden)
        return all(h == i or h == '?' for h, i in zip(hipotesis, instancia))

# Ejemplo de uso
X_train = [
    ['sol', 'caluroso', 'alta', 'debil'],
    ['sol', 'caluroso', 'alta', 'fuerte'],
    ['nublado', 'caluroso', 'alta', 'debil'],
    ['lluvioso', 'templado', 'alta', 'debil'],
]
y_train = [0, 0, 1, 1]

X_test = [
    ['sol', 'caluroso', 'alta', 'fuerte'],
    ['lluvioso', 'templado', 'normal', 'fuerte'],
]

vs = VersionSpace()
vs.fit(X_train, y_train)
y_pred = vs.predict(X_test)

print("Predicciones:", y_pred)
