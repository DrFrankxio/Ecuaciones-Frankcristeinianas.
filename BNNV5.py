from z3 import *

x1, x2, x3 = Bools('x1 x2 x3')
ecuacion1 = x1 == True
ecuacion2 = x2 == True
ecuacion3 = x3 == True

sistema = [ecuacion1, ecuacion2, ecuacion3]

solucion = Solver()
solucion.add(sistema)

if solucion.check() == sat:
  modelo = solucion.model()
  print("x1: ",modelo[x1])
  print("x2: ",modelo[x2])
  print("x3: ",modelo[x3])
else:
  print("No hay solución")