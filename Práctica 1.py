nota_final = float(input("Ingrese la nota final del estudiante: "))
asistencia = float(input("Ingrese el porcentaje de asistencia del estudiante: "))
tareas = input("¿El estudiante entregó todas las tareas? (sí/no): ")

if nota_final >= 8:
    if asistencia >= 80:
        if tareas == "sí":
            print("El estudiante aprobó con honores.")
        if tareas != "si":
            print("El estudiante aprobó.")
    if asistencia < 80:
        if tareas == "sí":
            print("El estudiante aprobó, pero con asistencia insuficiente.")
        if tareas != "sí":
            print("El estudiante aprobó, pero con asistencia insuficiente.")
if nota_final < 8:
    if asistencia >= 80:
        if tareas == "sí":
            print("El estudiante aprobó, pero con nota insuficiente.")
        if tareas != "sí":
            print("El estudiante aprobó, pero con nota insuficiente.")
    if asistencia < 80:
        if tareas == "sí":
            print("El estudiante reprobó por nota y asistencia insuficientes.")
        if tareas != "sí":
            print("El estudiante reprobó por nota y asistencia insuficientes.")