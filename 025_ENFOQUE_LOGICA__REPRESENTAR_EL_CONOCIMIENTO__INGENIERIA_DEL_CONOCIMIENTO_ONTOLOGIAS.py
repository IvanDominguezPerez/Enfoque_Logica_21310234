from rdflib import Graph, Namespace, URIRef, Literal

# Crear un grafo RDF
g = Graph()

# Definir namespaces
ex = Namespace("http://example.org/")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")

# Definir recursos y propiedades
persona = ex.Persona
nombre = ex.nombre
edad = ex.edad
amigo_de = ex.amigo_de

# Agregar tripletas al grafo
g.add((persona, rdf.type, rdfs.Class))  # persona es una clase
g.add((nombre, rdf.type, rdf.Property))  # nombre es una propiedad
g.add((edad, rdf.type, rdf.Property))  # edad es una propiedad
g.add((amigo_de, rdf.type, rdf.Property))  # amigo_de es una propiedad

# Agregar instancias y relaciones
g.add((ex.Alice, rdf.type, persona))  # Alice es una instancia de persona
g.add((ex.Alice, nombre, Literal("Alice")))  # Alice tiene el nombre "Alice"
g.add((ex.Alice, edad, Literal(30)))  # Alice tiene 30 años
g.add((ex.Bob, rdf.type, persona))  # Bob es una instancia de persona
g.add((ex.Bob, nombre, Literal("Bob")))  # Bob tiene el nombre "Bob"
g.add((ex.Bob, edad, Literal(35)))  # Bob tiene 35 años
g.add((ex.Alice, amigo_de, ex.Bob))  # Alice es amigo de Bob

# Serializar y visualizar el grafo RDF
print("Grafo RDF:")
print(g.serialize(format='turtle').decode("utf-8"))
