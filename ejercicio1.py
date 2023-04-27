AFIRMATIVO = ["si", "yes", "s", "y"]
NEGATIVO = ["no", "not", "n"]

class NodoArbol(object):

    def __init__(self, valor, izd=None, dch=None):
        self.valor = valor
        self.izd = izd
        self.dch = dch


class Superheroe(object):

    def __init__(self, nombre, fortaleza):
        self.nombre = nombre
        self.fortaleza = fortaleza

    def __str__(self):
        return self.nombre
    

class Arbol(object):

    def __init__(self, arbol):
        self.arbol = arbol
    
    def asignar(self):
        nodo_actual = self.arbol
        while nodo_actual.izd != None:
            if isinstance(nodo_actual.valor, Superheroe):
                return nodo_actual.valor
            else:
                respuesta = input(f"{nodo_actual.valor} (s/n): ")
                if respuesta.lower() in AFIRMATIVO:
                    nodo_actual = nodo_actual.izd
                elif respuesta.lower() in NEGATIVO:
                    nodo_actual = nodo_actual.dch
                else:
                    print("Respuesta no válida")
        return nodo_actual.valor
    

def main():
    kang = Superheroe("Kang", "misiones intergalácticas en equipo") #intergalactica
    antman = Superheroe("Ant Man", "misiones de recuperación donde sea necesario no se detectado")#recuperacion
    hulk = Superheroe("Hulk", "misiones de destrucción")#destruccion
    capi = Superheroe("Capitán América", "misiones de defensa y de recuperación")#defensa y recuperacion
    capitana_marvel = Superheroe("Capitana Marvel", "viajar por las distintas galaxias")#intergalactica
    kang_2 = Superheroe("Kang", "es muy hábil y puede ser muy útil para varias misiones")#varias misiones
    winter_soldier = Superheroe("The Winter Soldier", "misiones de recuperación donde requiera infiltrarse con personas del lugar")#recuperacion
    iron_man = Superheroe("Iron Man", "planear misiones de defensa, además es un genio y domina el manejo de tecnología avanzada, cuenta con un traje muy poderoso")#defensa
    nick_fury = Superheroe("Nick Fury", "elegir cuál será la próxima acción para tomar y moverse rápidamente de un lugar a otro")#decision
    thor = Superheroe("Thor", "destruir ejércitos completos")#destruccion
    super_nadie = Superheroe("Súper Nadie", "no es nadie, lo sentimos, tu misión no podrá ser completada con nuestra plantilla actual, pruebe en otro universo")

    raiz = NodoArbol("¿Son varias misiones?")
    raiz.izd = NodoArbol(kang_2)
    raiz.dch = NodoArbol("¿Es una misión intergaláctica?")
    raiz.dch.izd = NodoArbol("¿Es una misión de equipo?")
    raiz.dch.dch = NodoArbol("¿Es una misión de recuperación?")
    raiz.dch.izd.izd = NodoArbol(kang)
    raiz.dch.izd.dch = NodoArbol(capitana_marvel)
    raiz.dch.dch.izd = NodoArbol("¿Es una misión de infiltración?")
    raiz.dch.dch.dch = NodoArbol("¿Es una misión de destrucción?")
    raiz.dch.dch.izd.izd = NodoArbol("¿Es necesario no ser detecatado?")
    raiz.dch.dch.izd.dch = NodoArbol("¿Es una misión de defensa?")
    raiz.dch.dch.dch.izd = NodoArbol("¿Hay que aniquilar ejércitos completos?")
    raiz.dch.dch.dch.dch = NodoArbol("¿Es una misión de defensa?")
    raiz.dch.dch.izd.izd.izd = NodoArbol(antman)
    raiz.dch.dch.izd.izd.dch = NodoArbol("¿Es además de defensa")
    raiz.dch.dch.izd.izd.dch.izd = NodoArbol(capi)
    raiz.dch.dch.izd.izd.dch.dch = NodoArbol(winter_soldier)
    raiz.dch.dch.izd.dch.izd = NodoArbol("¿Se necesita tecnología?")
    raiz.dch.dch.izd.dch.dch = NodoArbol(super_nadie)
    raiz.dch.dch.izd.dch.izd.izd = NodoArbol(iron_man)
    raiz.dch.dch.izd.dch.izd.dch = NodoArbol(capi)
    raiz.dch.dch.dch.izd.izd = NodoArbol(thor)
    raiz.dch.dch.dch.izd.dch = NodoArbol(hulk)
    raiz.dch.dch.dch.dch.izd = NodoArbol("¿Se necesita tecnología?")
    raiz.dch.dch.dch.dch.dch = NodoArbol("¿Es una misión de decisión?")
    raiz.dch.dch.dch.dch.izd.izd = NodoArbol(iron_man)
    raiz.dch.dch.dch.dch.izd.dch = NodoArbol(capi)
    raiz.dch.dch.dch.dch.dch.izd = NodoArbol(nick_fury)
    raiz.dch.dch.dch.dch.dch.dch = NodoArbol(super_nadie)

    arbol = Arbol(raiz)
    superheroe = arbol.asignar()
    print(f"\nSuperhéroe seleccionado:. {superheroe}\nFortaleza: {superheroe.fortaleza}")

if __name__ == "__main__":
    main()