from pyprover import ModalFormula, ModalWorld

# Crear mundos modales
world1 = ModalWorld()
world2 = ModalWorld()

# Definir proposiciones en los mundos
world1.set_proposition("p")
world1.set_proposition("q")

world2.set_proposition("p")
world2.set_proposition("r")

# Crear fórmulas modales
formula1 = ModalFormula("necesario p", box=True, propositional='p')
formula2 = ModalFormula("posible q", diamond=True, propositional='q')

# Verificar si las fórmulas son verdaderas en los mundos
print("La fórmula 1 es verdadera en el mundo 1:", world1.evaluate_formula(formula1))
print("La fórmula 2 es verdadera en el mundo 1:", world1.evaluate_formula(formula2))
print("La fórmula 1 es verdadera en el mundo 2:", world2.evaluate_formula(formula1))
print("La fórmula 2 es verdadera en el mundo 2:", world2.evaluate_formula(formula2))
