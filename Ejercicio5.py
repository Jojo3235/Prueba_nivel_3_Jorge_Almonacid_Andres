# Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea- toria– que resuelva las siguientes actividades:

 

# realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
#  determinar si un número está cargado en el árbol o no;
#  eliminar tres valores del árbol;
#  determinar la altura del subárbol izquierdo y del subárbol derecho;
#  determinar la cantidad de ocurrencias de un elemento en el árbol;

import random

class nodoCola(object):
    info, sig = None, None

class Cola(object):
    def __init__(self):
        self.frente = None
        self.final = None
        self.size = 0

    def arribo(cola, dato):
        nodo = nodoCola()
        nodo.info = dato
        if cola.frente is None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
        cola.size += 1

    def atencion(cola):
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        if cola.frente is None:
            cola.final = None
        cola.size -= 1
        return dato
    
    def cola_vacia(cola):
        return cola.frente is None
    
    def en_frente(cola):
        return cola.frente.info
    
    def size(cola):
        return cola.size
    
    def mover_al_final(cola):
        dato = Cola.atencion(cola)
        Cola.arribo(cola, dato)
        return dato
    
    def barrido(cola):
        i = 0
        while i < Cola.size(cola):
            dato = Cola.mover_al_final(cola)
            print(dato)
            i += 1

    def vaciar_cola(cola):
        for i in range(Cola.size(cola)):
            Cola.atencion(cola)
        return cola


class Arbol(object):#aumentar la altura de los nodos a medida que se añade un nuevo nivel

    def __init__(self, info):
        self.izd = None
        self.dch = None
        self.info = info
        self.altura_izd = 0
        self.altura_dch = 0

    def insertar(self, dato):
        if self.info == dato:
            print("El dato ya existe en el árbol")
        elif self.info > dato:
            if self.izd is None:
                self.izd = Arbol(dato)
            else:
                self.izd.insertar(dato)
        else:
            if self.dch is None:
                self.dch = Arbol(dato)
            else:
                self.dch.insertar(dato)
        
    def inorden(self):
        if self is not None:
            if self.izd is not None:
                self.izd.inorden()
            print(self.info)
            if self.dch is not None:
                self.dch.inorden()

    def preorden(self):
        if self is not None:
            print(self.info)
            if self.izd is not None:
                self.izd.preorden()
            if self.dch is not None:
                self.dch.preorden()

    def postorden(self):
        if self is not None:
            if self.izd is not None:
                self.izd.postorden()
            if self.dch is not None:
                self.dch.postorden()
            print(self.info)
    
    def por_nivel(self):
        cola = Cola()
        cola.arribo(self)
        while not cola.cola_vacia():
            nodo = cola.atencion()
            print(nodo.info)
            if nodo.izd is not None:
                cola.arribo(nodo.izd)
            if nodo.dch is not None:
                cola.arribo(nodo.dch)

    def busqueda(self, buscado):
        if self.info == buscado:
            return True
        elif self.info > buscado and self.izd is not None:
            return self.izd.busqueda(buscado)
        elif self.info < buscado and self.dch is not None:
            return self.dch.busqueda(buscado)
        return False
    
    def eliminar_tres(self, dato1, dato2, dato3):
        if self is not None:
            if self.izd is not None:
                if self.izd.info == dato1 or self.izd.info == dato2 or self.izd.info == dato3:
                    self.izd = None
                else:
                    self.izd.eliminar_tres(dato1, dato2, dato3)
            if self.dch is not None:
                if self.dch.info == dato1 or self.dch.info == dato2 or self.dch.info == dato3:
                    self.dch = None
                else:
                    self.dch.eliminar_tres(dato1, dato2, dato3)

    def altura_izd_dch(self):
        if self is not None:
            if self.izd is not None:
                self.altura_izd = self.izd.altura_izd_dch()[0] + 1
            if self.dch is not None:
                self.altura_dch = self.dch.altura_izd_dch()[1] + 1
        return self.altura_izd, self.altura_dch


    def numero_ocurrencias(self, buscado):
        if self is not None:
            if self.info == buscado:
                return 1
            elif self.info > buscado and self.izd is not None:
                return self.izd.numero_ocurrencias(buscado)
            elif self.info < buscado and self.dch is not None:
                return self.dch.numero_ocurrencias(buscado)
        return 0
    
def contar_pares_impares(arbol):
    pares = impares = 0
    if arbol is not None:
        if arbol.info % 2 == 0:
            pares = 1
        else:
            impares = 1
        pares_izq, impares_izq = contar_pares_impares(arbol.izd)
        pares_der, impares_der = contar_pares_impares(arbol.dch)
        pares += pares_izq + pares_der
        impares += impares_izq + impares_der
    return pares, impares

        
    

def main():
    #insertar mediante random.randint
    arbol = Arbol(1750000/2)
    for i in range(500):
        arbol.insertar(random.randint(0, 1750000/2))
    for i in range(500):
        arbol.insertar(random.randint(1750000/2, 1750000))
    arbol.inorden()
    print()
    arbol.preorden()
    print()
    arbol.postorden()
    print()
    arbol.por_nivel()
    print()
    print(f"¿Esta cargado el numero 50?: {arbol.busqueda(50)}")
    print(f"¿Esta cargado el numero 100?: {arbol.busqueda(100)}")
    print(f"¿Esta cargado el numero 1000?: {arbol.busqueda(1000)}")

    #eliminar tres nodos
    arbol.eliminar_tres(1, 2, 3)
    
    #altura de subarbol izquierdo y derecho
    print(f"Altura subarbol izquierdo: {arbol.altura_izd_dch()[0]}\nAltura subarbol derecho: {arbol.altura_izd_dch()[1]}")

    #numero de ocurrencias
    s = random.randint(0, 1750000)
    print(f"Número de veces que aparece {s} en el árbol: {arbol.numero_ocurrencias(s)}")

    #contar nodos pares e impares
    print(f"Números pares: {contar_pares_impares(arbol)[0]}\nNúmeros impares: {contar_pares_impares(arbol)[1]}")

if __name__ == "__main__":
    main()
