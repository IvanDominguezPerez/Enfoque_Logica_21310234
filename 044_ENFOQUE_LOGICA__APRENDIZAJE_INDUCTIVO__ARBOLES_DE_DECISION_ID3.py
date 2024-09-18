#Practica: 044_ENFOQUE_LOGICA__APRENDIZAJE_INDUCTIVO__ARBOLES_DE_DESICION_ID3
#Alumno: IVAN_DOMINGUEZ
#Registro: 21310234
#Grupo: 7F1

# Importamos las bibliotecas necesarias
from sklearn import datasets  # Para cargar ejemplos de datos
from sklearn.model_selection import train_test_split  # Para dividir los datos en entrenamiento y prueba
from sklearn.tree import DecisionTreeClassifier  # Para crear el árbol de decisión
from sklearn import tree  # Para visualizar el árbol
import pandas as pd  # Para manejar datos estructurados como tablas
import numpy as np  # Para operaciones matemáticas
import matplotlib.pyplot as plt  # Para visualizar el árbol

# Creamos un conjunto de datos que simula condiciones climáticas y decisiones para llevar paraguas.
data = {'Clima': ['soleado', 'soleado', 'nublado', 'lluvioso', 'lluvioso', 'lluvioso', 'nublado', 'soleado', 'soleado', 'lluvioso'],
        'Temperatura': ['caliente', 'caliente', 'caliente', 'templado', 'frío', 'frío', 'frío', 'templado', 'frío', 'templado'],
        'Humedad': ['alta', 'alta', 'alta', 'alta', 'normal', 'normal', 'normal', 'alta', 'normal', 'alta'],
        'Viento': ['débil', 'fuerte', 'débil', 'débil', 'débil', 'fuerte', 'fuerte', 'débil', 'débil', 'fuerte'],
        'Paraguas': ['no', 'no', 'sí', 'sí', 'sí', 'no', 'sí', 'no', 'sí', 'sí']}

# Convertimos los datos a un DataFrame de pandas para manejarlos mejor.
df = pd.DataFrame(data)

# Mapeamos los datos categóricos a valores numéricos para que el algoritmo ID3 pueda procesarlos.
df['Clima'] = df['Clima'].map({'soleado': 0, 'nublado': 1, 'lluvioso': 2})
df['Temperatura'] = df['Temperatura'].map({'caliente': 0, 'templado': 1, 'frío': 2})
df['Humedad'] = df['Humedad'].map({'alta': 0, 'normal': 1})
df['Viento'] = df['Viento'].map({'débil': 0, 'fuerte': 1})
df['Paraguas'] = df['Paraguas'].map({'no': 0, 'sí': 1})

# Dividimos los datos en características (X) y la etiqueta objetivo (y).
X = df[['Clima', 'Temperatura', 'Humedad', 'Viento']]  # Características de entrada
y = df['Paraguas']  # Etiqueta de salida (si llevar paraguas o no)

# Dividimos los datos en conjuntos de entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos el clasificador de árbol de decisión usando el algoritmo ID3 (DecisionTreeClassifier en sklearn)
clf = DecisionTreeClassifier(criterion='entropy')  # 'entropy' usa el concepto de entropía para la división

# Entrenamos el clasificador con los datos de entrenamiento
clf.fit(X_train, y_train)

# Evaluamos el rendimiento del clasificador con los datos de prueba
accuracy = clf.score(X_test, y_test)
print(f'Precisión del modelo: {accuracy * 100:.2f}%')

# Visualizamos el árbol de decisión
plt.figure(figsize=(10,8))  # Ajustamos el tamaño de la figura
tree.plot_tree(clf, feature_names=X.columns, class_names=['No', 'Sí'], filled=True)
plt.show()

# Hacemos una predicción para un nuevo caso
# Por ejemplo: Clima = 'lluvioso', Temperatura = 'templado', Humedad = 'alta', Viento = 'débil'
nuevo_dato = pd.DataFrame([[2, 1, 0, 0]], columns=['Clima', 'Temperatura', 'Humedad', 'Viento'])  # Crear DataFrame con nombres de características
prediccion = clf.predict(nuevo_dato)
resultado = 'sí' if prediccion[0] == 1 else 'no'
print(f'¿Debería llevar paraguas? {resultado}')

#Este programa implementa el algoritmo ID3 para construir un árbol de decisión basado en un
#conjunto de datos sobre el clima y las condiciones para decidir si llevar o no un paraguas. El
#aprendizaje inductivo se refiere a extraer patrones generales de ejemplos específicos, y en este caso,
#el árbol de decisión aprende las reglas que determinan si se debe llevar un paraguas, basándose en
#ejemplos previos.

#La entropía mide la incertidumbre de un conjunto de datos, y el árbol de decisión construye su
#estructura eligiendo en cada paso la característica que reduce más la incertidumbre (es decir, la que
#proporciona la mayor ganancia de información).

