import numpy as np

class NodoDecision:
    def __init__(self, caracteristica=None, valor=None, resultados=None, verdadero=None, falso=None):
        self.caracteristica = caracteristica  # Característica que se evalúa en este nodo
        self.valor = valor  # Valor de la característica que se compara en este nodo
        self.resultados = resultados  # Resultados (etiquetas) en este nodo si es una hoja
        self.verdadero = verdadero  # Nodo hijo si la característica es verdadera
        self.falso = falso  # Nodo hijo si la característica es falsa

def entropia(datos):
    # Calcula la entropía del conjunto de datos
    etiquetas = datos[:, -1]
    clases, cuenta = np.unique(etiquetas, return_counts=True)
    probabilidad = cuenta / len(etiquetas)
    entropia = -np.sum(probabilidad * np.log2(probabilidad))
    return entropia

def ganancia_informacion(datos, caracteristica_index):
    # Calcula la ganancia de información para una característica dada
    entropia_total = entropia(datos)
    valores = datos[:, caracteristica_index]
    clases, cuenta = np.unique(valores, return_counts=True)
    peso = cuenta / len(valores)
    ganancia = entropia_total
    for clase, p in zip(clases, peso):
        subconjunto = datos[valores == clase]
        ganancia -= p * entropia(subconjunto)
    return ganancia

def construir_arbol(datos, caracteristicas):
    # Función recursiva para construir el árbol de decisión
    if len(np.unique(datos[:, -1])) == 1:
        return NodoDecision(resultados=np.unique(datos[:, -1]))

    ganancias = [ganancia_informacion(datos, i) for i in range(len(caracteristicas))]
    mejor_caracteristica_index = np.argmax(ganancias)
    mejor_caracteristica = caracteristicas[mejor_caracteristica_index]

    nodo = NodoDecision(caracteristica=mejor_caracteristica)

    valores = np.unique(datos[:, mejor_caracteristica_index])
    for valor in valores:
        subconjunto = datos[datos[:, mejor_caracteristica_index] == valor]
        nuevo_caracteristicas = np.delete(caracteristicas, mejor_caracteristica_index)
        nodo_hijo = construir_arbol(subconjunto, nuevo_caracteristicas)
        if valor == 0:
            nodo.falso = nodo_hijo
        else:
            nodo.verdadero = nodo_hijo
    return nodo

def predecir_muestra(arbol, muestra):
    # Función para predecir una muestra utilizando el árbol de decisión
    if arbol.resultados is not None:
        return arbol.resultados
    valor = muestra[arbol.caracteristica]
    rama = arbol.verdadero if valor == 1 else arbol.falso
    return predecir_muestra(rama, muestra)

# Ejemplo de datos de entrada
# Cada fila representa una muestra, y la última columna es la etiqueta (0 o 1)
datos = np.array([
    [1, 1, 0],
    [1, 0, 0],
    [0, 1, 1],
    [0, 0, 1]
])

# Nombre de las características (en este caso, solo "Característica 1" y "Característica 2")
caracteristicas = ["Característica 1", "Característica 2"]

# Construir el árbol de decisión
arbol = construir_arbol(datos, caracteristicas)

# Ejemplo de predicción para una nueva muestra
nueva_muestra = np.array([1, 1])
print("Predicción para la nueva muestra:", predecir_muestra(arbol, nueva_muestra))
