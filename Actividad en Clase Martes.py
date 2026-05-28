num = int(input("Ingrese el número de estudiantes que desea ingresar: "))
def informacion(nombre,curso):
    print("Datos del estudiante")
    print(f"Nombre: {nombre}")
    print(f"Curso: {curso}")
def mensaje_final():
    print("Fin del programa")

i = 0
while i < num:
    nombre = input("Ingrese el nombre: ")
    curso = input("Ingrese el curso: ")
    informacion(nombre, curso)
    i = i+1

mensaje_final()
