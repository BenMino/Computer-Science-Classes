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
# input() devuelve siempre un texto (str), incluso si se escriben números. Si se usa directamente en un cálculo, puede dar error porque las operaciones matemáticas requieren datos numéricos como int o float.

# c) Explica la diferencia entre **, // y %.
# ** realiza la potenciación
# // realiza división entera pero sin decimales
# % devuelve el residuo de la división

# d)  Escribe una instrucción que permita consultar las palabras reservadas de Python.
help('keywords')

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
# Los errores principales eran que los datos ingresados con input() no se convertían a números, por lo que no se podían hacer operaciones matemáticas correctamente.
# b) ¿Por qué tu corrección sí funciona? 
# La corrección funciona porque convierte los datos a float, permitiendo hacer cálculos. También usa una forma correcta de mostrar resultados, evitando errores al combinar texto y números con (str) y (float).

# Respuesta 4: Construcción breve (15 puntos)
frase = "Aprender Python es útil"

print("Frase en minúsculas: " + frase.lower())
print("Longitud de la frase: " + str(len(frase)))
print("¿Está 'Python' en la frase? " + str("Python" in frase))

frase = frase.replace("útil", "interesante")
print("Frase modificada: " + frase)

palabras = frase.split()
print("Palabras en la frase: " + str(palabras))


