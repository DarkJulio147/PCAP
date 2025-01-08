nombre = input("Introduzca Su Nombre: ")
edad = input("Introduzca su edad: ")
direccion = input("Introduzca su direccion: ")
telefono = input("Introduzca su telefono: ")

diccionario = {"nombre":nombre , "edad": edad, "direccion": direccion, "telefono": telefono}

print(diccionario["nombre"], "tiene", diccionario["edad"], "años", "vive en", diccionario["direccion"], "y su numero de telefono es", diccionario["telefono"])