# Escribe tu código aquí :-)

suma = 0

while True:
    cantidad = int(input("¿Cuántas notas quieres ingresar?: "))

    if cantidad > 0:
        break
    print("Valor inválido. Debe ingresar un número mayor a 0.")

for i in range(cantidad):
    nota = float(input("Ingrese una nota: "))
    suma = suma + nota

if cantidad == 1:
    print("La nota es:", nota)
else:
    promedio = suma / cantidad
    print("El promedio es:", promedio)
