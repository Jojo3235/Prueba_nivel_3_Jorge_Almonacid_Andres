# Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de cartas de baraja española–,resolver las siguientes actividades:

#  generar las cartas del mazo de forma aleatoria;
#  separar la pila mazo en cuatro pilas una por cada palo;
#  ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente

import random


class NodoPila(object):
    
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox


class Pila(object):

    def __init__(self, tope=None):
        self.tope = tope

    def apilar(self, dato):
        nuevo = NodoPila(dato)
        nuevo.prox = self.tope
        self.tope = nuevo

    def desapilar(self):
        if self.tope is not None:
            aux = self.tope.dato
            self.tope = self.tope.prox
            return aux


class NodoLista(object):
    
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox


class Lista(object):

    def __init__(self, inicio=None):
        self.inicio = inicio

    def insertar(self, dato, pos=None):
        nuevo = NodoLista(dato)
        if pos is None or pos == 0:
            nuevo.prox = self.inicio
            self.inicio = nuevo
        else:
            anterior = self.buscar(pos-1)
            nuevo.prox = anterior.prox
            anterior.prox = nuevo

    def buscar(self, pos):
        aux = self.inicio
        for i in range(pos):
            if aux is None:
                break
            aux = aux.prox
        return aux
    
    def barrido(self):
        aux = self.inicio
        while aux is not None:
            print(aux.dato)
            aux = aux.prox

    def eliminar(self, pos=None):
        if pos is None:
            pos = self.tamanio()-1
        if self.inicio is not None:
            if pos == 0:
                self.inicio = self.inicio.prox
            else:
                anterior = self.buscar(pos-1)
                if anterior.prox is not None:
                    anterior.prox = anterior.prox.prox

    def tamanio(self):
        cont = 0
        aux = self.inicio
        while aux is not None:
            cont += 1
            aux = aux.prox
        return cont
    

class Carta(object):
    
    def __init__(self, numero=None, palo=None):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        return str(self.numero) + " de " + str(self.palo)
    

class Mazo(object):

    def __init__(self, cartas=None):
        self.cartas = cartas

    def generar(self):
        self.cartas = Lista()
        for i in range(1, 13):
            for j in range(1, 5):
                if j == 1:
                    self.cartas.insertar(Carta(i, "Espada"))
                elif j == 2:
                    self.cartas.insertar(Carta(i, "Basto"))
                elif j == 3:
                    self.cartas.insertar(Carta(i, "Copa"))
                else:
                    self.cartas.insertar(Carta(i, "Oro"))
        for i in range(self.cartas.tamanio()):
            pos1 = random.randint(0, self.cartas.tamanio()-1)
            pos2 = random.randint(0, self.cartas.tamanio()-1)
            aux1 = self.cartas.buscar(pos1).dato
            aux2 = self.cartas.buscar(pos2).dato
            self.cartas.insertar(aux1, pos2)
            self.cartas.insertar(aux2, pos1)
            self.cartas.eliminar(pos1+1)
            self.cartas.eliminar(pos2+1)

    def agrupar_por_palo(self):
        espada = Lista()
        basto = Lista()
        copa = Lista()
        oro = Lista()
        aux = self.cartas.inicio
        while aux is not None:
            if aux.dato.palo == "Espada":
                espada.insertar(aux.dato)
            elif aux.dato.palo == "Basto":
                basto.insertar(aux.dato)
            elif aux.dato.palo == "Copa":
                copa.insertar(aux.dato)
            else:
                oro.insertar(aux.dato)
            aux = aux.prox
        return espada, basto, copa, oro

    def ordenar_palo_creciente(self, palo):
        aux = self
        for i in range(1, aux.palos[palo].tamanio()):
            for j in range(0, aux.palos[palo].tamanio()-i):
                if aux.palos[palo].buscar(j).dato.numero > aux.palos[palo].buscar(j+1).dato.numero:
                    aux.palos[palo].insertar(aux.palos[palo].buscar(j).dato, j+2)
                    aux.palos[palo].eliminar(j)
        return aux.palos[palo]

    def __str__(self):
        aux = self.cartas.inicio
        while aux is not None:
            print(aux.dato)
            aux = aux.prox
        return ""

    

def pedir_numero(mensaje, min, max):
    numero = int(input(mensaje))
    while numero < min or numero > max:
        numero = int(input(mensaje))
    return numero


def main():
    mazo = Mazo()
    mazo.generar()
    print(mazo)
    mazo.palos = mazo.agrupar_por_palo()
    print("Espada:")
    mazo.palos[0].barrido()
    print("Basto:")
    mazo.palos[1].barrido()
    print("Copa:")
    mazo.palos[2].barrido()
    print("Oro:")
    mazo.palos[3].barrido()
    palo = pedir_numero("Ingrese el palo que desea ordenar (Espada -> 0, Basto -> 1, Copa -> 2, Oro -> 3): ", 0, 3)
    print("Palo ordenado:")
    mazo.ordenar_palo_creciente(palo).barrido()
    # print("Espada ordenada:")
    # mazo.ordenar_palo_creciente(0).barrido()
    # print("Basto ordenada:")
    # mazo.ordenar_palo_creciente(1).barrido()
    # print("Copa ordenada:")
    # mazo.ordenar_palo_creciente(2).barrido()
    # print("Oro ordenada:")
    # mazo.ordenar_palo_creciente(3).barrido()
  

if __name__ == "__main__":
    main()