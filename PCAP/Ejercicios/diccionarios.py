diccionario = {'euro':'€', 'Dollar':'$', 'Yen': 'y'}
print("-----------")
print("1º Euro")
print("2º Dollar")
print("1º Yen")
print("-----------")
im = input("Seleccione el metodo pago")


match im:
    case "1":
        print("Escogiste Euro",diccionario["euro"])
    case "2":
        print("Escogiste Dollar",diccionario["Dollar"])
    case "3":
        print("Escogiste Yen",diccionario["Yen"])
    case _:
        print("El metodo de pago no esta en nuestra pagina")