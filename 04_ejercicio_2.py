menu = {            "(1)": "Añadir empleado",
                     "(2)": "Borrar empleado",
                     "(3)": "Mostrar lista empleados",
                     "(4)": "Mostrar detalle de un empleado",
                     "(5)": "Mostrar empleados cumpleaños",
                     "(6)": "Terminar"}


lista = ['Nombre:','NIF:','Fecha nacimiento:','Tipo:', 'Año de alta:', 'Sueldo base:','Complemento anual:']

empleados = {
            '32.234.234M': ('Pedro Rodríguez Martínez','32.234.234M','12/05/1985','fijo','2010','2000','200'),
            '32.234.234V': ('José Martínez','32.234.234M','25/04/1995','temporal','2002','1800','400'),
            '32.234.234X': ('Maria Angel','32.234.234M','24/03/1995','fijo','1999','1800','400')
             }

        


class Empleado:
    """Clase que implementa una lista con algunos métodos adicionales."""
    def __init__(self, NIF,nombre,tipo_empleado,fecha_nacimiento,sueldo_mensual,ano_alta,complemento_anual):
        """Inicializa una lista chachi con un mensaje descriptivo."""
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

def menu_opciones():    
    print(" Menú de opciones")
    for clave in menu:
        print(clave, menu[clave])        
    opc = int(input("Elige una opción: "))
    opc2 = str(opc)
    opc3 = str("(" + opc2 + ")")    
    while not opc3 in menu:
        print("Error, esta opción no existe.")
        opc = int(input("Elige una opción: "))
        opc2 = str(opc)
        opc3 = str("(" + opc2 + ")")        
    return opc

def switch(case):    
   if case == 1:
       anadir_empleado_1()
   
   elif case == 2:
       borrar_empleado_2()

   elif case == 3:
       listar_empleado_3()

   elif case == 4:
       mostrar_empleado_4()      

   elif case == 5:
       empleado_cumple5()


def anadir_empleado_1():
    print("Introduce los datos del empleado:")    
    tipo_empleado = str(input("Tipo de empleado: "))
    nombre = str(input("Introduce el nombre: "))
    NIF = str(input("Introduce el nif: "))
    fecha_nacimiento = str(input("Introduce la fecha de nacimiento(dd/mm/aaaa): "))

    if (tipo_empleado == 'fijo'):           
        sueldo_base_mensual = float(input("Introduce el sueldo base mensual: "))
        ano_alta = int(input("Introduce el año de alta en la empresa: "))
        complemento_anual = float(input("Introduce el complemento anual: "))
        
    if (tipo_empleado == 'temporal'):
        sueldo_base_mensual = float(input("Introduce el sueldo mensual: "))
        fecha_alta = str(input("Introduce la fecha de alta (dd/mm/aaaa): "))
        fecha_baja = str(input("Introduce la fecha de baja (dd/mm/aaaa): "))
        
    persona1 = Empleado(NIF,nombre,tipo_empleado,fecha_nacimiento,sueldo_base_mensual,ano_alta,complemento_anual)
    persona1.ANADIR()
    print(".")

def borrar_empleado_2():
    NIF = input("Introduce el nif del empleado que quieres borrar: ")
    while not NIF in empleados:        
        NIF = input("No existe este NIF, introduce el NIF correcto: ")
    del empleados[NIF]
    print(".")

def listar_empleado_3():
    print("")
    for clave in empleados:
        print(clave, empleados[clave][0],"-",empleados[clave][3])
    print(".")

def mostrar_empleado_4():
    NIF = str(input("Introduce el nif del empleado: "))
    print("")
    e = 0
    for x in lista:
        print(x,empleados[NIF][e])
        e = e + 1    
    print(".")

def empleado_cumple5():
    mes = int(input("Introduce un mes (1 - 12): "))
    print("")
    print("Estan de cumpleaños:")
    for clave in empleados:
        txt = empleados[clave][2]
        x = txt.split("/")
        x = int(x[1])
        if (x == mes):
            print(empleados[clave][0],empleados[clave][2])            
    print(".")

def main():         

    loop = 0
    while loop != 6:
        opcion = menu_opciones()
        switch(opcion)        
        loop = opcion
    
if __name__ == "__main__":
    main()




