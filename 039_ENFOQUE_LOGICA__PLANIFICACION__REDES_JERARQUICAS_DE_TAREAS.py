#Practica: 039_ENFOQUE_LOGICA__PLANIFICACION__REDES_JERARQUICAS_DE_TAREAS
#Alumno: IVAN_DOMINGUEZ
#Registro: 21310234
#Grupo: 7F1

# Definimos un planificador basado en redes jerárquicas de tareas (HTN) para organizar una cena.

# Función para descomponer la tarea de preparar la cena
def preparar_cena():
    # Definimos las subtareas necesarias para preparar una cena
    print("Plan para preparar la cena:")
    comprar_ingredientes()
    cocinar()
    poner_la_mesa()
    servir_comida()
    print("Cena lista!")

# Función para descomponer la tarea de comprar ingredientes
def comprar_ingredientes():
    # Subtareas específicas para comprar ingredientes
    print("- Ir al supermercado")
    print("- Comprar verduras, carne, y pan")
    print("- Regresar a casa")

# Función para descomponer la tarea de cocinar
def cocinar():
    # Subtareas específicas para cocinar
    print("- Lavar las verduras")
    print("- Cortar las verduras y carne")
    print("- Cocinar los ingredientes")
    print("- Preparar una ensalada")

# Función para descomponer la tarea de poner la mesa
def poner_la_mesa():
    # Subtareas específicas para poner la mesa
    print("- Colocar platos, vasos y cubiertos")
    print("- Poner servilletas")
    print("- Acomodar las sillas")

# Función para servir la comida
def servir_comida():
    # Subtareas específicas para servir la comida
    print("- Servir la comida en los platos")
    print("- Llamar a los invitados")

# Función principal que ejecuta el plan
if __name__ == "__main__":
    preparar_cena()  # Ejecuta la tarea de alto nivel y la descompone en pasos detallados

#Este programa simulará un planificador simple basado en una red jerárquica de tareas para organizar
#una cena. A partir de una tarea de alto nivel, como "preparar la cena", el planificador descompondrá
#la tarea en subtareas más simples hasta que todas las tareas puedan ejecutarse secuencialmente.

#El programa simula una red jerárquica de tareas (HTN) para planificar la preparación de una cena.
#Las HTN son utilizadas en sistemas de inteligencia artificial para descomponer tareas complejas en
#subtareas más simples, hasta que cada una pueda ser ejecutada de manera secuencial o concurrente.
#Este enfoque es útil en la planificación de actividades de la vida cotidiana, como el ejemplo de la
#cena, y en aplicaciones más complejas, como la robótica, juegos y sistemas de planificación de
#proyectos.
