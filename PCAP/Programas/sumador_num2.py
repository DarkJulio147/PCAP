#Procesador de Números.
from imprime_pares import imprime_pares as impp
line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print("Error" + substr + "no es un numero.")

impp(strings)