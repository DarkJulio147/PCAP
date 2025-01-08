palabra = input("Ingresa la palabra que deseas encontrar: ").upper()
grupo = input("Ingresa la cadena en donde deseas buscar: ").upper()

found = True
start = 0

for ch in palabra:
	pos = grupo.find(c, posicion) 
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Si")
else:
	print("No")