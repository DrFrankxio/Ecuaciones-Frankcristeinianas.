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
    color_neurona = "lightblue"
    color_conexion = "gray"

    # Definir el espacio entre capas y el radio de las neuronas
    espacio_entre_capas = 200
    radio_neurona = 20

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
                                         fill=color_neurona, outline="black", tags=f"neurona_{i}_{j}")
            # Añadir texto con el número de neurona (opcional)
            lienzo.create_text(x, y, text=f"n{j+1}", font=("Arial", 8), tags=f"neurona_{i}_{j}")

        # Guardar las posiciones de la capa
        posiciones.append(capa_posiciones)

    # Dibujar las conexiones entre neuronas
    for i in range(capas - 1):
        for j, (x1, y1) in enumerate(posiciones[i]):
            for k, (x2, y2) in enumerate(posiciones[i + 1]):
                conexion = lienzo.create_line(x1, y1, x2, y2, fill=color_conexion, width=1, tags=f"conexion_{i}_{j}_{k}")

    # Después de dibujar las conexiones, aseguramos que las neuronas estén por encima
    for i in range(capas):
        for j in range(len(posiciones[i])):
            lienzo.tag_raise(f"neurona_{i}_{j}")  # Asegura que las neuronas se dibujan sobre las conexiones

    # Mostrar la ventana
    root.mainloop()



def predecir(model, entrada, salida):
    # Definir las entradas para la predicción
    i1, i2, i3 = entrada  # Entradas
    o1 = salida[0]  # Salida deseada

    # Crear los valores de neuronas y pesos (simulados con True/False para simplificación)
    # En este caso, model es la lista que define el número de neuronas en cada capa
    capas = len(model) - 1  # Número de capas (total de neuronas - 1)
    activaciones = []  # Almacenar activaciones de cada capa

    # Simulación de las activaciones de las neuronas por capa
    for capa in range(capas):
        num_neuronas = model[capa]
        activaciones_capa = []  # Activaciones de esta capa
        
        # Simulamos las activaciones de las neuronas para esta capa
        for i in range(num_neuronas):
            activacion = f"Neurona {i+1} en Capa {capa+1} - Activación: {True if i % 2 == 0 else False}"  # Valor simulado
            activaciones_capa.append(activacion)
        
        activaciones.append(activaciones_capa)  # Añadir las activaciones de esta capa



# Bucle principal
def bucle1():
    valores = [True, False]
    combinaciones = product(valores, repeat=8)  # 8 variables (i1, i2, i3, o1)

    # Crear un modelo con una cantidad arbitraria de neuronas
    model = [3, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]
    dibujar_red_neuronal(model)

    # Procesar cada combinación de entradas
    for combinacion in combinaciones:
        pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8 = combinacion
        # Llamamos a predecir para cada combinación
        predecir(model, [False, False, False], [pos1])
        predecir(model, [False, False, True], [pos2])
        predecir(model, [False, True, False], [pos3])
        predecir(model, [False, True, True], [pos4])
        predecir(model, [True, False, False], [pos5])
        predecir(model, [True, False, True], [pos6])
        predecir(model, [True, True, False], [pos7])
        predecir(model, [True, True, True], [pos8])

# Ejecuta el bucle
bucle1()
