import math

def taylor_series_aproximacion(x, n):
    aproximacion = 0
    for i in range(n + 1):
        aproximacion += ((-1)**i * x**i) / math.factorial(i)
    return aproximacion

def error_relativo(Vverdadero, approxV):
    return abs((Vverdadero - approxV) / Vverdadero) * 100

def main():
    xbase = 0.5
    xt = 0.505
    x_target = xt - xbase  # Corregido: se debe calcular x_target antes de usarlo
    Vverdadero = math.exp(-xt)  # Corregido: se debe usar -xt para calcular el valor verdadero
    print("Valor verdadero de f(x) en x = 0.505:", Vverdadero)

    for n in range(16):
        approxV = taylor_series_aproximacion(x_target, n)  # Corregido: usar x_target en lugar de xt - xbase
        error = error_relativo(Vverdadero, approxV)
        print(f"Aproximación de orden {n}: {approxV}, Error relativo: {error}%")

if __name__ == "__main__":
    main()
