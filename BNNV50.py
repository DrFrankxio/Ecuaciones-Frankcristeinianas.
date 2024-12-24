from z3 import *
import time

i1, i2, i3 = Bools('i1 i2 i3')
b1, w1, w2, w3 = Bools('b1 w1 w2 w3')
o1, o2, o3 = Bools('o1 o2 o3')

i1x, i2x, i3x = Bools('i1x i2x i3x')
o1x, o2x, o3x = Bools('o1x o2x o3x')



#Entrenamiento:

def predecir(pi1,pi2,pi3,po1):
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
	eqI3X = i3x == pi2

	# Pesos:
	eqW1X = o1x == Or(And(w1, i1x), And(w2, i2x), And(w3, i3x), b1)

	sistema = [
	    eqI1,
	    eqI2,
	    eqI3,

	    eqW1,

	    eqO1,

	    

	    eqI1X,
	    eqI2X,
	    eqI3X,

	    eqW1X,
	]



	solucion = Solver()
	solucion.add(sistema)



	if solucion.check() == sat:
	    modelo = solucion.model()
	    print("")
	    print("")
	    print("")
	    print("Input (Entrenamiento):")
	    print("i1: ", modelo[i1])
	    print("Input (Entrenamiento):")
	    print("i2: ", modelo[i2])
	    print("Input (Entrenamiento):")
	    print("i3: ", modelo[i3])
	    print("Output (Entrenamiento):")
	    print("o1: ", modelo[o1])
	    print("")
	    print("Input (Predicción):")
	    print("i1: ", modelo[i1x])
	    print("Input (Predicción):")
	    print("i2: ", modelo[i2x])
	    print("Input (Predicción):")
	    print("i3: ", modelo[i3x])
	    print("Output (Predicción):")
	    print("o1: ", modelo[o1x])
	else:
	    print("No hay solución")

def bucle1():
	time.sleep(10)
	os.system("cls")
	predecir(
		True,True,True,
		True,
	)
	predecir(
		True,True,False,
		True,
	)
	predecir(
		True,False,True,
		True,
	)
	predecir(
		True,False,False,
		True,
	)

	predecir(
		False,True,True,
		True,
	)
	predecir(
		False,True,False,
		True,
	)
	predecir(
		False,False,True,
		True,
	)
	predecir(
		False,False,False,
		True,
	)



	predecir(
		True,True,True,
		False,
	)
	predecir(
		True,True,False,
		False,
	)
	predecir(
		True,False,True,
		False,
	)
	predecir(
		True,False,False,
		False,
	)

	predecir(
		False,True,True,
		False,
	)
	predecir(
		False,True,False,
		False,
	)
	predecir(
		False,False,True,
		False,
	)
	predecir(
		False,False,False,
		False,
	)
	bucle1()
bucle1()
