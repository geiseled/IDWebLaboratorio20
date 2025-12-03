# Autor: Pacheco Medina Geisel Reymar
# Ejercicio 4: calculadora de impuestos progresivos

# ingreso mensual
ingreso_mensual = float(input("Ingrese su ingreso mensual: "))  # ingreso del usuario

# calcular ingreso anual (12 meses + 2 aguinaldos)
ingreso_anual = ingreso_mensual * 14

# acumuladores
impuesto_total = 0
restante = ingreso_anual

# tramo 1 -> [0 - 20000] con tasa 0%
limite1 = 20000
if restante > 0:
    tramo1 = min(restante, limite1) # retorna el menor valor
    impuesto1 = tramo1 * 0
    impuesto_total += impuesto1
    restante -= tramo1
else:
    tramo1 = 0
    impuesto1 = 0

# tramo 2 -> (20000 - 50000] con tasa 10%
limite2 = 50000 - 20000  # tamaño del tramo -> 30000
if restante > 0:
    tramo2 = min(restante, limite2)
    impuesto2 = tramo2 * 0.10
    impuesto_total += impuesto2
    restante -= tramo2
else:
    tramo2 = 0
    impuesto2 = 0

# tramo 3 -> (50000 - 100000] con tasa 20%
limite3 = 100000 - 50000  # tamaño del tramo -> 50000
if restante > 0:
    tramo3 = min(restante, limite3)
    impuesto3 = tramo3 * 0.20
    impuesto_total += impuesto3
    restante -= tramo3
else:
    tramo3 = 0
    impuesto3 = 0

# tramo 4 -> > 100000 con tasa 30%
if restante > 0:
    tramo4 = restante
    impuesto4 = tramo4 * 0.30
    impuesto_total += impuesto4
    restante = 0
else:
    tramo4 = 0
    impuesto4 = 0

# tasa efectiva real
tasa_efectiva = (impuesto_total / ingreso_anual) * 100

# redondeo
impuesto_total = round(impuesto_total, 2)
tasa_efectiva = round(tasa_efectiva, 2)
impuesto1 = round(impuesto1, 2)
impuesto2 = round(impuesto2, 2)
impuesto3 = round(impuesto3, 2)
impuesto4 = round(impuesto4, 2)

# salida en consola
print("\n=== Calculo del impuesto anual ===")
print("Ingreso anual:", ingreso_anual, "/S")

print("\nImpuesto por tramos:")
print(f"Tramo 1 [0 - 20000] -> {impuesto1} /S")
print(f"Tramo 2 (20000 - 50000] -> {impuesto2} /S")
print(f"Tramo 3 (50000 - 100000] -> {impuesto3} /S")
print(f"Tramo 4 > 100000 -> {impuesto4} /S")

print("\nTotal de impuestos ->", impuesto_total, "/S")
print("Tasa efectiva real ->", tasa_efectiva, "%")
