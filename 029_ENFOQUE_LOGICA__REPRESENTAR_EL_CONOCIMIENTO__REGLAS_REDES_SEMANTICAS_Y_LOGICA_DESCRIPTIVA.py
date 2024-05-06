# Definimos una función para verificar si una persona es adulta según su edad
def es_adulto(edad):
    return edad >= 18

# Definimos una función para verificar si una persona puede conducir según su edad y su país de residencia
def puede_conducir(edad, pais):
    return (edad >= 16 and pais == "USA") or (edad >= 18 and pais == "UK")

# Definimos una función para aplicar reglas lógicas a una persona
def aplicar_reglas_persona(nombre, edad, pais):
    print(f"Persona: {nombre}")
    print(f"Edad: {edad}")
    print(f"País: {pais}")
    print("Es adulto:", es_adulto(edad))
    print("Puede conducir:", puede_conducir(edad, pais))
    print()

# Creamos instancias de personas con diferentes edades y países
aplicar_reglas_persona("Alice", 25, "USA")
aplicar_reglas_persona("Bob", 16, "USA")
aplicar_reglas_persona("Charlie", 20, "UK")
