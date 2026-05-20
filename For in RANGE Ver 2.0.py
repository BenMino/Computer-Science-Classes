# NORMAL
numero = int(input("Ingrese un número: "))
limite_inferior = int(input("Ingrese desde qué número desea ver: "))
limite_superior = int(input("Ingrese hasta qué número desea ver: "))

print(f"Tabla de multiplicar del número {numero} desde {limite_inferior} hasta {limite_superior}")

for i in range (limite_inferior,limite_superior + 1):
    print(f"{numero} x {i} = {numero * i}")

# LISTA
grades = [5, 8, 9, 7, 10]
sum = 0
quantity = 0

for i in range (1,4):
    sum += grades[i]
    quantity += 1

average = sum/quantity
print(f"The average is: {average}")

