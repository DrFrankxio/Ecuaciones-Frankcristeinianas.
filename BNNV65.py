from z3 import *
import time
from itertools import product
import os  # Necesario para os.system("cls") en tu bucle principal

# Entrenamiento:
def predecir(pi1, pi2, pi3, po1):
    # Entradas
    i1, i2, i3 = Bools('i1 i2 i3')

    # Pesos y sesgos para la capa oculta
    w11, w12, w13, b1 = Bools('w11 w12 w13 b1')
    w21, w22, w23, b2 = Bools('w21 w22 w23 b2')

    # Capa oculta
    h1, h2 = Bools('h1 h2')

    # Pesos y sesgo para la capa de salida
    w31, w32, b3 = Bools('w31 w32 b3')

    # Salida final
    o1 = Bool('o1')

    # Entradas de simulación
    i1x, i2x, i3x = Bools('i1x i2x i3x')

    # Salidas de simulación
    o1x = Bool('o1x')

    # Definición de las entradas
    eqI1 = i1 == pi1
    eqI2 = i2 == pi2
    eqI3 = i3 == pi3

    # Reglas para los perceptrones en la capa oculta (entrenamiento)
    eqH1 = h1 == Or(And(w11, i1), And(w12, i2), And(w13, i3), b1)  # Perceptrón 1
    eqH2 = h2 == Or(And(w21, i1), And(w22, i2), And(w23, i3), b2)  # Perceptrón 2

    # Regla para el perceptrón en la capa de salida (entrenamiento)
    eqO1 = o1 == Or(And(w31, h1), And(w32, h2), b3)

    # Output deseado
    eqO1Final = o1 == po1

    # Predicción

    # Definición de las entradas de simulación
    eqI1X = i1x == pi1
    eqI2X = i2x == pi2
    eqI3X = i3x == pi3

    # Reglas para los perceptrones en la capa oculta (simulación)
    eqH1X = h1 == Or(And(w11, i1x), And(w12, i2x), And(w13, i3x), b1)
    eqH2X = h2 == Or(And(w21, i1x), And(w22, i2x), And(w23, i3x), b2)

    # Regla para el perceptrón en la capa de salida (simulación)
    eqO1X = o1x == Or(And(w31, h1), And(w32, h2), b3)

    # Sistema completo
    sistema = [
        eqI1, eqI2, eqI3, eqH1, eqH2, eqO1, eqO1Final,  # Entrenamiento
        eqI1X, eqI2X, eqI3X, eqH1X, eqH2X, eqO1X       # Simulación
    ]

    # Resolver el sistema
    solucion = Solver()
    solucion.add(sistema)

    if solucion.check() == sat:
        modelo = solucion.model()
        print(f"Entrenamiento: {modelo[i1]} {modelo[i2]} {modelo[i3]} => {modelo[o1]}. "
              f"Simulación: {modelo[i1x]} {modelo[i2x]} {modelo[i3x]} => {modelo[o1x]}.")
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
