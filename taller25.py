# -*- coding: utf-8 -*-
"""taller25.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10zu-3_pT5Sz8K7AHI4Fm2KSCGLslrFqY
"""

import copy
import math

def gaussJordan(a, b):
    aAux = copy.deepcopy(a)
    bAux = b.copy()

    n = len(bAux)

    #Se construye la matriz triangular superior
    for i in range(n):
        #Pivoteo
        if aAux[i][i] == 0:
            for k in range(i + 1, n):
                if aAux[k][i] != 0:
                    filaAux = aAux[i]
                    aAux[i] = aAux[k]
                    aAux[k] = filaAux

                    valoAux = bAux[i]
                    bAux[i] = bAux[k]
                    bAux[k] = valoAux
                    break

        #Escalonamiento
        valorAux = aAux[i][i]
        for j in range(i, n):
            aAux[i][j] /= valorAux
        bAux[i] /= valorAux

        #Reducción
        for j in range(n):
            if j != i:
                fact = aAux[j][i] / aAux[i][i]

                for k in range(n):
                    aAux[j][k] -= (aAux[i][k] * fact)
                bAux[j] -= (bAux[i] * fact)

    return bAux

# Datos de la tabla
tabla = {
    1: 1,
    2: 5,
    3: 4,
    4: 4,
    5: -2,
    6: 2,
    7: 9
}

# Extraer coordenadas x e y de la tabla
x = list(tabla.keys())
y = list(tabla.values())
n = len(x)

# Se crea la matriz de los trazadores
a = []
b = [0] * (n - 2)
for i in range(n - 2):
    a.append(b.copy())

for i in range(1, n - 1):
    if i > 1:
        a[i - 1][i - 2] = x[i] - x[i - 1]
    a[i - 1][i - 1] = 2 * (x[i + 1] - x[i - 1])
    if i < n - 2:
        a[i - 1][i] = x[i + 1] - x[i]
    b[i - 1] = (6 / (x[i + 1] - x[i])) * (y[i + 1] - y[i]) + (6 / (x[i] - x[i - 1]) * (y[i - 1] - y[i]))

# Resuelve el sistema de ecuaciones para obtener los trazadores cúbicos
rtaAux = gaussJordan(a, b)
f2 = [0] + rtaAux + [0]

# Calcula y muestra los polinomios de interpolación y trazadores cúbicos para cada intervalo
for i in range(1, n):
    t1 = f2[i - 1] / (6 * (x[i] - x[i - 1]))
    t2 = f2[i] / (6 * (x[i] - x[i - 1]))
    t3 = y[i - 1] / (x[i] - x[i - 1]) - f2[i - 1] * (x[i] - x[i - 1]) / 6
    t4 = y[i] / (x[i] - x[i - 1]) - f2[i] * (x[i] - x[i - 1]) / 6

    arrCoef = [0] * 4

    # Se calculan los coeficientes del polinomio
    arrCoef[0] = t1 * math.pow(x[i], 3) - t2 * math.pow(x[i - 1], 3) + t3 * x[i] - t4 * x[i - 1]
    arrCoef[1] = -t1 * 3 * math.pow(x[i], 2) + t2 * 3 * math.pow(x[i - 1], 2) - t3 + t4
    arrCoef[2] = t1 * 3 * x[i] - t2 * 3 * x[i - 1]
    arrCoef[3] = -t1 + t2

    print("Intervalo {x>=" + str(x[i - 1]) + "}{x<" + str(x[i]) + "}:")
    print("Polinomio de interpolación:")
    print("f(x) =", end="")
    for j in range(4):
        if arrCoef[j] != 0:
            if j > 0:
                print("+", end=" ")
            print(arrCoef[j], end="")
            if j == 0:
                print("", end=" ")
            elif j == 1:
                print("x", end=" ")
            else:
                print("x^" + str(j), end=" ")
    print()
    print("Trazador cúbico:")
    print("f(x) =", f2[i - 1], "/", (6 * (x[i] - x[i - 1])), "(x -", x[i], ")^3 +", f2[i], "/", (6 * (x[i] - x[i - 1])), "(x -", x[i - 1], ")^3 +", t3, "x +", t4)
    print()