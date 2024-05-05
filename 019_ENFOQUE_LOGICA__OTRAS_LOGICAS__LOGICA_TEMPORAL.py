from pytemporallogic import Atom, TemporalLogic

# Crear proposiciones atómicas
p = Atom("p")
q = Atom("q")

# Definir fórmulas de lógica temporal
formula1 = TemporalLogic.G(p)  # Siempre en el futuro p será verdadero
formula2 = TemporalLogic.F(TemporalLogic.G(p))  # En algún momento en el futuro, siempre será verdadero que en el futuro p será verdadero
formula3 = TemporalLogic.X(p)  # En el próximo instante de tiempo p será verdadero
formula4 = TemporalLogic.U(p, q)  # En algún momento en el futuro, p será verdadero hasta que q sea verdadero

# Evaluar las fórmulas en un modelo de tiempo específico
tiempo = 0
print(f"En el tiempo {tiempo}:")
print("La fórmula 1 es verdadera:", formula1.evaluate(tiempo))
print("La fórmula 2 es verdadera:", formula2.evaluate(tiempo))
print("La fórmula 3 es verdadera:", formula3.evaluate(tiempo))
print("La fórmula 4 es verdadera:", formula4.evaluate(tiempo))
