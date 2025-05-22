class Nodo:
    def __init__(self, nom):
        self.nom = nom
        self.izq = None
        self.der = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def vacio(self):
        return self.raiz is None

    def buscar_Nodo(self, nom):
        return self._buscar_NodoRec(self.raiz, nom)

    def _buscar_NodoRec(self, nodo, nom):
        if nodo is None or nodo.nom == nom:
            return nodo

        if nom < nodo.nom:
            return self._buscar_NodoRec(nodo.izq, nom)
        else:
            return self._buscar_NodoRec(nodo.der, nom)

    def insertar(self, nom):
        if self.vacio():
            self.raiz = Nodo(nom)
        else:
            self._insertar_Rec(self.raiz, nom)

    def _insertar_Rec(self, nodo, nom):
        if nom < nodo.nom:
            if nodo.izq is None:
                nodo.izq = Nodo(nom)
            else:
                self._insertar_Rec(nodo.izq, nom)
        elif nom > nodo.nom:
            if nodo.der is None:
                nodo.der = Nodo(nom)
            else:
                self._insertar_Rec(nodo.der, nom)

arbol = Arbol()
arbol.insertar("Miguel")
arbol.insertar("Mario")
arbol.insertar("Karen")
arbol.insertar("Lucia")
arbol.insertar("Marcos")
arbol.insertar("Zara")

nodo = arbol.buscarNodo("Miguel")
if nodo:
    print(f"Nodo Encontrado = {nodo.nom}")
else:
    print("Nodo No Encontrado")

print(f"¿El Árbol No Tiene Nodos? {arbol.vacio()}")
