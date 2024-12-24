from z3 import *

i1i1, i2i1, i3i1, i1i2, i2i2, i3i2 = Bools('i1i1 i2i1 i3i1 i1i2 i2i2 i3i2')
p1, p2 = Bools('p1 p2')
o1, o2, o3 = Bools('o1 o2 o3')
i1i1x, i2i1x, i3i1x, i1i2x, i2i2x, i3i2x = Bools('i1i1x i2i1x i3i1x i1i2x i2i2x i3i2x')
o1x, o2x, o3x = Bools('o1x o2x o3x')

#Input:
eqI1I1 = i1i1 == True
eqI2I1 = i2i1 == True
eqI3I1 = i3i1 == True
eqI1I2 = i1i2 == True
eqI2I2 = i2i2 == True
eqI3I2 = i3i2 == True
#Pesos:
eqP1 = o1 == p1&i1i1|p2&i1i2
eqP2 = o2 == p1&i2i1|p2&i1i2
eqP3 = o3 == p1&i3i1|p2&i1i2
#Output:
eqO1 = o1 == True
eqO2 = o2 == True
eqO3 = o3 == True

#Input (Predicción):
eqI1I1X = i1i1x == True
eqI2I1X = i2i1x == True
eqI3I1X = i3i1x == True
eqI1I2X = i1i2x == True
eqI2I2X = i2i2x == True
eqI3I2X = i3i2x == True
#Pesos (Predicción):
eqP1X = o1x == p1&i1i1x|p2&i1i2x
eqP2X = o2x == p1&i2i1x|p2&i1i2x
eqP3X = o3x == p1&i3i1x|p2&i1i2x

sistema = [
	eqI1I1, eqI2I1, eqI3I1,
	eqI1I2, eqI2I2, eqI3I2,

	eqP1, eqP2, eqP3,

	eqO1, eqO2, eqO3,

	eqI1I1X, eqI2I1X, eqI3I1X,
	eqI1I2X, eqI2I2X, eqI3I2X,

	eqP1X, eqP2X, eqP3X,
]

solucion = Solver()
solucion.add(sistema)

if solucion.check() == sat:
  modelo = solucion.model()
  print("Inputs:")
  print("i1i1: ",modelo[i1i1])
  print("i2i1: ",modelo[i2i1])
  print("i3i1: ",modelo[i3i1])
  print("i1i2: ",modelo[i1i2])
  print("i2i2: ",modelo[i2i2])
  print("i3i2: ",modelo[i3i2])
  print("Pesos:")
  print("p1: ",modelo[p1])
  print("p2: ",modelo[p2])
  print("Output:")
  print("o1: ",modelo[o1])
  print("o2: ",modelo[o2])
  print("o3: ",modelo[o3])
  print("Inputs (Predicción):")
  print("i1i1x: ",modelo[i1i1x])
  print("i2i1x: ",modelo[i2i1x])
  print("i3i1x: ",modelo[i3i1x])
  print("i1i2x: ",modelo[i1i2x])
  print("i2i2x: ",modelo[i2i2x])
  print("i3i2x: ",modelo[i3i2x])
  print("Output (Predicción):")
  print("o1x: ",modelo[o1x])
  print("o2x: ",modelo[o2x])
  print("o3x: ",modelo[o3x])
else:
  print("No hay solución")