# Autor: Pacheco Medina Geisel Reymar
# Ejercicio 7: registro de estudiantes con menu iterativo

# lista donde se almacenan los estudiantes
estudiantes = []  # cada estudiante sera un diccionario


# funcion -> agregar estudiante
def agregar_estudiante():
    print("\n--- Agregar estudiante ---")

    # pedir nombre
    nombre = input("Ingrese el nombre: ").strip()

    # pedir edad -> debe ser entero positivo
    while True:
        edad = input("Ingrese la edad: ")
        if edad.isdigit():
            edad = int(edad)
            break
        else:
            print("Error: ingrese una edad valida.")

    # pedir promedio -> numero real entre 0 y 20
    while True:
        prom = input("Ingrese el promedio (0 a 20): ")
        try:
            promedio = float(prom)
            if 0 <= promedio <= 20:
                break
            else:
                print("Error: el promedio debe estar entre 0 y 20.")
        except:
            print("Error: ingrese un numero real.")

    # crear diccionario del estudiante
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio
    }

    # agregarlo a la lista
    estudiantes.append(estudiante)
    print("Estudiante agregado con exito.")


# funcion -> mostrar todos los estudiantes
def mostrar_estudiantes():
    print("\n--- Lista de estudiantes ---")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    for idx, est in enumerate(estudiantes, start=1):
        print(idx, "->", est["nombre"], "| edad:", est["edad"], "| promedio:", est["promedio"])


# funcion -> mostrar estudiante con mejor promedio
def mejor_promedio():
    print("\n--- Estudiante con mejor promedio ---")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    mejor = max(estudiantes, key=lambda e: e["promedio"])
    print("Nombre:", mejor["nombre"])
    print("Edad:", mejor["edad"])
    print("Promedio:", mejor["promedio"])


# funcion -> buscar estudiante por nombre
def buscar_por_nombre():
    print("\n--- Buscar por nombre ---")
    nombre = input("Ingrese el nombre a buscar: ").strip().lower()

    encontrados = [e for e in estudiantes if e["nombre"].lower() == nombre]

    if encontrados:
        print("Estudiante encontrado:")
        for e in encontrados:
            print("Nombre:", e["nombre"], "| edad:", e["edad"], "| promedio:", e["promedio"])
    else:
        print("No se encontro el nombre.")


# funcion -> eliminar por nombre
def eliminar_por_nombre():
    print("\n--- Eliminar por nombre ---")
    nombre = input("Ingrese el nombre a eliminar: ").strip().lower()

    global estudiantes
    antes = len(estudiantes)

    estudiantes = [e for e in estudiantes if e["nombre"].lower() != nombre]

    despues = len(estudiantes)

    if antes == despues:
        print("No se encontro el estudiante.")
    else:
        print("Estudiante eliminado con exito.")


# --- menu principal ---
while True:
    print("\nMENU PRINCIPAL")
    print("1) Agregar estudiante")
    print("2) Mostrar estudiantes")
    print("3) Mostrar estudiante con mejor promedio")
    print("4) Buscar por nombre")
    print("5) Eliminar por nombre")
    print("6) Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        mejor_promedio()
    elif opcion == "4":
        buscar_por_nombre()
    elif opcion == "5":
        eliminar_por_nombre()
    elif opcion == "6":
        print("Fin del programa.")
        break
    else:
        print("Opcion invalida.")
