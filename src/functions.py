# -*- coding: utf-8 -*-

import numpy as np

def caminata_aleatoria_2d(num_pasos):
    # Inicializar la posición en el origen (0, 0)
    posicion = np.array([0, 0])
    trayectoria = [posicion.copy()]

    # Definir posibles movimientos en las direcciones X e Y
    movimientos = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])

    for _ in range(num_pasos):
        # Elegir un movimiento aleatorio
        paso = movimientos[np.random.randint(0, 4)]
        # Actualizar la posición
        posicion += paso
        # Guardar la posición en la trayectoria
        trayectoria.append(posicion.copy())

    return np.array(trayectoria)
