class BaseConocimiento:
    def __init__(self):
        self.hechos = set()

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def eliminar_hecho(self, hecho):
        self.hechos.remove(hecho)

    def consultar_hecho(self, hecho):
        return hecho in self.hechos

# Creamos una instancia de la base de conocimiento
base_conocimiento = BaseConocimiento()

# Agregamos algunos hechos iniciales
base_conocimiento.agregar_hecho("pájaros vuelan")
base_conocimiento.agregar_hecho("pájaros tienen alas")
base_conocimiento.agregar_hecho("pájaros tienen plumas")

# Consultamos algunos hechos
print("¿Los pájaros vuelan?", base_conocimiento.consultar_hecho("pájaros vuelan"))
print("¿Los peces vuelan?", base_conocimiento.consultar_hecho("peces vuelan"))

# Eliminamos un hecho
base_conocimiento.eliminar_hecho("pájaros tienen alas")

# Consultamos de nuevo el hecho eliminado
print("¿Los pájaros tienen alas?", base_conocimiento.consultar_hecho("pájaros tienen alas"))
