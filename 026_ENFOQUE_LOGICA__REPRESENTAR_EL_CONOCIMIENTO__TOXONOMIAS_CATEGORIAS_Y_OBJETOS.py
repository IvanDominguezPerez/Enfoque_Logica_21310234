# Definir una taxonomía de categorías y objetos utilizando un diccionario
taxonomia = {
    "Animales": ["Perro", "Gato", "León", "Elefante"],
    "Frutas": ["Manzana", "Plátano", "Naranja", "Uva"],
    "Instrumentos": ["Guitarra", "Piano", "Violín", "Batería"]
}

# Función para imprimir la taxonomía
def imprimir_taxonomia(taxonomia):
    for categoria, objetos in taxonomia.items():
        print(f"{categoria}:")
        for objeto in objetos:
            print(f" - {objeto}")
        print()

# Imprimir la taxonomía
print("Taxonomía:")
imprimir_taxonomia(taxonomia)
