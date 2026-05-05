# ===== NIVEL 1 =====

# Ejercicio 1: Edad para conducir
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Tienes la edad suficiente para aprender a conducir.")
else:
    faltan = 18 - edad
    print(f"Necesitas {faltan} años más para aprender a conducir.")


# Ejercicio 2: Comparar edades
my_age = 15
your_age = int(input("Ingrese su edad: "))

if your_age > my_age:
    diferencia = your_age - my_age
    if diferencia == 1:
        print("Eres 1 año mayor que yo.")
    else:
        print(f"Eres {diferencia} años mayor que yo.")
elif your_age < my_age:
    diferencia = my_age - your_age
    if diferencia == 1:
        print("Soy 1 año mayor que tú.")
    else:
        print(f"Soy {diferencia} años mayor que tú.")
else:
    print("Tenemos la misma edad.")


# Ejercicio 3: Comparar dos números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")


# ===== NIVEL 2 =====

# Ejercicio 4: Calificación
puntaje = int(input("Ingrese su puntaje: "))

if 90 <= puntaje <= 100:
    print("Calificación: A")
elif 80 <= puntaje <= 89:
    print("Calificación: B")
elif 70 <= puntaje <= 79:
    print("Calificación: C")
elif 60 <= puntaje <= 69:
    print("Calificación: D")
elif 0 <= puntaje <= 59:
    print("Calificación: F")
else:
    print("Puntaje inválido")


# Ejercicio 5: Estación del año
mes = input("Ingrese el mes: ").lower()

if mes in ["septiembre", "octubre", "noviembre"]:
    print("Otoño")
elif mes in ["diciembre", "enero", "febrero"]:
    print("Invierno")
elif mes in ["marzo", "abril", "mayo"]:
    print("Primavera")
elif mes in ["junio", "julio", "agosto"]:
    print("Verano")
else:
    print("Mes no válido")


# Ejercicio 6: Lista de frutas
fruits = ['banana', 'orange', 'mango', 'lemon']
fruta = input("Ingrese una fruta: ").lower()

if fruta in fruits:
    print("Esa fruta ya existe en la lista")
else:
    fruits.append(fruta)
    print("Lista actualizada:", fruits)


# ===== EJERCICIO COMBINADO =====

edad = int(input("Ingrese la edad del estudiante: "))
promedio = float(input("Ingrese el promedio académico: "))
permiso = input("¿Tiene permiso de sus padres? (si/no): ").lower()

if edad < 12:
    if permiso == "si":
        print("Puede ingresar con supervisión")
    else:
        print("No puede ingresar a la plataforma")

elif 12 <= edad <= 17:
    if promedio >= 8.5:
        print("Acceso completo a cursos avanzados")
    elif promedio >= 7:
        print("Acceso a cursos intermedios")
    else:
        print("Acceso solo a cursos básicos")

else:
    print("Acceso libre a la plataforma")