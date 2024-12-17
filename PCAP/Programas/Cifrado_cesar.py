# Ingresa el texto a encriptar.
text = input("Ingresa un mensaje: ")

# Ingresar un valor de cambio válido (repitelo hasta que tengas éxito).
shift = 0

while shift == 0:
    try:    
        shift = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("¡Valor de cambio inválido!")

cipher = ''

for char in text:
    # ¿Es un letra?
    if char.isalpha():
        # Cambia su código.
        code = ord(char) + shift
        # Encontrar el código de la primera letra (mayúscula o minúscula).
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Realizar corrección.
        code -= first
        code %= 26
        # Agregar carácter codificado al mensaje.
        cipher += chr(first + code)
    else:
        # Agregar carácter original al mensaje.
        cipher += char

print(cipher)
    