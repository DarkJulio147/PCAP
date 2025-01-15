class Empleado:
    def __init__(self, nombre, apellidos, cargo, salario = 1000):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.__salario = salario
    def get_salario(self):
        return self.__salario
    def __str__(self):
        return f"{self.nombre} ({self.cargo}) gana: {round(self.get_salario)}"
    
listaEmpleados = [
    Empleado("Julio", "Gutierrez", "200", 10000000),
    Empleado("Iñigo", "Ramon", "100", 10000),
    Empleado("Sergio", "lopez", "34", 100000),
    Empleado("Betsbo", "BETBBERANTARA", "2900", 1530),
    Empleado("blowjob", "petterBETSBO", "10", 900000)
]

empleados_vip= [empleado for empleado in listaEmpleados if empleado.getsalario() > 50000]
print(empleado1.apellidos)
  