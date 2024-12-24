from z3 import *

i1, i2, i3 = Bools('x1 x2 x3')
o1, o2, o3 = Bools('o1 o2 o3')
#Input:
eqI1 = i1 == True
eqI2 = i2 == True
eqI3 = i3 == True
#Pesos:
#Output:
eqO1 = o1 == True
eqO2 = o2 == True
eqO3 = o3 == True

sistema = [
	eqI1, eqI2, eqI3,
	eqO1, eqO2, eqO3
]

solucion = Solver()
solucion.add(sistema)

if solucion.check() == sat:
  modelo = solucion.model()
  print("Input:")
  print("i1: ",modelo[i1])
  print("i2: ",modelo[i2])
  print("i3: ",modelo[i3])
  print("Output:")
  print("o1: ",modelo[o1])
  print("o2: ",modelo[o2])
  print("o3: ",modelo[o3])
else:
  print("No hay solución")