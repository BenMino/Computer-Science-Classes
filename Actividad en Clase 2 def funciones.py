# Escribe tu código aquí :-)

def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3)/3

def nota_mayor(nota1, nota2, nota3):
    if nota1 > nota2 and nota1 > nota3:
        return nota1
    elif nota2 > nota1 and nota2 > nota3:
            return nota2
    else:
        return nota3

def nota_menor(nota1, nota2, nota3):
    if nota1 < nota2 and nota1 < nota3:
        return nota1
    elif nota2 < nota1 and nota2 < nota3:
            return nota2
    else:
        return nota3

def estado_estudiante(n1, n2, n3):
    promedio = calcular_promedio(n1, n2, n3)

    if promedio >= 7:
        return "aprobado"
    else:
        return "reprobado"

nota1 = float(input("Ingrese la primera calificación: "))
nota2 = float(input("Ingrese la segunda calificación: "))
nota3 = float(input("Ingrese la tercera calificación: "))

while True:
    print("\n -MENÚ DE CALIFICACIONES- ")
    print("1. Calcular el promedio")
    print("2. Mostrar la nota mayor")
    print("3. Mostrar la nota menor")
    print("4. Determinar si el estudiante aprueba o reprueba")

    opcion = int(input("Seleccione una opción (1-4): "))

    if opcion == 1:
        resultado = calcular_promedio(nota1, nota2, nota3)
        print(f"El promedio es igual a {resultado}.")
        break

    elif opcion == 2:
        resultado = nota_mayor(nota1, nota2, nota3)
        print(f"La nota mayor es {resultado}.")
        break

    elif opcion == 3:
        resultado = nota_menor(nota1, nota2, nota3)
        print(f"La nota menor es {resultado}.")
        break

    elif opcion == 4:
        resultado = estado_estudiante(nota1, nota2, nota3)
        print(f"El estudiante está {resultado}.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")

