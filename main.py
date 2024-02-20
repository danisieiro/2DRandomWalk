# -*- coding: utf-8 -*-
"""
Este programa realiza una simulación de caminata aleatoria en 2D.
Comenzando en el origen, realiza movimientos de arriba a abajo y
de izquierda a derecha.

"""

import matplotlib.pyplot as plt
from src import functions

# Número de pasos en la caminata
num_pasos = 1000

# Realizar la caminata aleatoria en 2D
trayectoria = functions.caminata_aleatoria_2d(num_pasos)

# Obtener las coordenadas X e Y de la trayectoria
x = trayectoria[:, 0]
y = trayectoria[:, 1]

# Graficar la trayectoria en 2D
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', markersize=2, linestyle='-', color='b')
plt.title('Caminata Aleatoria en 2D')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
