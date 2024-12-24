from z3 import *

i1, i2, i3 = Bools('x1 x2 x3')
w1 = Bool('w1')  # Asegúrate de usar Bool en lugar de Bools
o1, o2, o3 = Bools('o1 o2 o3')

i1x, i2x, i3x = Bools('x1x x2x x3x')
o1x, o2x, o3x = Bools('o1x o2x o3x')



#Entrenamiento:

# Input:
eqI1 = i1 == True
eqI2 = i2 == True

# Pesos:
eqW1 = o1 == And(w1, i1)  # Usar And para conjunción lógica
eqW2 = o2 == And(w1, i2)  # Usar And para conjunción lógica

# Output:
eqO1 = o1 == True
eqO2 = o2 == True



#Predicción:

# Input:
eqI1X = i1x == True
eqI2X = i2x == True

# Pesos:
eqW1X = o1x == And(w1, i1x)  # Usar And para conjunción lógica
eqW2X = o2x == And(w1, i2x)  # Usar And para conjunción lógica



sistema = [
    eqI1,eqI2,
    eqW1,eqW2,
    eqO1,eqO2,
    eqI1X,eqI2X,
    eqW1X,eqW2X,
]



solucion = Solver()
solucion.add(sistema)



if solucion.check() == sat:
    modelo = solucion.model()
    print("Input:")
    print("i1: ", modelo[i1])
    print("i2: ", modelo[i2])
    print("i3: ", modelo[i3])
    print("Output:")
    print("o1: ", modelo[o1])
    print("o2: ", modelo[o2])
    print("o3: ", modelo[o3])
    print("Input (Predicción):")
    print("i1: ", modelo[i1x])
    print("i2: ", modelo[i2x])
    print("i3: ", modelo[i3x])
    print("Output (Predicción):")
    print("o1: ", modelo[o1x])
    print("o2: ", modelo[o2x])
    print("o3: ", modelo[o3x])
else:
    print("No hay solución")
