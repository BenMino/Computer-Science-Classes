# Escribe tu código aquí :-)
def obtener_mensaje():
    mensaje = 'Bienvenido al Sistema'
    return mensaje

def generar_nombre_completo(nombre, apellido):
    nombre_completo = nombre + " " + apellido
    return nombre_completo

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

print(f"{obtener_mensaje()}, {generar_nombre_completo(nombre, apellido)}")
