from datetime import datetime

class Temperaturas_DB:
    def __init__(self):
        self.raiz = None
        self.tamaño = 0  

    def guardar_temperatura(self, fecha, temperatura):
        if self.raiz:
            self._agregar(fecha, temperatura, self.raiz)
        else:
            self.raiz = Temperatura(fecha, temperatura)
        self.tamaño += 1  

    def _agregar(self, fecha, temperatura, nodo_actual):
        if datetime.strptime(fecha, "%d/%m/%Y") < datetime.strptime(nodo_actual.fecha, "%d/%m/%Y"):
            if nodo_actual.hijoIzquierdo:  
                self._agregar(fecha, temperatura, nodo_actual.hijoIzquierdo)
                
            else:
                nodo_actual.hijo_izquierdo = Temperatura(fecha, temperatura, padre=nodo_actual)
                self.actualizarEquilibrio(nodo_actual.hijoIzquierdo)
        else:
            if nodo_actual.hijoDerecho:
                self._agregar(fecha, temperatura, nodo_actual.hijoDerecho)
                

            else:
                nodo_actual.hijoDerecho = Temperatura(fecha, temperatura, padre=nodo_actual)
                self.actualizarEquilibrio(nodo_actual.hijoDerecho)
    
    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                    nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)

    def reequilibrar(self,nodo):
        if nodo.factorEquilibrio < 0:
            if nodo.hijoDerecho.factorEquilibrio > 0:
                self.rotarDerecha(nodo.hijoDerecho)
                self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
             if nodo.hijoIzquierdo.factorEquilibrio < 0:
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
             else:
                self.rotarDerecha(nodo)
    def rotarIzquierda(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)

    
    
    
    
    def devolver_temperatura(self,fecha):
        if self.raiz:
            res = self._obtener(fecha,self.raiz)
            if res:
                return res.temperatura
            else:
                return None
        else:
            return None

    def _obtener(self,fecha,nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.fecha == fecha:
            return nodoActual
        elif datetime.strptime(fecha, "%d/%m/%Y") < datetime.strptime(nodoActual.fecha, "%d/%m/%Y"):
            return self._obtener(fecha,nodoActual.hijoIzquierdo)
        else:
            return self._obtener(fecha,nodoActual.hijoDerecho)

    def __getitem__(self,fecha):
        return self.obtener(fecha)

    def __contains__(self,clave):
        if self._obtener(clave,self.raiz):
            return True
        else:
            return False


    def max_temp_rango(self, fecha1, fecha2):
        fecha_obj1 = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha_obj2 = datetime.strptime(fecha2, "%d/%m/%Y")
        max_temp = 100
        nodo_actual = self.raiz
        while nodo_actual:
            if nodo_actual.temperatura > max_temp:
                max_temp = nodo_actual.temperatura
            if fecha_obj1 < datetime.strptime(nodo_actual.fecha, "%d/%m/%Y") <= fecha_obj2:
                nodo_actual = nodo_actual.hijoDerecho
                
            else: 
                nodo_actual= nodo_actual.hijoIzquierdo


class Temperatura():
    def __init__(self, fecha, temperatura, padre=None):
        self.fecha = fecha
        self.temperatura = temperatura
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.factorEquilibrio = 0
        self.padre = padre
    def esHijoIzquierdo(self):
        if self == self.padre.hijoIzquierdo:
            return True 
    def esHijoDerecho(self):
        if self == self.padre.hijoDerecho:
            return True 
    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho and self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,fecha,temperatura, hizq,hder):
        self.fecha = fecha
        self.cargaUtil = temperatura
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self
    
    
            
temp = Temperaturas_DB()
temp.guardar_temperatura("01/10/2000", 30)
temp.guardar_temperatura("02/10/2000", 32)
temp.guardar_temperatura("03/10/2000", 33)
temp.guardar_temperatura("04/10/2000", 34)
temp.guardar_temperatura("05/10/2000", 35)

print(temp.max_temp_rango("01/10/2000","05/10/2000"))
