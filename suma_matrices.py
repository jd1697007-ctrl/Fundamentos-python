# Programa para sumar dos matrices

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

C = [[0, 0],
     [0, 0]]

for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]

print("Matriz A:")
for fila in A:
    print(fila)

print("Matriz B:")
for fila in B:
    print(fila)

print("Suma de las matrices:")
for fila in C:
    print(fila)