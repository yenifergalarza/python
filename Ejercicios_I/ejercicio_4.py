Notas = [
    {"codigo": "1", "nombre": "Juan Perez", "PC1": 15, "PC2": 14, "PC3": 17, "PC4": 11, "EF": 12, "EP": 13},
    {"codigo": "2", "nombre": "Lucia Rodriguez", "PC1": 17, "PC2": 18, "PC3": 18, "PC4": 6, "EF": 12, "EP": 12},
    {"codigo": "3", "nombre": "Ana Molina", "PC1": 12, "PC2": 19, "PC3": 17, "PC4": 11, "EF": 11, "EP": 15},
    {"codigo": "4", "nombre": "Pedro Santana", "PC1": 9, "PC2": 12, "PC3": 11, "PC4": 12, "EF": 15, "EP": 12},
    {"codigo": "5", "nombre": "Raul Paz", "PC1": 14, "PC2": 15, "PC3": 12, "PC4": 10, "EF": 12, "EP": 15},
    {"codigo": "6", "nombre": "Michael Barzola", "PC1": 11, "PC2": 11, "PC3": 8, "PC4": 19, "EF": 14, "EP": 11},

    {"codigo": "7", "nombre": "Andrea Suarez", "PC1": 12, "PC2": 16, "PC3": 5, "PC4": 12, "EF": 13, "EP": 19},
]

for alumnos in Notas:
    PC1 = alumnos["PC1"]
    PC2 = alumnos["PC2"]
    PC3 = alumnos["PC3"]
    PC4 = alumnos["PC4"]
    EF = alumnos["EF"]
    EP = alumnos["EP"]
    promedioFinal = (((PC1 + PC2 + PC3 + PC4) / 4) + EP + EF) / 3

    if (promedioFinal >= 12):
        alumnos["condicion"] = "aprobado"
    else:
        alumnos["condicion"] = "desaprobado"
    print alumnos
