"""
Nombre: Ben Mino
Fecha: 2026-04-15
Título: Actividad en Clase Variables
"""

# Ejercicios parte 1
nombre = "Ben"
apellido = "Mino"
nombreCompleto = nombre + apellido
pais = "Ecuador"
ciudad = "Quito"
edad = 15
anio = 2026
estaCasado = False
esVerdadero = True
luzEncendida = False

color, comida, animal = "azul", "pizza", "perro"

# Ejercicios parte 2
print(type(nombre))
print(type(apellido))
print(type(nombreCompleto))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(anio))
print(type(estaCasado))
print(type(esVerdadero))
print(type(luzEncendida))

print("Longitud de nombre:", len(nombre))
print("¿El nombre es más largo que apellido?:", len(nombre) > len(apellido))

numeroUno = 5
numeroDos = 4

total = numeroUno + numeroDos
diferencia = numeroUno - numeroDos
producto = numeroUno * numeroDos
division = numeroUno / numeroDos
residuo = numeroDos % numeroUno
potencia = numeroUno ** numeroDos
divisionEntera = numeroUno // numeroDos

print("Suma:", total)
print("Diferencia:", diferencia)
print("Producto:", producto)
print("División:", division)
print("Residuo:", residuo)
print("Potencia:", potencia)
print("División entera:", divisionEntera)

radio = 30
pi = 3.1416
areaCirculo = pi * radio ** 2
print("Área del círculo:", areaCirculo)
circunferenciaCirculo = 2 * pi * radio
print("Circunferencia del círculo:", circunferenciaCirculo)
radio_usuario = float(input("Ingresa el radio del círculo: "))
area_usuario = pi * radio_usuario ** 2
print("Área con radio ingresado:", area_usuario)

nombre_user = input("Ingresa tu nombre: ")
apellido_user = input("Ingresa tu apellido: ")
pais_user = input("Ingresa tu país: ")
edad_user = int(input("Ingresa tu edad: "))

help('keywords')

