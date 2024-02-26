import math

def cosenoaproximado(x, epsilon):
    terminoactual = 1
    cosxaproximado = terminoactual
    iteraciones = 0
    
    while True:
        iteraciones += 1
        terminosiguiente = -terminoactual * x**2 / ((2 * iteraciones) * (2 * iteraciones - 1))
        
        if abs(terminosiguiente) < epsilon:
            break
        
        cosxaproximado += terminosiguiente
        terminoactual = terminosiguiente
        
    erroraproximado = abs((math.cos(x) - cosxaproximado) / math.cos(x)) * 100
    
    return cosxaproximado, erroraproximado, iteraciones

def main():
    x = float(input("Ingrese el valor en radianes para evaluar su coseno: "))
    epsilon = float(input("Ingrese el criterio de error esperado (epsilon): "))
    
    valorestimado, error_rel_porcentual, iteraciones = cosenoaproximado(x, epsilon)
    
    print(f"Valor estimado de cos({x}): {valorestimado}")
    print(f"Error aproximado relativo porcentual: {error_rel_porcentual:.8f}%")
    print(f"Número de iteraciones realizadas: {iteraciones}")

if __name__ == "__main__":
    main()
