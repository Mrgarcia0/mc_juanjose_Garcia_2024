# -*- coding: utf-8 -*-
"""taller 20.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Xbh3z9SLdr2w_4rAvBc2iQj90Rx0Hj8D
"""

import numpy as np

# Datos de entrada
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([0.1, 0.3, 0.9, 1.7, 2.8, 4.5, 6.9])

# Calcular la pendiente (m) y la intersección con el eje y (b)
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x_squared = np.sum(x ** 2)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
b = (sum_y - m * sum_x) / n

# Calcular los valores predichos de y
y_predicted = m * x + b

# Calcular la desviación estándar (sy)
sy = np.sqrt(np.sum((y - y_predicted) ** 2) / (n - 2))

# Calcular el coeficiente de correlación (r)
r = (n * sum_xy - sum_x * sum_y) / np.sqrt((n * sum_x_squared - sum_x ** 2) * (n * np.sum(y ** 2) - sum_y ** 2))

# Calcular el coeficiente de determinación (r^2)
r_squared = r ** 2

# Calcular el error estándar de la estimación (s Τ yx)
s_yx = sy * np.sqrt(1 - r_squared)

# Imprimir los resultados
print("Pendiente (m):", m)
print("Intersección con el eje y (b):", b)
print("Desviación estándar (sy):", sy)
print("Coeficiente de correlación (r):", r)
print("Coeficiente de determinación (r^2):", r_squared)
print("Error estándar de la estimación (s Τ yx):", s_yx)