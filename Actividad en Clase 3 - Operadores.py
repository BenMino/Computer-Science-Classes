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

# Función y = x² + 6x + 9 
x = -3 
y = x**2 + 6*x + 9 
print("y:", y) 

# Longitud y comparación 
print(len("python") == len("dragón")) 

# Verificar 'on' en ambas palabras 
print("on" in "python" and "on" in "dragón") 

# Verificar palabra en oración 
oracion = "Espero que este curso no esté lleno de jerga" 
print("jerga" in oracion) 

# Verificar 'on' en python y dragon 
print("on" in "python" and "on" in "dragon") 

# Longitud a float y string 
valor = len("python") 
print(str(float(valor))) 

# División entera vs entero 
print(7 // 3 == int(2.7)) 

# Comparar tipos 
print(type("10") == type(10)) 

# Comparación int 
print(int(float("9.8")) == 10) 

# Calcular pago 
horas = float(input("Ingrese horas: ")) 
tarifa = float(input("Ingrese tarifa por hora: ")) 
pago = horas * tarifa 
print("Pago:", pago) 

# Segundos vividos 
anios = int(input("Ingrese años: ")) 
segundos = anios * 365 * 24 * 60 * 60 
print("Segundos vividos:", segundos) 

# Mostrar tabla 
print("1 1 1 1 1") 
print("2 1 2 4 8") 
print("3 1 3 9 27") 
print("4 1 4 16 64") 
print("5 1 5 25 125") 