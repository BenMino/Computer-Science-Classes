# =========================================
# 1. CICLO WHILE CON VARIABLE DE CONTROL
# Suma acumulativa
# =========================================

numero = int(input("Ingrese un número entero positivo: "))

contador = 1
suma = 0

while contador <= numero:
    suma += contador
    contador += 1

print("La suma total es:", suma)


# =========================================
# 2. CICLO WHILE CON BREAK
# Control de presupuesto
# =========================================

total_compras = 0
cantidad_compras = 0

while True:
    precio = float(input("Ingrese el precio del producto: "))

    if precio <= 0:
        break

    total_compras += precio
    cantidad_compras += 1

print("Cantidad de compras:", cantidad_compras)
print("Suma total de compras:", total_compras)
print("Registro de compras finalizado")


# =========================================
# 3. CICLO WHILE CON CONTINUE
# Filtro de números
# =========================================

limite = int(input("Ingrese un número entero positivo: "))

contador = 1

while contador <= limite:

    if contador % 5 == 0:
        contador += 1
        continue

    print(contador)
    contador += 1