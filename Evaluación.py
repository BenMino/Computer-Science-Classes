# ===== PARTE A =====

# Respuesta 1:  Análisis de datos y código (15 puntos) 

# a) Indica el tipo de dato de cada variable. 
# nombre -> str
# edad -> int
# promedio -> float
# materias -> list

# b) Escribe qué mostraría el programa en pantalla. 
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'list'>

# c) Explica qué hace len(nombre).
# len(nombre) devuelve la cantidad de caracteres que tiene la cadena "Mateo".

# Respuesta 2: Comprensión conceptual (15 puntos)

# a) ¿Qué diferencia hay entre almacenar un valor en una variable y mostrarlo con print()?
# La diferencia es que almacenar un valor en una variable lo guarda en la memoria para su uso posterior, mientras que print() se usa para mostrar información en pantalla al usuario.

# b) ¿Por qué input() devuelve texto aunque el usuario escriba un número?
# Porque input() siempre devuelve un dato de tipo str, y no se puede usar directamente en operaciones matemáticas sin convertirlo a int o float.

# c) Explica la diferencia entre **, // y %.
# ** realiza la potenciación
# // realiza división entera pero sin decimales
# % devuelve el residuo de la división

# d)  Escribe una instrucción que permita consultar las palabras reservadas de Python.
# import sys; print(sys.version) o también help('keywords')

# ===== PARTE B =====

# Repuesta 3: Corrección de código (15 puntos)
base = float(input("Ingrese la base del anuncio: ")) 
altura = float(input("Ingrese la altura del anuncio: ")) 
precio = float(input("Ingrese el precio por metro cuadrado: "))

superficie = base * altura 
valor = superficie * precio 

print("Superficie total: " + str(superficie)) 
print("Valor estimado: " + str(valor))

# a) ¿Cuáles eran los errores principales? 
# Los errores principales eran que se intentaba concatenar strings con variables numéricas sin convertirlas a strings primero.
# b) ¿Por qué tu corrección sí funciona? 
# La corrección funciona porque se convierten las variables numéricas a strings antes de concatenarlas con los mensajes de impresión.

# Respuesta 4: Construcción breve (15 puntos)
frase = "Aprender Python es útil"

print(frase.lower())
print(len(frase))
print("Python" in frase)

frase = frase.replace("útil", "interesante")
print(frase)

palabras = frase.split()
print(palabras)

