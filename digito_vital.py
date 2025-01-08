fecha = ''

while True:
    fecha = input("Introduce tu fecha de nacimiento (en formato AAAAMMDD): ")
    if fecha.isnumeric():
        break
    print("Debes introducir una fecha en formato AAAMMDD.")

digito = 0
suma = 0

for c in fecha:
    suma += int(c)

if len(str(suma)) >1:
    for c in str(suma):
        digito += int(c)
else: digito = suma

print("tu digito vital es:", digito)
