def gauss_jordan(matrix):
    n = len(matrix)
    
    inverse = [[0] * n for _ in range(n)]
    for i in range(n):
        inverse[i][i] = 1
    
    for i in range(n):
        if matrix[i][i] == 0:
            raise ValueError("La matriz no es invertible")
        
        divisor = matrix[i][i]
        for j in range(n):
            matrix[i][j] /= divisor
            inverse[i][j] /= divisor
        
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(n):
                    matrix[k][j] -= factor * matrix[i][j]
                    inverse[k][j] -= factor * inverse[i][j]
    
    return inverse

matrix = [[3, 2, 2],
          [3, 1, -3],
          [1, 0, -2]]

try:
    inverse_matrix = gauss_jordan(matrix)
    print("Inversa de la matriz:")
    for row in inverse_matrix:
        print(row)
except ValueError as e:
    print(e)
