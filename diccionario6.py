persona = {}
continuar = True
while continuar:
    clave = input("Que dato quieres introducir?")
    valor = input(clave + ":")
    persona[clave] = valor
    print(persona)
    continuar = input("Quieres añadir mas informacion? (S/N)") =="S"