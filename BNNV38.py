from z3 import *

i1, i2, i3 = Bools('x1 x2 x3')
w1, b1 = Bools('w1 b1')
o1, o2, o3 = Bools('o1 o2 o3')

i1x, i2x, i3x = Bools('x1x x2x x3x')
o1x, o2x, o3x = Bools('o1x o2x o3x')



#Entrenamiento:

# Input:
eqI1 = i1 == False

# Pesos:
eqW1 = o1 == Or(And(w1, i1), b1)

# Output:
eqO1 = o1 == False



#Predicción:

# Input:
eqI1X = i1x == False

# Pesos:
eqW1X = o1x == Or(And(w1, i1x), b1)



sistema = [
    eqI1,
    eqW1,
    eqO1,
    eqI1X,
    eqW1X,
]



solucion = Solver()
solucion.add(sistema)



if solucion.check() == sat:
    modelo = solucion.model()
    print("Input:")
    print("i1: ", modelo[i1])
    print("Output:")
    print("o1: ", modelo[o1])
    print("Input (Predicción):")
    print("i1: ", modelo[i1x])
    print("Output (Predicción):")
    print("o1: ", modelo[o1x])
else:
    print("No hay solución")
