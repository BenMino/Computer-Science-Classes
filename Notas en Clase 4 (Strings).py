stringVariasLineas = """
Ben Mino
Programación 1
Actividad 4 (Strings)"""
print(stringVariasLineas)

ciudad = str("Newcastle")
print(len(ciudad))

name = str("Ben")
last_name = str("Mino")
full_name = name + " " + last_name
print(full_name)

print(str("Python\nChallenge"))
print("Nombre\tSemana1\tSemana2\tSemana3")
print("símbolo@\\\"")
print(f"Mi nombre es {name} y mi apellido es {last_name}")

language = "Python"
a, b, c, d, e, f = language
print(a)
print(c)
print(language[0])
print(language[0:3])
print(language[0:5])
print(language[-3])

greeting = "Hello, World!"
print(greeting[::-1])

language = "Python"
pto = language[0:6:2]
print(pto)
yhn = language[1:6:2]
print(yhn)

challenge = 'thirty days of python'
print(challenge.capitalize())

challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))





