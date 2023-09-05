def ordenar_fila(matriz, fila):
    matriz[fila] = sorted(matriz[fila])


# Matriz de ejemplo (3x3)
matriz_ejemplo2 = [
    [5, 12, 1],
    [8, 4, 10],
    [6, 3, 7]
]

fila_a_ordenar = 0

print("Matriz original:")
for fila in matriz_ejemplo2:
    print(fila)

ordenar_fila(matriz_ejemplo2, fila_a_ordenar)

print(f"\nMatriz con la fila {fila_a_ordenar + 1} ordenada:")
for fila in matriz_ejemplo2:
    print(fila)
