estudiantes = [
    "Ana", "Luis", "María", "Carlos",
    "Sofía", "Mateo", "Daniela", "Pedro",
    "Valeria", "José", "Camila", "Andrés"
]

contador = 0

for fila in range(1, 4):
    for puesto in range(1, 5):
        print(f"Fila {fila} - Puesto {puesto}: {estudiantes[contador]}")
        contador = contador + 1