class Frame:
    def __init__(self, name):
        self.name = name
        self.slots = {}

    def add_slot(self, slot_name, value):
        self.slots[slot_name] = value

    def get_slot(self, slot_name):
        return self.slots.get(slot_name, None)

# Definimos una clase de marco para representar una persona
persona_frame = Frame("Persona")
persona_frame.add_slot("nombre", "Alice")
persona_frame.add_slot("edad", 30)
persona_frame.add_slot("profesion", "Ingeniera")

# Definimos otra clase de marco para representar una empresa
empresa_frame = Frame("Empresa")
empresa_frame.add_slot("nombre", "Empresa XYZ")
empresa_frame.add_slot("ubicacion", "Ciudad A")
empresa_frame.add_slot("numero_empleados", 100)

# Imprimimos la información de los marcos
print("Información del marco de persona:")
print("Nombre:", persona_frame.get_slot("nombre"))
print("Edad:", persona_frame.get_slot("edad"))
print("Profesión:", persona_frame.get_slot("profesion"))

print("\nInformación del marco de empresa:")
print("Nombre:", empresa_frame.get_slot("nombre"))
print("Ubicación:", empresa_frame.get_slot("ubicacion"))
print("Número de empleados:", empresa_frame.get_slot("numero_empleados"))
