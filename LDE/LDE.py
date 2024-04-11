from nodo import Nodo


class ListaDobleEnlazada():
    """lista doblemente enlazada como tipo de dato abstracto"""
    def __init__(self):
        self.cabeza = None
        self.cola = None 
        self.tamanio = 0 
        
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
        self.tamanio += 1
    def agregar_al_final(self, item):
        nodo_nuevo = Nodo(dato=item)

        if self.esta_vacia():
            self.cabeza = nodo_nuevo
            self.cola = nodo_nuevo
        else:
            nodo_nuevo.asignar_anterior(self.cola)
            self.cola.asignar_siguiente(nodo_nuevo)
            self.cola = nodo_nuevo
        self.tamanio += 1
    def insertar(self, item, posicion):
        if posicion == 0:
            nodo_nuevo = Nodo(dato=item)
            nodo_a_cambiar = self.cabeza
            nodo_nuevo.asignar_siguiente(nodo_a_cambiar)
            self.cabeza = nodo_nuevo
            nodo_a_cambiar.asignar_anterior(nodo_nuevo)
        elif posicion == self.tamanio-1 :
            nodo_nuevo = Nodo(dato=item)
            nodo_a_cambiar = self.cola
            nodo_nuevo.asignar_siguiente(nodo_a_cambiar)
            nodo_a_cambiar.anterior.asignar_siguiente(nodo_nuevo)
            nodo_nuevo.asignar_anterior(nodo_a_cambiar.anterior)
            nodo_a_cambiar.asignar_anterior(nodo_nuevo)
        elif posicion-1 < self.tamanio:
            nodo_nuevo = Nodo(dato = item)
            contador = 0
            nodo_a_cambiar = self.cabeza
            contador = 0
            while contador != posicion:
                contador +=1
                nodo_a_cambiar = nodo_a_cambiar.siguiente
            nodo_a_cambiar.anterior.asignar_siguiente(nodo_nuevo)
            nodo_nuevo.asignar_siguiente(nodo_a_cambiar)
            nodo_nuevo.asignar_anterior(nodo_a_cambiar.anterior)
            nodo_a_cambiar.asignar_anterior(nodo_nuevo) 
            
        self.tamanio +=1   
    def extraer(self, posicion=None):
        try:
                if posicion == None:
                    nodo = self.cola
                    self.cola = nodo.anterior
                    self.cola.asignar_siguiente(None)
                    self.tamanio -=1
                    return nodo.mostrarNodo()
                elif posicion < 0 or posicion > self.tamanio:
                    raise IndexError("la posicion indexada no existe en la lista")
                elif self.cabeza == None:
                    raise MemoryError("la lista esta vacia")
               
                elif posicion == 0 :
                    nodo_a_extraer = self.cabeza
                    self.cabeza = nodo_a_extraer.siguiente
                    self.cabeza.asignar_anterior(None)
                    self.tamanio -=1 
                    return nodo_a_extraer.mostrarNodo()
                elif posicion == self.tamanio:
                    nodo = self.cola
                    self.cola = nodo.anterior
                    self.cola.asignar_siguiente(None)
                    self.tamanio -=1
                    return nodo.mostrarNodo()
                else: 
                    nodo_a_extraer = self.cabeza
                    contador = 0
                    while contador != posicion-1:
                        contador +=1 
                        nodo_a_extraer = nodo_a_extraer.siguiente
                        if nodo_a_extraer is None:
                            raise IndexError("la posicion indexada no existe en la lista")
                    nodo_a_extraer.anterior.asignar_siguiente(nodo_a_extraer.siguiente)
                    nodo_a_extraer.siguiente.asignar_anterior(nodo_a_extraer.anterior)
                    self.tamanio -=1 
        except IndexError as e :
                        nodo_a_extraer = None
                        print(e)
            
        except MemoryError as b:
                    print (b)
               
    def copiar(self):
        nodo = self.cabeza
        lista = ListaDobleEnlazada()
        while nodo != None:
            lista.agregar_al_final(nodo.mostrarNodo())
            nodo = nodo.siguiente
        return lista
        
    def invertir(self):
    
        
        lista_invertida = ListaDobleEnlazada()
        nodo = self.cabeza
        lista_invertida.agregar_al_inicio(nodo.mostrarNodo())
        while nodo != None:
            nodo = nodo.siguiente
            if nodo != None:
                lista_invertida.agregar_al_inicio(nodo.mostrarNodo())
        self.cabeza = lista_invertida.cabeza
    
    def concatenar(self, lista):
        if self.cabeza is None:
            return lista.cabeza
        if lista.cabeza is None:
            return self.cabeza
        
        ultimo_nodo = self.cabeza
        while ultimo_nodo.siguiente is not None:
            ultimo_nodo = ultimo_nodo.siguiente
            
        ultimo_nodo.asignar_siguiente(lista.cabeza)
        lista.cabeza.asignar_anterior (ultimo_nodo)
        self.tamanio += lista.tamanio
    def esta_vacia(self):
        return self.cabeza is None
    def __len__ (self):
        return self.tamanio
    def __add__ (self, lista):
        
        self.concatenar(lista)
   
        return self.tamanio
    def __iter__ (self):
        nodo = self.cabeza
        
        while nodo != None:
            yield nodo.mostrarNodo()
            nodo = nodo.siguiente

    
    
    
    
if __name__ == "__main__":
    
    LDE = ListaDobleEnlazada() # creamos una lista vacia 
    lista = ListaDobleEnlazada()

    LDE.agregar_al_inicio(1000)
    LDE.agregar_al_inicio(500)
    LDE.agregar_al_inicio(250)
    LDE.agregar_al_final(2000)
    LDE.agregar_al_final(3000)
    lista = LDE.copiar()
    #lista.invertir
    #nodo = lista.extraer(0)
    
    #lista.concatenar(LDE)
    LDE + lista
    print(LDE.cabeza.anterior)

    