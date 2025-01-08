fruta = {"Mandarina": 2, "Platanillo": 3, "Berenjenazo": 29}

print("Mandarina")
print("Platanillo")
print("Berenjenazo")
frutas = input("Eliga una fruta")
kilos = input("Introduzca los kilos")

if frutas in fruta:
    print(kilos, "kilos de", fruta, "valen", fruta[frutas]*kilos, "€")
else:
    print("no hay frutas")
