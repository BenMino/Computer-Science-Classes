# LIST EXERCISE

grades = [8.5, 6.0, 9.0, 7.0, 5.5]

sum = 0
approved = 0
failed = 0
quantity = 0

for grade in grades:
    sum = sum + grade
    quantity = quantity + 1

    if grade >= 7:
        approved = approved + 1
    else:
        failed = failed + 1

average = sum/quantity

print("---LIST---")
print(f"Suma total: {sum}")
print(f"Promedio: {average}")
print(f"Aprobado: {approved}")
print(f"Reprobados: {failed}")
print(" ")

# STRING EXERCISE

password = "Python2026"

letters = 0
numbers = 0
letter_o = 0

for character in password:

    if character.isalpha():
        letters = letters + 1

    if character.isdigit():
        numbers = numbers + 1

    if character == "o":
        letter_o = letter_o + 1

print("---STRING---")
print(f"Cantidad de letras: {letters}")
print(f"Cantidad de números: {numbers}")
print(f"Cantidad de la letra O: {letter_o}")
print(" ")

# SET EXERCISE

products = {"teclado", "mouse", "monitor", "mouse", "impresora"}

unique_products = 0
morethan6 = 0

for product in products:

    unique_products = unique_products + 1

    counter = 0

    for letter in product:
        counter = counter + 1

    if counter > 6:
        morethan6 = morethan6 + 1

print("---SET---")
print(f"Productos únicos: {unique_products}")
print(f"Productos con más de 6 letras: {morethan6}")
print(" ")

# BREAK EXERCISE

email = input("Introduce tu e-mail: ")

user = ""

for character in email:

    if character == "@":
        break

    user = user + character

print(f"Nombre de usuario: {user}")
print(" ")

# CONTINUE EXERCISE

phone = input("Introduce tu número de teléfono: ")

clean_phone = ""

for character in phone:

    if character == " " or character == "-":
        continue

    clean_phone = clean_phone + character

print(f"Número telefónico limpio: {clean_phone}")