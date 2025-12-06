# Autor: Pacheco Medina Geisel Reymar
# Ejercicio 6: normalizar datos sin librerias externas

# funcion que normaliza segun el modo solicitado
def normalizar(lista, modo):
    # MINMAX
    if modo == "minmax":
        minimo = min(lista)
        maximo = max(lista)
        rango = maximo - minimo

        if rango == 0:  # evitar division por cero
            return [0 for _ in lista]

        return [(x - minimo) / rango for x in lista]

    # Z-SCORE
    elif modo == "zscore":
        media = sum(lista) / len(lista)
        suma_cuadrados = sum((x - media) ** 2 for x in lista)
        desviacion = (suma_cuadrados / len(lista)) ** 0.5

        if desviacion == 0:
            return [0 for _ in lista]

        return [(x - media) / desviacion for x in lista]

    # UNIT (vector normalizado)
    elif modo == "unit":
        norma = (sum(x ** 2 for x in lista)) ** 0.5

        if norma == 0:
            return [0 for _ in lista]

        return [x / norma for x in lista]


# pedir cantidad de datos
while True:
    entrada = input("Ingrese la cantidad de valores del vector: ")
    try:
        n = int(entrada)
        if n >= 1:
            break
        else:
            print("Error: el numero debe ser mayor o igual a 1.")
    except:
        print("Error: debe ingresar un numero entero.")

# pedir los valores reales
valores = []
for i in range(n):
    while True:
        dato = input("Ingrese el valor " + str(i + 1) + ": ")
        try:
            numero = float(dato)   # validar numero real
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
