from random import random
from math import ceil, floor


class NodoLista(object):

    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

    def __str__(self):
        return "{} -> {}".format(self.valor, self.siguiente)
    

class ListaEnlazada(object):

    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = NodoLista(val)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.siguiente is not None:
                current_node = current_node.siguiente
            current_node.siguiente = new_node

    def get(self, index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.siguiente
        return current_node.valor

    def set(self, index, val):
        current_node = self.head
        for i in range(index):
            current_node = current_node.siguiente
        current_node.val = val

    def remove(self, index):
        if index == 0:
            self.head = self.head.siguiente
        else:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.siguiente
            current_node.siguiente = current_node.siguiente.siguiente

    def insert_at(self, index, val):
        new_node = NodoLista(val)
        if index == 0:
            new_node.siguiente = self.head
            self.head = new_node
        else:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.siguiente
            new_node.siguiente = current_node.siguiente
            current_node.siguiente = new_node

    def index_of(self, val):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.valor == val:
                return index
            current_node = current_node.siguiente
            index += 1
        return -1
    
    def contains(self, val):
        return self.index_of(val) != -1

    def __str__(self):
        current_node = self.head
        values = []
        while current_node is not None:
            values.append(current_node.valor)
            current_node = current_node.siguiente
        return str(values)
    

def leer_numero(ini, fin, mensaje):
    
    while True:
        try:
            valor = int(input(mensaje))
        except:
            print("Debes introducir un número")
        else:
            if valor >= ini and valor <= fin:
                return valor
            else:
                print("El número debe estar entre {} y {}".format(ini, fin))


def generador():

    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

    lista = ListaEnlazada()

    for i in range(numeros):
        lista.insert(random() * 100)

    for i in range(numeros):
        numero = lista.get(i)
        if modo == 1:
            print("{} => {}".format(numero, ceil(numero)))
        elif modo == 2:
            print("{} => {}".format(numero, floor(numero)))
        else:
            print("{} => {}".format(numero, round(numero)))

    return lista


def main():
    generador()


if __name__ == "__main__":
    main()