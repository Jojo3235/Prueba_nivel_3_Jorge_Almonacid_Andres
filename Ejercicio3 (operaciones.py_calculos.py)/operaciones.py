# Crea el siguiente módulo:

# El módulo se denominará operaciones.py y contendrá 4 funciones para realizar una suma, una resta, un producto y una division entres dos números. Todas ellas devolverán el resultado.
# En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:
# TypeError: En caso de que se envíen valores a las funciones que no sean números. Además deberá aparecer un mensaje que informe Error: Tipo de dato no válido.
# ZeroDivisionError: En caso de realizar una división por cero. Además deberá aparecer un mensaje que informe Error: No es posible dividir entre cero.
# Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás importar el módulo y realizar las siguientes instrucciones. Observa si el comportamiento es el esperado:

# from operaciones import *

 

# a, b, c, d = (10, 5, 0, "Hola")

 

# print( "{} + {} = {}".format(a, b, suma(a, b) ) )

# print( "{} - {} = {}".format(b, d, resta(b, d) ) )

# print( "{} * {} = {}".format(b, b, producto(b, b) ) )

# print( "{} / {} = {}".format(a, c, division(a, c) ) )


class Operadores(object):

    def __init__(self, numero):
        self.numero = numero if isinstance(numero, int) or isinstance(numero, float) else None

    def suma(self, numero):
        if isinstance(numero, int) or isinstance(numero, float):
            return self.numero + numero
        else:
            return "Error: Tipo de dato no válido."
        
    def resta(self, numero):
        if isinstance(numero, int) or isinstance(numero, float):
            return self.numero - numero
        else:
            return "Error: Tipo de dato no válido."
        
    def producto(self, numero):
        if isinstance(numero, int) or isinstance(numero, float):
            return self.numero * numero
        else:
            return "Error: Tipo de dato no válido."
        
    def division(self, numero):
        if isinstance(numero, int) or isinstance(numero, float):
            if numero != 0:
                return self.numero / numero
            else:
                return "Error: No es posible dividir entre cero."
        else:
            return "Error: Tipo de dato no válido."
    