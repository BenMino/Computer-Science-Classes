# Escribe tu código aquí :-)

def metros_a_centimetros(metros):
    return metros * 100

def metros_a_milimetros(metros):
    return metros * 1000

def metros_a_kilometros(metros):
    return metros / 1000

def metros_a_pulgadas(metros):
    return metros * 39.3701


metros = float(input("Ingrese una cantidad en metros: "))

while True:
    print("\n -MENÚ DE CONVERSIÓN- ")
    print("1. Centímetros")
    print("2. Milímetros")
    print("3. Kilómetros")
    print("4. Pulgadas")

    opcion = int(input("Seleccione una opción (1-4): "))

    if opcion == 1:
        resultado = metros_a_centimetros(metros)
        print(f"{metros} metros equivalen a {resultado} centímetros.")
        break

    elif opcion == 2:
        resultado = metros_a_milimetros(metros)
        print(f"{metros} metros equivalen a {resultado} milímetros.")
        break

    elif opcion == 3:
        resultado = metros_a_kilometros(metros)
        print(f"{metros} metros equivalen a {resultado} kilómetros.")
        break

    elif opcion == 4:
        resultado = metros_a_pulgadas(metros)
        print(f"{metros} metros equivalen a {resultado} pulgadas.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")





