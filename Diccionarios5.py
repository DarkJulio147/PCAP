diccionariof = {"Matematicas": 6, "Fisica": 4, "Quimica": 5}
total_creditos = 0

for asignatura, creditos in diccionariof.items():
    print(asignatura, "tiene", creditos, "creditos")
    total_creditos += creditos

print("Numero total de creditos del curso: ", total_creditos)