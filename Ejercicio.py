# Escribe tu código aquí :-)
def calcular_promedio(nombre, apellido, nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3

    print("\n--DATOS DEL ESTUDIANTE--")
    print("-" + f"Nombre: {nombre}")
    print("-" + f"Apellido: {apellido}")
    print("-" + f"Nota 1: {nota1}")
    print("-" + f"Nota 2: {nota2}")
    print("-" + f"Nota 3: {nota3}")
    print("-" + f"Promedio: {promedio}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))

calcular_promedio(nombre, apellido, nota1, nota2, nota3)
