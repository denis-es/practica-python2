

class Empleado:
    """ DEFINE LA CLASS EMPLEADO"""
    def __init__(self, NIF,nombre,tipo_empleado,fecha_nacimiento,sueldo_mensual,ano_alta,complemento_anual):
        """Inicializa """
        self.NIF = NIF
        self.nombre = nombre
        self.tipo_empleado = tipo_empleado
        self.fecha_nacimiento = fecha_nacimiento
        self.sueldo_mensual = sueldo_mensual
        self.ano_alta = ano_alta
        self.complemento_anual = complemento_anual

    def ANADIR(self):
        empleados[self.NIF] = (self.nombre,self.NIF,self.fecha_nacimiento,self.tipo_empleado,self.ano_alta,self.sueldo_mensual,self.complemento_anual)

    def Exibir(self):
        print(self.nombre,self.fecha_nacimiento,self.sueldo_mensual)

