import numpy as np
from sklearn.linear_model import LinearRegression

class NodoRegresion:
    def __init__(self, caracteristica=None, valor=None, resultado=None, modelo=None, hijos=None):
        self.caracteristica = caracteristica  # Característica que se evalúa en este nodo
        self.valor = valor  # Valor de la característica que se compara en este nodo
        self.resultado = resultado  # Valor de regresión en este nodo si es una hoja
        self.modelo = modelo  # Modelo lineal asociado a este nodo si es una hoja
        self.hijos = hijos  # Sub-árboles de regresión asociados a este nodo

def error_cuadratico_medio(predicciones, etiquetas):
    # Calcula el error cuadrático medio entre las predicciones y las etiquetas reales
    return np.mean((predicciones - etiquetas) ** 2)

def construir_arbol_regresion(datos, caracteristicas, max_profundidad):
    # Función recursiva para construir el árbol de regresión
    if max_profundidad == 0 or len(np.unique(datos[:, -1])) == 1:
        # Si alcanzamos la profundidad máxima o no hay variabilidad en la etiqueta, retornamos una hoja
        return NodoRegresion(resultado=np.mean(datos[:, -1]))

    mejor_error = float('inf')
    mejor_caracteristica = None
    mejor_valor = None
    mejor_hijos = None

    for caracteristica_index in range(len(caracteristicas)):
        valores = np.unique(datos[:, caracteristica_index])
        for valor in valores:
            subconjunto = datos[datos[:, caracteristica_index] == valor]
            subcaracteristicas = np.delete(caracteristicas, caracteristica_index)
            error_total = 0

            for i in range(10):  # Utilizamos validación cruzada de 10 pliegues
                np.random.shuffle(subconjunto)
                train_size = int(0.9 * len(subconjunto))
                train_data, val_data = subconjunto[:train_size], subconjunto[train_size:]
                
                if len(train_data) == 0 or len(val_data) == 0:
                    continue

                modelo = LinearRegression()
                modelo.fit(train_data[:, :-1], train_data[:, -1])
                predicciones = modelo.predict(val_data[:, :-1])
                error_total += error_cuadratico_medio(predicciones, val_data[:, -1])

            error_promedio = error_total / 10

            if error_promedio < mejor_error:
                mejor_error = error_promedio
                mejor_caracteristica = caracteristicas[caracteristica_index]
                mejor_valor = valor
                mejor_hijos = (train_data, val_data)

    if mejor_caracteristica is None:  # Si no encontramos una buena partición, retornamos una hoja
        return NodoRegresion(resultado=np.mean(datos[:, -1]))

    izquierdo = construir_arbol_regresion(mejor_hijos[0], np.delete(caracteristicas, caracteristicas.index(mejor_caracteristica)), max_profundidad - 1)
    derecho = construir_arbol_regresion(mejor_hijos[1], np.delete(caracteristicas, caracteristicas.index(mejor_caracteristica)), max_profundidad - 1)

    return NodoRegresion(caracteristica=mejor_caracteristica, valor=mejor_valor, hijos=(izquierdo, derecho))

def predecir_muestra_regresion(arbol, muestra):
    # Función para predecir un valor de regresión para una nueva muestra utilizando el árbol de regresión
    if arbol.resultado is not None:
        return arbol.resultado
    if muestra[arbol.caracteristica] == arbol.valor:
        return predecir_muestra_regresion(arbol.hijos[0], muestra)
    else:
        return predecir_muestra_regresion(arbol.hijos[1], muestra)

# Ejemplo de datos de entrada
# Cada fila representa una muestra, y la última columna es la etiqueta
datos = np.array([
    [1, 2, 3, 5],
    [2, 3, 4, 6],
    [3, 4, 5, 7],
    [4, 5, 6, 8]
])

# Nombre de las características
caracteristicas = ["Característica 1", "Característica 2", "Característica 3"]

# Construir el árbol de regresión con una profundidad máxima de 2
arbol = construir_arbol_regresion(datos, caracteristicas, max_profundidad=2)

# Ejemplo de predicción para una nueva muestra
nueva_muestra = np.array([1, 2, 3])
print("Predicción para la nueva muestra:", predecir_muestra_regresion(arbol, nueva_muestra))
