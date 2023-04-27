class Monticulo(object):

    def __init__(self, size):
        self.size = 0
        self.lista = [None] * size

    def agregar(self, valor):
        self.lista[self.size] = valor
        self.size += 1
        self.flotar(self.size - 1)

    def flotar(self, indice):
        padre = (indice - 1) // 2
        if indice > 0 and self.lista[indice] > self.lista[padre]:
            self.lista[indice], self.lista[padre] = self.lista[padre], self.lista[indice]
            self.flotar(padre)

    def extraer(self):
        valor = self.lista[0]
        self.size -= 1
        self.lista[0] = self.lista[self.size]
        self.hundir(0)
        return valor
    
    def hundir(self, indice):
        izq = 2 * indice + 1
        der = 2 * indice + 2
        mayor = indice
        if izq < self.size and self.lista[izq] > self.lista[mayor]:
            mayor = izq
        if der < self.size and self.lista[der] > self.lista[mayor]:
            mayor = der
        if mayor != indice:
            self.lista[indice], self.lista[mayor] = self.lista[mayor], self.lista[indice]
            self.hundir(mayor)

    def vacio(self):
        return self.size == 0
    
    def arrive(self, valor, prioridad):
        self.agregar([prioridad, valor])

    def atencion(self):
        return self.extraer()[1]
    
    def cambio_index(self, index1, index2):
        self.lista[index1], self.lista[index2] = self.lista[index2], self.lista[index1]


class NodoPila(object):
    
        def __init__(self):
            self.valor = None
            self.sig = None


class Pila(object):

    def __init__(self):
        self.cima = None
        self.size = 0

    def apilar(self, data):
        nodo = NodoPila()
        nodo.valor = data
        nodo.sig = self.cima
        self.cima = nodo
        self.size += 1

    def desapilar(self):
        x = self.cima.valor
        self.cima = self.cima.sig
        self.size -= 1
        return x
    
    def pila_vacia(self):
        return self.cima == None

def prio(pedido):
    if pedido[0] == "Gran Conquistador" or pedido[1] == "616" or pedido[2] == "El que permanece":
        return 1
    elif pedido[0] == "Khan que todo lo sabe" or pedido[1] == "838" or pedido[2] == "Carnicero de Dioses":
        return 2
    else:
        return 3
    
def procesador(pedidos):
    cola = Monticulo(100)
    pila = Pila()
    for i in pedidos:
        cola.arrive(i, prio(i))
    while not cola.vacio():
        pila.apilar(cola.atencion())
    return pila

def main():
    
    pedido1 = ("Gran Conquistador", "616", "El que permanece")
    pedido2 = ("Khan que todo lo sabe", "838", "Carnicero de Dioses")
    pedido3 = ("Capitan America", "616", "Escudo de Vibranium")
    pedido4 = ("Iron Man", "1610", "Colisionador de hadrones")
    pedido5 = ("Adam Warlock", "12041", "Gema del alma")

    pedidos = [pedido1, pedido2, pedido3, pedido4, pedido5]

    bitacora = procesador(pedidos)

    print("Pedidos efectuados: \n")
    while not bitacora.pila_vacia():
        print(bitacora.desapilar())

if __name__ == "__main__":
    main()
