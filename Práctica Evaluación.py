# ===== PARTE A =====
# Respuesta 1:
# a)
# nombre -> str
# edad -> int
# promedio -> float
# cursos -> list

# b)
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'list'>

# c)
# len(nombre) devuelve la cantidad de caracteres que tiene la cadena "Lucía".

# Respuesta 2:
# a)
# print() se usa para mostrar información en pantalla, mientras que input() se usa para pedir datos al usuario.

# b)
# Porque input() siempre devuelve un dato de tipo str, y no se puede usar directamente en operaciones matemáticas sin convertirlo a int o float.

# c)
# / realiza división normal lo cual da un resultado decimal
# // realiza división entera pero sin decimales
# % devuelve el residuo de la división

# d)
# import sys; print(sys.version)

# e)
# help('keywords')


# ===== PARTE B =====
# Código corregido

ancho = float(input("Ingrese el ancho del terreno: "))
largo = float(input("Ingrese el largo del terreno: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))

area = ancho * largo
costo = area * precio

print("Área total:", area)
print("Costo estimado:", costo)

# a)
# Los errores principales eran que input() devuelve texto y no números, por lo que no se podían hacer operaciones.
# Además, se intentaba concatenar texto con números sin convertirlos.

# b)
# La corrección convierte los datos a float, lo que permite hacer cálculos correctamente y mostrar resultados válidos.


# Construcción breve

frase = "Tecnología para todos"

print(frase.upper())
print(len(frase))
print("Python" in frase)

frase = frase.replace("Tecnología", "Programación")
print(frase)

palabras = frase.split()
print(palabras)


# ===== PARTE C =====
# Programa integrador

nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
pais = str(input("Ingrese su país: "))

ancho = float(input("Ingrese el ancho de la pared: "))
alto = float(input("Ingrese el alto de la pared: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))

area = ancho * alto
costo_total = area * precio

nombre_completo = nombre + " " + apellido

print(f"\n--- REPORTE FINAL ---")
print(f"Nombre completo: {nombre_completo}")
print(f"País: {pais}")
print(f"Área de la pared: {area}")
print(f"Costo total: {costo_total}")

print("Mayúsculas: ", nombre_completo.upper())
print("Longitud: ", len(nombre_completo))
print("¿Letra a presente?: ", "a" in nombre_completo.lower())
print("¿Costo total mayor que 100?: ", costo_total > 100)
