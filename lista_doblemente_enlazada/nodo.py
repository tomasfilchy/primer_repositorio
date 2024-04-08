class Nodo:
    def __init__(self, dato, dato_anterior=None, dato_siguiente=None) :
        self.dato = dato
        self.asignar_siguiente(dato_siguiente)
        self.asignar_anterior(dato_anterior)
    def asignar_siguiente(self, nodo_siguiente):
        self.siguiente = nodo_siguiente
    def asignar_anterior(self, nodo_anterior):
        self.anterior = nodo_anterior
    def mostrarNodo(self):
        return self.dato
nodo1 = Nodo(dato=5)
nodo2 = Nodo(dato=15)


nodo2.asignar_anterior(nodo1)
nodo1.asignar_siguiente(nodo2)

nodo3 = Nodo(dato = 7)
nodo1.asignar_siguiente(nodo3)
nodo3.asignar_siguiente(nodo2)
nodo3.asignar_anterior(nodo1)
nodo2.asignar_anterior(nodo3)


nodo_aux = nodo1

#while nodo_aux != None :
#    
#    print(nodo_aux.dato)
#    nodo_aux = nodo_aux.siguiente
    
    
    