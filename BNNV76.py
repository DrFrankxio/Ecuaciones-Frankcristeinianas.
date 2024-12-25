from z3 import *
import time
import os
from itertools import product

def predecir(estructura, entradas, salida_esperada):
    """
    Crea y resuelve un modelo de red neuronal con estructura dinámica.
    
    estructura: Lista de enteros, donde cada número representa el número de neuronas en esa capa.
    entradas: Lista de valores booleanos para las entradas.
    salida_esperada: Lista de valores booleanos para las salidas esperadas.
    """
    # Validar la estructura
    if len(estructura) < 2:
        raise ValueError("La estructura debe tener al menos una capa de entrada y una de salida.")

    if len(entradas) != estructura[0]:
        raise ValueError("El número de entradas no coincide con el tamaño de la capa de entrada.")
    
    if len(salida_esperada) != estructura[-1]:
        raise ValueError("El número de salidas esperadas no coincide con el tamaño de la capa de salida.")

    # Crear listas para las variables Z3
    capas = []
    pesos = []
    sesgos = []
    
    for i, num_neuronas in enumerate(estructura):
        capas.append([Bool(f"h{i+1}_{j+1}") for j in range(num_neuronas)])
        if i > 0:  # Pesos y sesgos empiezan desde la segunda capa
            pesos.append([[Bool(f"w{i}_{k+1}_{j+1}") for k in range(estructura[i-1])] for j in range(num_neuronas)])
            sesgos.append([Bool(f"b{i}_{j+1}") for j in range(num_neuronas)])

    # Reglas de las capas
    reglas = []

    # Reglas para la capa de entrada
    for j, valor in enumerate(entradas):
        reglas.append(capas[0][j] == valor)

    # Reglas para las capas ocultas y de salida
    for i in range(1, len(estructura)):
        for j in range(estructura[i]):
            conexiones = [And(pesos[i-1][j][k], capas[i-1][k]) for k in range(estructura[i-1])]
            regla = capas[i][j] == Or(*conexiones, sesgos[i-1][j])
            reglas.append(regla)

    # Reglas para las salidas esperadas
    for j, valor in enumerate(salida_esperada):
        reglas.append(capas[-1][j] == valor)

    # Resolver el sistema
    solucion = Solver()
    solucion.add(reglas)

    if solucion.check() == sat:
        modelo = solucion.model()
        os.system("cls")  # Limpia la pantalla
        print("Modelo encontrado:")
        for capa in capas:
            print([modelo[neurona] for neurona in capa])
    else:
        print("No hay solución para la configuración dada.")


# Genera todas las combinaciones posibles de valores booleanos para i1, i2, i3, o1
valores = [True, False]
combinaciones = product(valores, repeat=8)  # 8 variables (i1, i2, i3, o1)

for combinacion in combinaciones:
    pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8 = combinacion
    model=[3,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,1]
    predecir(model,[False, False, False], [pos1])
    predecir(model,[False, False, True], [pos2])
    predecir(model,[False, True, False], [pos3])
    predecir(model,[False, True, True], [pos4])
    predecir(model,[True, False, False], [pos5])
    predecir(model,[True, False, True], [pos6])
    predecir(model,[True, True, False], [pos7])
    predecir(model,[True, True, True], [pos8])
