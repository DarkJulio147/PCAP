def read_int(prompt, min, max):
    si = False
    while not si:
        try:
            val = int(input(prompt))
            si = True
            if si:
                si = val >= min and val <= max
            else:           
                print("El valor no esta dentro del rango permitido")
        except ValueError:
            print("Error")
    return val
num = read_int("Ingresa un número entre -10 a 10: ", -10, 10)
print("El número es:", num)
    