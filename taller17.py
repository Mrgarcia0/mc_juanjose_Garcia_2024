# -*- coding: utf-8 -*-
"""taller17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LE1pcxvFakgwtiUQx5nWhJ4vc7d0TOo_
"""

import numpy as np

def linear_regression(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = 0
    denominator = 0
    for i in range(n):
        numerator += (x[i] - x_mean) * (y[i] - y_mean)
        denominator += (x[i] - x_mean) ** 2

    m = numerator / denominator
    c = y_mean - m * x_mean

    return m, c

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [9, 7, 8, 5, 6, 4.5, 4, 2.5]

m, c = linear_regression(x, y)

print("Coeficientes de la línea de regresión:")
print("Pendiente (m):", m)
print("Intercepto (c):", c)