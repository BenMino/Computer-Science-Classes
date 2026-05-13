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

average = sum / quantity

print("---LIST---")
print(f"Total sum: {sum}")
print(f"Average: {average}")
print(f"Approved: {approved}")
print(f"Failed: {failed}")

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
print(f"Letter quantity: {letters}")
print(f"Number quantity: {numbers}")
print(f"Letter O quantity: {letter_o}")

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
print(f"Unique products: {unique_products}")
print(f"Products with more than 6 letters: {morethan6}")


# -----------------------------------------
# EJERCICIO CON BREAK
# -----------------------------------------

correo = input("\nIngrese su correo electrónico: ")

usuario = ""

for caracter in correo:

    if caracter == "@":
        break

    usuario = usuario + caracter

print("Nombre de usuario:", usuario)


# -----------------------------------------
# EJERCICIO CON CONTINUE
# -----------------------------------------

telefono = input("\nIngrese su número de teléfono: ")

telefono_limpio = ""

for caracter in telefono:

    if caracter == " " or caracter == "-":
        continue

    telefono_limpio = telefono_limpio + caracter

print("Teléfono limpio:", telefono_limpio)