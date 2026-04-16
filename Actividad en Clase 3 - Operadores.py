# Edad entero
edad = 15
print("Edad:", edad)

# Estatura dcimal
estatura = 1.75
print("Estatura:", estatura)

# Área de un triángulo
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area_triangulo = 0.5 * base * altura
print("Área del triángulo:", area_triangulo)

# Perímetro de un triángulo
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))
perimetro_triangulo = a + b + c
print("Perímetro del triángulo:", perimetro_triangulo)

# Área y perímetro de un rectángulo
longitud = float(input("Longitud del rectángulo: "))
ancho = float(input("Ancho del rectángulo: "))
area_rect = longitud * ancho
perimetro_rect = 2 * (longitud + ancho)
print("Área rectángulo:", area_rect)
print("Perímetro rectángulo:", perimetro_rect)

# Área y circunferencia de un círculo
radio = float(input("Radio del círculo: "))
pi = 3.14
area_circulo = pi * radio * radio
circunferencia = 2 * pi * radio
print("Área círculo:", area_circulo)
print("Circunferencia círculo:", circunferencia)

# Pendiente y distancia entre dos puntos
x1, y1 = 2, 2
x2, y2 = 5, 6
pendiente = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Pendiente entre los puntos:", pendiente)
print("Distancia entre los puntos:", distancia)



