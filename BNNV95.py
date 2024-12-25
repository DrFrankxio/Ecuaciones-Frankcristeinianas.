from z3 import *
import time
import os
from itertools import product
import tkinter as tk

def dibujar_red_neuronal(model):
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Red Neuronal")

    # Definir el tamaño de la ventana
    ancho = 800
    alto = 600
    root.geometry(f"{ancho}x{alto}")

    # Configurar el lienzo para dibujar
    lienzo = tk.Canvas(root, width=ancho, height=alto, bg="white")
    lienzo.pack()

    # Configuración de colores
    color_neurona = "gray"
    color_conexion = "black"

    # Definir el espacio entre capas y el radio de las neuronas
    espacio_entre_capas = 80
    radio_neurona = 8

    # Calcular el total de capas
    capas = len(model)

    # Calcular el rango de posiciones Y para distribuir las neuronas
    max_altura = alto - 100  # Un margen para que no se superpongan en la parte superior
    margen_superior = 50  # Espacio superior para evitar que se dibuje demasiado arriba

    # Calcular las posiciones de las neuronas
    posiciones = []
    for i in range(capas):  # Recorremos todas las capas
        # Posición X para la capa (se distribuye horizontalmente)
        x = (i + 1) * espacio_entre_capas

        # Calcular la distancia entre las neuronas para que se distribuyan adecuadamente
        num_neuronas = model[i]
        y_offset = (max_altura - margen_superior) / (num_neuronas + 1)  # Espacio extra para evitar solapamientos

        # Almacenar las posiciones de las neuronas para la capa
        capa_posiciones = []
        for j in range(num_neuronas):
            # Posición Y para la neurona
            y = margen_superior + (j + 1) * y_offset  # Evitar que se solapen en el eje Y
            capa_posiciones.append((x, y))
            
            # Dibujar un círculo para representar la neurona
            neurona = lienzo.create_oval(x - radio_neurona, y - radio_neurona,
                                         x + radio_neurona, y + radio_neurona,
                                         fill=color_neurona, outline="black", width=4, tags=f"neurona_{i}_{j}")
            # Añadir texto con el número de neurona (opcional)
            # lienzo.create_text(x, y, text=f"n{j+1}", font=("Arial", 8), tags=f"neurona_{i}_{j}")

        # Guardar las posiciones de la capa
        posiciones.append(capa_posiciones)

    # Dibujar las conexiones entre neuronas
    for i in range(capas - 1):
        for j, (x1, y1) in enumerate(posiciones[i]):
            for k, (x2, y2) in enumerate(posiciones[i + 1]):
                conexion = lienzo.create_line(x1, y1, x2, y2, fill=color_conexion, width=4, tags=f"conexion_{i}_{j}_{k}")

    # Después de dibujar las conexiones, aseguramos que las neuronas estén por encima
    for i in range(capas):
        for j in range(len(posiciones[i])):
            lienzo.tag_raise(f"neurona_{i}_{j}")  # Asegura que las neuronas se dibujan sobre las conexiones

    # Mostrar la ventana
    root.mainloop()

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
        print("Modelo encontrado:")
        for capa in capas:
            print([modelo[neurona] for neurona in capa])
    else:
        print("No hay solución para la configuración dada.")


model=[3,25,25,25,25,25,25,1]
dibujar_red_neuronal(model)

# Genera todas las combinaciones posibles de valores booleanos.
valores = [True, False]
combinaciones = product(valores, repeat=8)  # 8 variables.

for combinacion in combinaciones:
    pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8 = combinacion
    #os.system("cls")  # Limpia la pantalla
    predecir(model,[False, False, False], [pos1])
    predecir(model,[False, False, True], [pos2])
    predecir(model,[False, True, False], [pos3])
    predecir(model,[False, True, True], [pos4])
    predecir(model,[True, False, False], [pos5])
    predecir(model,[True, False, True], [pos6])
    predecir(model,[True, True, False], [pos7])
    predecir(model,[True, True, True], [pos8])
