# Autor: Pacheco Medina Geisel Reymar
# Ejercicio 5: generar una matriz NxN en forma de espiral

# pedir N y validar que sea entero y N >= 3
while True:
    entrada = input("Ingrese un numero N (mayor o igual a 3): ")
    if entrada.isdigit(): # isdigit comprueba que sea un entero positivo
        N = int(entrada)
        if N >= 3:
            break
        else:
            print("Error: ingrese un numero N mayor o igual a 3.")
    else:
        print("Error: debe ingresar un numero entero.")

# crear matriz NxN 
matriz = [[0 for _ in range(N)] for _ in range(N)]

# limites del recorrido en espiral
arriba = 0
abajo = N - 1
izquierda = 0
derecha = N - 1

numero = 1
maximo = N * N

# llenar matriz en espiral
while numero <= maximo:

    # recorrer izquierda -> derecha
    for j in range(izquierda, derecha + 1):
        matriz[arriba][j] = numero
        numero += 1
    arriba += 1

    # recorrer arriba -> abajo
    for i in range(arriba, abajo + 1):
        matriz[i][derecha] = numero
        numero += 1
    derecha -= 1

    # recorrer derecha -> izquierda
    for j in range(derecha, izquierda - 1, -1):
        matriz[abajo][j] = numero
        numero += 1
    abajo -= 1

    # recorrer abajo -> arriba
    for i in range(abajo, arriba - 1, -1):
        matriz[i][izquierda] = numero
        numero += 1
    izquierda += 1

# imprimir matriz
print("\nMatriz en espiral:\n")
for fila in matriz:
    for valor in fila:
        print(f"{valor}\t", end="")
    print()

