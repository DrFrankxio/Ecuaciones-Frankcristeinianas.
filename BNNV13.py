from z3 import *

i1i1, i2i1, i3i1, i1i2, i2i2, i3i2, p1p1, p2p1, p3p1, p1p2, p2p2, p3p2, o1, o2, o3 = Bools('i1i1 i2i1 i3i1 i1i2 i2i2 i3i2 p1p1 p2p1 p3p1 p1p2 p2p2 p3p2 o1 o2 o3')
#Input:
eqI1I1 = i1i1 == True
eqI2I1 = i2i1 == True
eqI3I1 = i3i1 == True
eqI1I2 = i1i2 == True
eqI2I2 = i2i2 == True
eqI3I2 = i3i2 == True
#Pesos:
eqP1 = o1 == p1p1&i1i1|p1p2&i1i2
eqP2 = o2 == p2p1&i2i1|p2p2&i1i2
eqP3 = o3 == p3p1&i3i1|p3p2&i1i2
#Output:
eqO1 = o1 == True
eqO2 = o2 == True
eqO3 = o3 == True

sistema = [
	eqI1I1, eqI2I1, eqI3I1,
	eqI1I2, eqI2I2, eqI3I2,

	eqP1, eqP2, eqP3,

	eqO1, eqO2, eqO3
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
  print("p1p1: ",modelo[p1p1])
  print("p2p1: ",modelo[p2p1])
  print("p3p1: ",modelo[p3p1])
  print("p1p2: ",modelo[p1p2])
  print("p2p2: ",modelo[p2p2])
  print("p3p2: ",modelo[p3p2])
  print("Output:")
  print("o1: ",modelo[o1])
  print("o2: ",modelo[o2])
  print("o3: ",modelo[o3])
else:
  print("No hay solución")