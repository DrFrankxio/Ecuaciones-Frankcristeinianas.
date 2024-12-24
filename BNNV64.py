from z3 import *
import time
from itertools import product



#Entrenamiento:

def predecir(pi1,pi2,pi3,po1,):

	i1, i2, i3 = Bools('i1 i2 i3')
	b1, w1, w2, w3 = Bools('b1 w1 w2 w3')
	o1, o2, o3 = Bools('o1 o2 o3')

	i1x, i2x, i3x = Bools('i1x i2x i3x')
	o1x, o2x, o3x = Bools('o1x o2x o3x')
	
	# Input:
	eqI1 = i1 == pi1
	eqI2 = i2 == pi2
	eqI3 = i3 == pi3

	# Pesos:
	eqW1 = o1 == Or(And(w1, i1), And(w2, i2), And(w3, i3), b1)

	# Output:
	eqO1 = o1 == po1

	#Predicción:

	# Input:
	eqI1X = i1x == pi1
	eqI2X = i2x == pi2
	eqI3X = i3x == pi3

	# Pesos:
	eqW1X = o1x == Or(And(w1, i1x), And(w2, i2x), And(w3, i3x), b1)

	sistema = [
	    eqI1,eqI2,eqI3,
	    eqW1,
	    eqO1,

	    eqI1X,eqI2X,eqI3X,
	    eqW1X,
	]

	solucion = Solver()
	solucion.add(sistema)

	if solucion.check() == sat:
	    modelo = solucion.model()
	    print("Entrenamiento: ","{} {} {} ".format(modelo[i1], modelo[i2], modelo[i3]),"=>",modelo[o1],". Simulación: ","{} {} {}".format(modelo[i1x], modelo[i2x], modelo[i3x]),"=>",modelo[o1],".")
	else:
	    print("No hay solución")

# Bucle principal
def bucle1():
	time.sleep(0.5)   # Espera medio segundo
	os.system("cls")  # Limpia la pantalla
	# Genera todas las combinaciones posibles de valores booleanos para i1, i2, i3, o1
	valores = [True, False]
	combinaciones = product(valores, repeat=8)  # 4 variables (i1, i2, i3, o1)
	for combinacion in combinaciones:
		pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, = combinacion
		predecir(False, False, False, pos1)
		predecir(False, False, True, pos2)
		predecir(False, True, False, pos3)
		predecir(False, True, True, pos4)
		predecir(True, False, False, pos5)
		predecir(True, False, True, pos6)
		predecir(True, True, False, pos7)
		predecir(True, True, True, pos8)
		
	bucle1()

# Ejecuta el bucle
bucle1()