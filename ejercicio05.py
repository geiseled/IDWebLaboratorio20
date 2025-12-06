# Autor: Pacheco Medina Geisel Reymar
# Ejercicio 5: generar una matriz NxN en espiral

# pedir N y validar que sea entero y N >= 3
while True:
    entrada = input("Ingrese un numero N (mayor o igual a 3): ")
    if entrada.isdigit():                  # validar que sea numero entero positivo
        N = int(entrada)
        if N >= 3:                         # validar rango
            break
        else:
            print("Error: N debe ser mayor o igual a 3.")
    else:
        print("Error: debe ingresar un numero entero.")

# crear matriz NxN llena de ceros
matriz = [[0 for _ in range(N)] for _ in range(N)]

# limites del recorrido en espiral
top = 0                # limite superior
bottom = N - 1         # limite inferior
left = 0               # limite izquierdo
right = N - 1          # limite derecho

num = 1                # numero inicial
max_num = N * N        # ultimo numero a colocar

# llenar matriz en espiral
while num <= max_num:

    # recorrer izquierda -> derecha
    for j in range(left, right + 1):
        if num <= max_num:
            matriz[top][j] = num
            num += 1
    top += 1

    # recorrer arriba -> abajo
    for i in range(top, bottom + 1):
        if num <= max_num:
            matriz[i][right] = num
            num += 1
    right -= 1

    # recorrer derecha -> izquierda
    for j in range(right, left - 1, -1):
        if num <= max_num:
            matriz[bottom][j] = num
            num += 1
    bottom -= 1

    # recorrer abajo -> arriba
    for i in range(bottom, top - 1, -1):
        if num <= max_num:
            matriz[i][left] = num
            num += 1
    left += 1

# imprimir matriz con formato
print("\nMatriz en espiral:\n")
for fila in matriz:
    for valor in fila:
        print(f"{valor}\t", end="")   # usamos tabulacion para alinear columnas
    print()
