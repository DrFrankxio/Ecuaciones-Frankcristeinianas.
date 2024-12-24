from z3 import *

i1, i2, i3 = Bools('i1 i2 i3')
w1, b1, w2, b2, w3, b3, w4, b4 = Bools('w1 b1 w2 b2 w3 b3 w4 b4')
o1, o2, o3 = Bools('o1 o2 o3')

i1x, i2x, i3x = Bools('x1x x2x x3x')
o1x, o2x, o3x = Bools('o1x o2x o3x')



#Entrenamiento:

# Input:
eqI1 = i1 == True
eqI2 = i2 == False

# Pesos:
eqW1 = o1 == Or(And(w1, i1), And(w2, i2), b1)

# Output:
eqO1 = o1 == False

#Predicción:

# Input:
eqI1X = i1x == True
eqI2X = i2x == False

# Pesos:
eqW1X = o1x == Or(And(w1, i1x), And(w2, i2x), b1)



sistema = [
    eqI1,
    eqI2,
    eqW1,
    eqO1,
    eqI1X,
    eqI2X,
    eqW1X,
]



solucion = Solver()
solucion.add(sistema)



if solucion.check() == sat:
    modelo = solucion.model()
    print("")
    print("Input (Entrenamiento):")
    print("i1: ", modelo[i1])
    print("Input (Entrenamiento):")
    print("i2: ", modelo[i2])
    print("Output (Entrenamiento):")
    print("o1: ", modelo[o1])
    print("")
    print("Input (Predicción):")
    print("i1: ", modelo[i1x])
    print("Input (Predicción):")
    print("i2: ", modelo[i2x])
    print("Output (Predicción):")
    print("o1: ", modelo[o1x])
else:
    print("No hay solución")
