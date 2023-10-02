def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j
    return None


# Matriz de ejemplo (3x3)
matriz_ejemplo2 = [
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
]

valor_a_buscar = 88
posicion = buscar_valor(matriz_ejemplo2, valor_a_buscar)

if posicion:
    fila, columna = posicion
    print(f"Encontrado: El valor {valor_a_buscar} se encuentra en la fila {fila + 1}, columna {columna + 1}.")
else:
    print(f"No encontrado: El valor {valor_a_buscar} no se encuentra en la matriz.")
