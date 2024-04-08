from nodo import Nodo


class listadDoblementeEnlazada:
    """lista doblemente enlazada como tipo de dato abstracto"""
    def __init__(self):
        self.cabeza = None
        self.cola = None 
        self.longitud = 0 
        
    def agregar_al_inicio(self, item):
        nodo_nuevo = Nodo(dato=item)
        #caso 1: la lista esta vacia 
        if self.esta_vacia():
            self.cabeza = nodo_nuevo
            self.cola = nodo_nuevo
        #caso 2: cuando la lista no esta vacia 
        else:
            nodo_nuevo.asignar_siguiente(self.cabeza)
            self.cabeza.asignar_anterior(nodo_nuevo)
            self.cabeza = nodo_nuevo
        self.longitud += 1
    def agregar_al_final(self, item):
        nodo_nuevo = Nodo(dato=item)

        if self.esta_vacia():
            self.cabeza = nodo_nuevo
            self.cola = nodo_nuevo
        else:
            nodo_nuevo.asignar_anterior(self.cola)
            self.cola.asignar_siguiente(nodo_nuevo)
            self.cola = nodo_nuevo
        self.longitud += 1
    def insertar(self, item, posicion):
        if posicion == 0:
            nodo_nuevo = Nodo(dato=item)
            nodo_a_cambiar = self.cabeza
            nodo_nuevo.asignar_siguiente(nodo_a_cambiar.siguiente)
            self.cabeza = nodo_nuevo
        elif posicion == self.longitud-1 :
            nodo_nuevo = Nodo(dato=item)
            nodo_a_cambiar = self.cola
            nodo_a_cambiar.anterior.asignar_siguiente(nodo_nuevo)
            nodo_nuevo.asignar_anterior(nodo_a_cambiar.anterior)
            self.cola = nodo_nuevo
        
        elif posicion-1 < self.longitud:
            nodo_nuevo = Nodo(dato = item)
            contador = 0
            nodo_anterior = self.cabeza
            while contador != posicion-1:
                contador +=1
                nodo_anterior = nodo_anterior.siguiente
            #print(nodo_anterior.mostrarNodo())
            nodo_a_cambiar = nodo_anterior.siguiente
            nodo_siguiente =nodo_a_cambiar.siguiente
            nodo_nuevo.asignar_siguiente(nodo_siguiente)
            nodo_nuevo.asignar_anterior(nodo_anterior)
            nodo_anterior.asignar_siguiente(nodo_nuevo)
            nodo_siguiente.asignar_anterior(nodo_nuevo)
            
            
            
    def esta_vacia(self):
        return self.cabeza is None
    def __len__ (self):
        self.longitud

if __name__ == "__main__":
    
    LDE = listadDoblementeEnlazada() # creamos una lista vacia 
    
    LDE.agregar_al_inicio(1000)
    LDE.agregar_al_inicio(500)
    LDE.agregar_al_inicio(250)
    LDE.agregar_al_final(100)
    LDE.agregar_al_final(2000)
    LDE.insertar(3000, 4)
    nodo_aux = LDE.cabeza
    
    while nodo_aux != None:
        
        print(nodo_aux.mostrarNodo())
        nodo_aux=nodo_aux.siguiente
    
    