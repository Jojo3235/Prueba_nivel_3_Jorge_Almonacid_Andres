from operaciones import *

def main():
    a, b, c, d = (10, 5, 0, "Hola")
    operador = Operadores(a)
    print( "{} + {} = {}".format(a, b, operador.suma(b) ) )
    print( "{} - {} = {}".format(b, d, operador.resta(d) ) )
    print( "{} * {} = {}".format(b, b, operador.producto(b) ) )
    print( "{} / {} = {}".format(a, c, operador.division(c) ) )

if __name__ == "__main__":
    main()