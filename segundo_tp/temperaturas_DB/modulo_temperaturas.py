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
                nodo_actual.hijoIzquierdo = Temperatura(fecha, temperatura, padre=nodo_actual)
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
            if nodo.hijoDerecho:
                if nodo.hijoDerecho.factorEquilibrio > 0:
                    self.rotarDerecha(nodo.hijoDerecho)
                    self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.hijoIzquierdo:
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

    def rotarDerecha(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                    rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
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
        if self.raiz:
            return self._max_temp_rango(fecha1, fecha2, self.raiz)
        else:
            return None

    def _max_temp_rango(self, fecha1, fecha2, nodo):
        if not nodo:
            return None
        if datetime.strptime(fecha1, "%d/%m/%Y") <= datetime.strptime(nodo.fecha, "%d/%m/%Y") <= datetime.strptime(fecha2, "%d/%m/%Y"):
            max_temp = max(nodo.temperatura, self._max_temp_rango(fecha1, fecha2, nodo.hijoIzquierdo), self._max_temp_rango(fecha1, fecha2, nodo.hijoDerecho))
            return max_temp
        elif fecha1 < nodo.fecha:
            return self._max_temp_rango(fecha1, fecha2, nodo.hijoIzquierdo)
        else:
            return self._max_temp_rango(fecha1, fecha2, nodo.hijoDerecho)
    
    def min_temp_rango(self, fecha1, fecha2):
        if self.raiz:
            return self._min_temp_rango(fecha1, fecha2, self.raiz)
        else:
            return None

    def _min_temp_rango(self, fecha1, fecha2, nodo):
        if not nodo:
            return None
        if fecha1 <= nodo.fecha <= fecha2:
            min_temp = min(nodo.temperatura, self._min_temp_rango(fecha1, fecha2, nodo.hijoIzquierdo), self._min_temp_rango(fecha1, fecha2, nodo.hijoDerecho))
            return min_temp
        elif fecha1 < nodo.fecha:
            return self._min_temp_rango(fecha1, fecha2, nodo.hijoIzquierdo)
        else:
            return self._min_temp_rango(fecha1, fecha2, nodo.hijoDerecho)
            
            

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


temp.guardar_temperatura("20/01/2000", 10)
temp.guardar_temperatura("19/01/2000", 15)
temp.guardar_temperatura("18/01/2000", 20)
temp.guardar_temperatura("17/01/2000", 25)
temp.guardar_temperatura("21/01/2000", 22)
temp.guardar_temperatura("22/01/2000", 23)
temp.guardar_temperatura("23/01/2000", 24)

print(temp.raiz.hijoDerecho.hijoDerecho.hijoDerecho.temperatura)