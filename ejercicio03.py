# Autor: Pacheco Medina Geisel Reymar
# Ejercicio 3: calcular salario bruto, descuentos y salario neto

# ingreso de datos
salario_base = float(input("Ingrese el salario base: ")) 
horas_extras = float(input("Ingrese las horas extras: ")) 
pago_hora_extra = float(input("Ingrese el pago por hora extra: ")) 
afp = float(input("Ingrese el porcentaje de AFP: ")) 
bono = 200  # bono fijo asignado por el empleador
salud = 9   # porcentaje EsSalud fijo

# calculos
salario_bruto = salario_base + (horas_extras * pago_hora_extra) + bono  # monto sin descuentos
descuento_afp = salario_base * (afp / 100)   # descuento AFP
descuento_salud = salario_base * (salud / 100)  # descuento salud
descuentos_totales = descuento_afp + descuento_salud # total de descuentos
salario_neto = salario_bruto - descuentos_totales # salario neto final

# redondeo de resultados en centimos 2 decimales
salario_bruto = round(salario_bruto, 2)
descuento_afp = round(descuento_afp, 2)
descuento_salud = round(descuento_salud, 2)
descuentos_totales = round(descuentos_totales, 2)
salario_neto = round(salario_neto, 2)

# salida de datos completos
print("\nDatos ingresados:")
print("Salario base:", salario_base, "/S")
print("Horas extras:", horas_extras)
print("Pago por hora extra:", pago_hora_extra, "/S")
print("Bono fijo:", bono, "/S")
print("AFP (%):", afp, "%")
print("Salud (%):", salud, "%")

# resultados solicitados
print("\nResultados:")
print("Salario bruto:", salario_bruto, "/S")
print("Descuento AFP:", descuento_afp, "/S")
print("Descuento salud:", descuento_salud, "/S")
print("Descuentos totales:", descuentos_totales, "/S")
print("Salario neto:", salario_neto, "/S")
