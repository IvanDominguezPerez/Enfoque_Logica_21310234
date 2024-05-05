import numpy as np
import skfuzzy as fuzz

# Definir los universos de discurso para las variables de entrada y salida
x_calidad = np.arange(0, 11, 1)
x_servicio = np.arange(0, 11, 1)
x_propina = np.arange(0, 26, 1)

# Generar funciones de membresía difusas para las variables de entrada y salida
calidad_baja = fuzz.trimf(x_calidad, [0, 0, 5])
calidad_media = fuzz.trimf(x_calidad, [0, 5, 10])
calidad_alta = fuzz.trimf(x_calidad, [5, 10, 10])

servicio_bajo = fuzz.trimf(x_servicio, [0, 0, 5])
servicio_medio = fuzz.trimf(x_servicio, [0, 5, 10])
servicio_alto = fuzz.trimf(x_servicio, [5, 10, 10])

propina_baja = fuzz.trimf(x_propina, [0, 0, 13])
propina_media = fuzz.trimf(x_propina, [0, 13, 25])
propina_alta = fuzz.trimf(x_propina, [13, 25, 25])

# Visualizar las funciones de membresía
import matplotlib.pyplot as plt

plt.figure()

plt.plot(x_calidad, calidad_baja, 'b', linewidth=1.5, label='Baja')
plt.plot(x_calidad, calidad_media, 'g', linewidth=1.5, label='Media')
plt.plot(x_calidad, calidad_alta, 'r', linewidth=1.5, label='Alta')
plt.title('Calidad del Comida')
plt.xlabel('Nivel de Calidad')
plt.ylabel('Membresía')
plt.legend()

plt.figure()

plt.plot(x_servicio, servicio_bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(x_servicio, servicio_medio, 'g', linewidth=1.5, label='Medio')
plt.plot(x_servicio, servicio_alto, 'r', linewidth=1.5, label='Alto')
plt.title('Calidad del Servicio')
plt.xlabel('Nivel de Servicio')
plt.ylabel('Membresía')
plt.legend()

plt.figure()

plt.plot(x_propina, propina_baja, 'b', linewidth=1.5, label='Baja')
plt.plot(x_propina, propina_media, 'g', linewidth=1.5, label='Media')
plt.plot(x_propina, propina_alta, 'r', linewidth=1.5, label='Alta')
plt.title('Cantidad de Propina')
plt.xlabel('Cantidad de Propina')
plt.ylabel('Membresía')
plt.legend()

plt.show()

# Definir las reglas difusas
regla1 = fuzz.relation_min(calidad_baja, servicio_bajo)
regla2 = fuzz.relation_min(calidad_media, servicio_medio)
regla3 = fuzz.relation_min(calidad_alta, servicio_alto)

# Combinar las reglas difusas para obtener la salida difusa
salida = np.fmax(regla1, np.fmax(regla2, regla3))

# Calcular el resultado final de la inferencia difusa
resultado = fuzz.defuzz(x_propina, salida, 'centroid')

# Visualizar la salida difusa
plt.plot(x_propina, salida, 'b', linewidth=0.5, label='Inferencia')
plt.fill_between(x_propina, salida, alpha=0.1)
plt.title('Salida de Inferencia Difusa')
plt.xlabel('Cantidad de Propina')
plt.ylabel('Membresía')
plt.legend()
plt.show()

print("Cantidad de propina recomendada:", resultado)
