# Autor: Pacheco Medina Geisel Reymar
# Ejercicio 6: normalizar datos usando NumPy

import numpy as np # importamos la libreria Numerical Python

# funcion que normaliza segun el modo
def normalizar(lista, modo):
    arr = np.array(lista)  # convertir lista en un arreglo numpy

    if modo == "minmax":
        minimo = np.min(arr)
        maximo = np.max(arr)
        rango = maximo - minimo

        if rango == 0:
            return np.zeros_like(arr)  # si rango es 0 -> todos los valores son iguales y dividir entre 0 produce error NaN

        return (arr - minimo) / rango

    elif modo == "zscore":
        media = np.mean(arr)
        desviacion = np.std(arr)

        if desviacion == 0:
            return np.zeros_like(arr)  # desviacion 0 -> todos los valores son iguales y dividir entre 0 produce NaN

        return (arr - media) / desviacion

    elif modo == "unit":
        norma = np.linalg.norm(arr)

        if norma == 0:
            return np.zeros_like(arr)  # norma 0 -> vector nulo, no existe vector unitario, evitar division entre 0

        return arr / norma

# pedir cantidad de valores
while True:
    entrada = input("Ingrese la cantidad de valores del vector: ")

    if entrada.isdigit():  # validar que el usuario ingreso un entero positivo
        n = int(entrada)
        if n >= 1:         # validar que sea 1 o mayor
            break
        else:
            print("Error: el numero debe ser mayor o igual a 1.")
    else:
        print("Error: debe ingresar un numero entero positivo.")

# pedir los valores reales
valores = []
for i in range(n):
    while True:
        dato = input("Ingrese el valor " + str(i + 1) + ": ")
        try:
            numero = float(dato)
            valores.append(numero)
            break
        except:
            print("Error: debe ingresar un numero real.")

# resultados
print("\nResultados:\n")
print("MinMax:\n", normalizar(valores, "minmax"))
print("Z-score:\n", normalizar(valores, "zscore"))
print("Unit:\n", normalizar(valores, "unit"))
print("Original:\n", valores)
