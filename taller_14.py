# -*- coding: utf-8 -*-
"""taller 14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u3Ubp6OxUzmREHqB0BYxOu2BBKanfj1l
"""

def escalar(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))
def main():
    n = int(input("Ingrese la longitud: "))
    print("Ingrese el primer vector:")
    v1 = [float(input(f"Ingrese el elemento {i+1}: ")) for i in range(n)]
    print("Ingrese el segundo vector:")
    v2 = [float(input(f"Ingrese el elemento {i+1}: ")) for i in range(n)]
    rta = escalar(v1, v2)
    print(f"El producto escalar es: {rta}")
if __name__ == "__main__":
    main()

def multiplicar_matrices(matriz1, matriz2):

    if len(matriz1[0]) != len(matriz2):
        return "No se pueden multiplicar las matrices"


    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            fila.append(0)
        resultado.append(fila)


    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

def main():

    filas_A = int(input("Ingrese el número de filas de la matriz A: "))
    columnas_A = int(input("Ingrese el número de columnas de la matriz A: "))
    filas_B = int(input("Ingrese el número de filas de la matriz B: "))
    columnas_B = int(input("Ingrese el número de columnas de la matriz B: "))

    print("\nIngrese los elementos de la matriz A:")
    matriz_A = []
    for i in range(filas_A):
        fila = []
        for j in range(columnas_A):
            elemento = float(input(f"Ingrese el elemento ({i+1},{j+1}): "))
            fila.append(elemento)
        matriz_A.append(fila)


    print("\nIngrese los elementos de la matriz B:")
    matriz_B = []
    for i in range(filas_B):
        fila = []
        for j in range(columnas_B):
            elemento = float(input(f"Ingrese el elemento ({i+1},{j+1}): "))
            fila.append(elemento)
        matriz_B.append(fila)


    resultado_3A = [[3 * elemento for elemento in fila] for fila in matriz_A]
    resultado_4B = [[4 * elemento for elemento in fila] for fila in matriz_B]

    if filas_A == filas_B and columnas_A == columnas_B:
        resultado_suma = [[matriz_A[i][j] + matriz_B[i][j] for j in range(columnas_A)] for i in range(filas_A)]
    else:
        resultado_suma = "No se pueden sumar las matrices, las dimensiones no coinciden"

    resultado_producto = multiplicar_matrices(matriz_B, matriz_A)


    print("\n3A:")
    for fila in resultado_3A:
        print(fila)

    print("\n4B:")
    for fila in resultado_4B:
        print(fila)

    print("\nA + B:")
    if isinstance(resultado_suma, str):
        print(resultado_suma)
    else:
        for fila in resultado_suma:
            print(fila)

    print("\nB × A:")
    if isinstance(resultado_producto, str):
        print(resultado_producto)
    else:
        for fila in resultado_producto:
            print(fila)

if __name__ == "__main__":
    main()