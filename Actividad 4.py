# Nivel 1 - Operaciones Básicas

texto = str("Programación Para Todos")
print("Texto: ", texto)
print("Cantidad de caracteres: ", len(texto))

# Nivel 2 - Transformación de Texto

print("Mayúsculas:", texto.upper())
print("Minúsculas:", texto.lower())
print("Title:", texto.title())
print("Capitalize:", texto.capitalize())

# Nivel 3 - Búsqueda y Verificación

print("¿Empieza con 'Programación'?:", texto.startswith("Programación"))
print("¿Termina con 'Todos'?:", texto.endswith("Todos"))
print("Posición de 'Para':", texto.find("Para"))
print("¿Contiene 'Python'?:", "Python" in texto)

# Nivel 4 - Manipulación

texto2 = texto.replace("Programación", "Python")
print("Reemplazar:", texto2)
palabras = texto.split()
print("Palabras:", palabras)
unir = " - ".join(palabras)
print("Unión:", unir)

# Nivel 5 - Índices
print("Primer carácter:", texto[0])
# 16. Último carácter
print("Último carácter:", texto[-1])
# 17. Carácter en posición 5
print("Carácter en posición 5:", texto[5])

# Nivel 6 - Aplicación Simple
nombre = "Ben"
apellido = "Mino"
print("Nombre completo: " + nombre + " " + apellido)
print(f"Hola, mi nombre es {nombre}")
iniciales_nombre = nombre[0]
iniciales_apellido = apellido[0]
print("Acrónimo:", iniciales_nombre + iniciales_apellido)

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding' 
