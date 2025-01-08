meses = {
    "01": "enero",
    "02": "febrero",
    "03": "marzo",
    "04": "abril",
    "05": "mayo",
    "06": "junio",
    "07": "julio",
    "08": "agosto",
    "09": "septiembre",
    "10": "octubre",
    "11": "noviembre",
    "12": "diciembre"
}
fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")
dia, mes, anio = fecha.split("/")
nombre_mes = meses.get(mes, "Mes inválido")
if nombre_mes != "Mes inválido":
    print(f"{dia} de {nombre_mes} de {anio}")
else:
    print("El mes ingresado no es válido. Por favor, revisa el formato.")
