frase = input("introduce una frase: ")

frase2 = (frase.lower()).replace('','')
if frase2 == frase2.upper() == frase2[::-1].upper():
	print("Es un palíndromo")
else:
	print("No es un palíndromo")