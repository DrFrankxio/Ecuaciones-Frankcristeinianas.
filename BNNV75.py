from z3 import *
import time
import os
from itertools import product

# Entrenamiento:
def predecir(pi1, pi2, pi3, po1):
    # Entradas para entrenamiento
    i1, i2, i3 = Bools('i1 i2 i3')

    # Pesos y sesgos para la capa de entrada (L1)
    w11, w12, w13, b1l1 = Bools('w11 w12 w13 b1l1')
    w21, w22, w23, b2l1 = Bools('w21 w22 w23 b2l1')

    # Salidas de la capa de entrada (L1)
    h1l1, h2l1 = Bools('h1l1 h2l1')

    # Pesos y sesgos para la capa oculta (L2)
    w11l2, w12l2, b1l2 = Bools('w11l2 w12l2 b1l2')
    w21l2, w22l2, b2l2 = Bools('w21l2 w22l2 b2l2')

    # Salidas de la capa oculta (L2)
    h1l2, h2l2 = Bools('h1l2 h2l2')

    # Pesos y sesgos para la capa oculta (L3)
    w11l3, w12l3, b1l3 = Bools('w11l3 w12l3 b1l3')
    w21l3, w22l3, b2l3 = Bools('w21l3 w22l3 b2l3')

    # Salidas de la capa oculta (L3)
    h1l3, h2l3 = Bools('h1l3 h2l3')

    # Pesos y sesgos para la capa oculta (L4)
    w11l4, w12l4, b1l4 = Bools('w11l4 w12l4 b1l4')
    w21l4, w22l4, b2l4 = Bools('w21l4 w22l4 b2l4')

    # Salidas de la capa oculta (L4)
    h1l4, h2l4 = Bools('h1l4 h2l4')

    # Pesos y sesgo para la capa de salida
    w31, w32, b3 = Bools('w31 w32 b3')

    # Salida final
    o1 = Bool('o1')

    # Definición de las entradas
    eqI1 = i1 == pi1
    eqI2 = i2 == pi2
    eqI3 = i3 == pi3

    # Reglas para los perceptrones en la capa de entrada (entrenamiento)
    eqH1L1 = h1l1 == Or(And(w11, i1), And(w12, i2), And(w13, i3), b1l1)  # Perceptrón 1 capa 1.
    eqH2L1 = h2l1 == Or(And(w21, i1), And(w22, i2), And(w23, i3), b2l1)  # Perceptrón 2 capa 1.

    # Reglas para los perceptrones en la capa oculta (L2)
    eqH1L2 = h1l2 == Or(And(w11l2, h1l1), And(w12l2, h2l1), b1l2)  # Perceptrón 1 capa 2.
    eqH2L2 = h2l2 == Or(And(w21l2, h1l1), And(w22l2, h2l1), b2l2)  # Perceptrón 2 capa 2.

    # Reglas para los perceptrones en la capa oculta (L3)
    eqH1L3 = h1l3 == Or(And(w11l3, h1l2), And(w12l3, h2l2), b1l3)  # Perceptrón 1 capa 3.
    eqH2L3 = h2l3 == Or(And(w21l3, h1l2), And(w22l3, h2l2), b2l3)  # Perceptrón 2 capa 3.

    # Reglas para los perceptrones en la capa oculta (L4)
    eqH1L4 = h1l4 == Or(And(w11l4, h1l3), And(w12l4, h2l3), b1l4)  # Perceptrón 1 capa 4.
    eqH2L4 = h2l4 == Or(And(w21l4, h1l3), And(w22l4, h2l3), b2l4)  # Perceptrón 2 capa 4.

    # Regla para el perceptrón en la capa de salida (entrenamiento)
    eqO1 = o1 == Or(And(w31, h1l4), And(w32, h2l4), b3)

    # Output deseado
    eqO1Final = o1 == po1

    # Definición de las entradas para simulación (i1x, i2x, i3x)
    i1x, i2x, i3x = Bools('i1x i2x i3x')

    eqI1X = i1x == pi1
    eqI2X = i2x == pi2
    eqI3X = i3x == pi3

    # Reglas para los perceptrones en la capa de entrada (simulación)
    eqH1L1X = h1l1 == Or(And(w11, i1x), And(w12, i2x), And(w13, i3x), b1l1)  # Perceptrón 1 capa 1.
    eqH2L1X = h2l1 == Or(And(w21, i1x), And(w22, i2x), And(w23, i3x), b2l1)  # Perceptrón 2 capa 1.

    # Reglas para los perceptrones en la capa oculta (L2)
    eqH1L2X = h1l2 == Or(And(w11l2, h1l1), And(w12l2, h2l1), b1l2)  # Perceptrón 1 capa 2.
    eqH2L2X = h2l2 == Or(And(w21l2, h1l1), And(w22l2, h2l1), b2l2)  # Perceptrón 2 capa 2.

    # Reglas para los perceptrones en la capa oculta (L3)
    eqH1L3X = h1l3 == Or(And(w11l3, h1l2), And(w12l3, h2l2), b1l3)  # Perceptrón 1 capa 3.
    eqH2L3X = h2l3 == Or(And(w21l3, h1l2), And(w22l3, h2l2), b2l3)  # Perceptrón 2 capa 3.

    # Reglas para los perceptrones en la capa oculta (L4)
    eqH1L4X = h1l4 == Or(And(w11l4, h1l3), And(w12l4, h2l3), b1l4)  # Perceptrón 1 capa 4.
    eqH2L4X = h2l4 == Or(And(w21l4, h1l3), And(w22l4, h2l3), b2l4)  # Perceptrón 2 capa 4.

    # Regla para el perceptrón en la capa de salida (simulación)
    eqO1X = o1 == Or(And(w31, h1l4), And(w32, h2l4), b3)

    # Sistema completo de simulación
    sistema = [
        eqI1, eqI2, eqI3, eqH1L1, eqH2L1, eqH1L2, eqH2L2, eqH1L3, eqH2L3, eqH1L4, eqH2L4, eqO1, eqO1Final,
        eqI1X, eqI2X, eqI3X, eqH1L1X, eqH2L1X, eqH1L2X, eqH2L2X, eqH1L3X, eqH2L3X, eqH1L4X, eqH2L4X, eqO1X
    ]

    # Resolver el sistema
    solucion = Solver()
    solucion.add(sistema)

    if solucion.check() == sat:
        modelo = solucion.model()
        print("Entrenamiento: ","{} {} {} ".format(modelo[i1], modelo[i2], modelo[i3]),"=>",modelo[o1],". Simulación: ","{} {} {}".format(modelo[i1x], modelo[i2x], modelo[i3x]),"=>",modelo[o1],".")
    else:
        print("No hay solución")

# Bucle principal
def bucle1():
    time.sleep(0.5)  # Espera medio segundo
    os.system("cls")  # Limpia la pantalla

    # Genera todas las combinaciones posibles de valores booleanos para i1, i2, i3, o1
    valores = [True, False]
    combinaciones = product(valores, repeat=8)  # 8 variables (i1, i2, i3, o1)

    for combinacion in combinaciones:
        pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8 = combinacion
        predecir(False, False, False, pos1)
        predecir(False, False, True, pos2)
        predecir(False, True, False, pos3)
        predecir(False, True, True, pos4)
        predecir(True, False, False, pos5)
        predecir(True, False, True, pos6)
        predecir(True, True, False, pos7)
        predecir(True, True, True, pos8)

# Ejecuta el bucle
bucle1()
