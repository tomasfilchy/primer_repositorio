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
        if nodo.factorEquilibrio < -1:
            if nodo.hijoDerecho:
                if nodo.hijoDerecho.factorEquilibrio > 0:
                    self.rotarDerecha(nodo.hijoDerecho)
                    self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 1:
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
        rotRaiz.factorEquilibrio = 0  # Actualiza el factor de equilibrio del nodo movido
        nuevaRaiz.factorEquilibrio = 1  # Ajusta el factor de equilibrio del nuevo nodo raíz

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
        rotRaiz.factorEquilibrio = 0  # Actualiza el factor de equilibrio del nodo movido
        nuevaRaiz.factorEquilibrio = 1  # Ajusta el factor de equilibrio del nuevo nodo raíz
    
    
    
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
        return self._buscar_max_temp_rango(self.raiz, fecha1, fecha2)

    def _buscar_max_temp_rango(self, nodo, fecha1, fecha2):
        if nodo is None:
            return None

        max_temp = None
        if datetime.strptime(fecha1, "%d/%m/%Y") <= datetime.strptime(nodo.fecha, "%d/%m/%Y") <= datetime.   strptime(fecha2, "%d/%m/%Y"):
            temp = nodo.temperatura
            temp_izq = self._buscar_max_temp_rango(nodo.hijoIzquierdo, fecha1, fecha2)
            temp_der = self._buscar_max_temp_rango(nodo.hijoDerecho, fecha1, fecha2)

            if temp_izq is not None and temp_izq > temp:
                temp = temp_izq
            if temp_der is not None and temp_der > temp:
                temp = temp_der

            if temp is not None:
                max_temp = temp

        return max_temp
    
    def min_temp_rango(self, fecha_inicio, fecha_fin):
        return self._buscar_min_temp_rango(self.raiz, fecha_inicio, fecha_fin)

    def _buscar_min_temp_rango(self, nodo, fecha1, fecha2):
        if nodo is None:
            return None

        min_temp = None
        if datetime.strptime(fecha1, "%d/%m/%Y") <= datetime.strptime(nodo.fecha, "%d/%m/%Y") <= datetime.strptime(fecha2, "%d/%m/%Y"):
            temp = nodo.temperatura
            temp_izq = self._buscar_min_temp_rango(nodo.hijoIzquierdo, fecha1, fecha2)
            temp_der = self._buscar_min_temp_rango(nodo.hijoDerecho, fecha1, fecha2)

            if temp_izq is not None and temp_izq < temp:
                temp = temp_izq
            if temp_der is not None and temp_der < temp:
                temp = temp_der

            if temp is not None:
                min_temp = temp
            
        return min_temp
    
    def temp_extremos_rango(self, fecha1, fecha2):
        return self.buscar_temp_extremos( self.raiz, fecha1, fecha2)
    
    def buscar_temp_extremos(self,nodo, fecha1, fecha2):
        
        if nodo is None:
            return None
        max_temp = None
        min_temp = None
        if datetime.strptime(fecha1, "%d/%m/%Y") <= datetime.strptime(nodo.fecha, "%d/%m/%Y") <= datetime.strptime(fecha2, "%d/%m/%Y"):     

            temp_max = nodo.temperatura
            temp_min = nodo.temperatura
            temp_izq = self._buscar_max_temp_rango(nodo.hijoIzquierdo, fecha1, fecha2)
            temp_der = self._buscar_max_temp_rango(nodo.hijoDerecho, fecha1, fecha2)

            if temp_der is not None and temp_der > temp_max:
                temp_max = temp_der
            if temp_der is not None and temp_der > temp_max:
                temp_max = temp_der
            if temp_der is not None and temp_der < temp_min:
                temp_min = temp_izq
            if temp_der is not None and temp_der < temp_min:
                temp_min = temp_izq
            if temp_max is not None:
                max_temp = temp_max
            if temp_min is not None:
                min_temp = temp_min
                
        return min_temp,  max_temp
    
    from datetime import datetime

class Temperatura:
    def __init__(self, fecha, temperatura, padre=None):
        self.fecha = fecha
        self.temperatura = temperatura
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.factorEquilibrio = 0
        self.padre = padre

    def esHijoIzquierdo(self):
        return self == self.padre.hijoIzquierdo

    def esHijoDerecho(self):
        return self == self.padre.hijoDerecho

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho and self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def tieneUnSoloHijo(self):
        return self.tieneAlgunHijo() and not self.tieneAmbosHijos()

    def reemplazarDatoDeNodo(self, fecha, temperatura, hizq, hder):
        self.fecha = fecha
        self.temperatura = temperatura
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

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

    def actualizarEquilibrio(self, nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio!= 0:
                self.actualizarEquilibrio(nodo.padre)

    def reequilibrar(self, nodo):
        if nodo.factorEquilibrio < -1:
            if nodo.hijoDerecho:
                if nodo.hijoDerecho.factorEquilibrio > 0:
                    self.rotarDerecha(nodo.hijoDerecho)
                    self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 1:
            if nodo.hijoIzquierdo:
                if nodo.hijoIzquierdo.factorEquilibrio < 0:
                    self.rotarIzquierda(nodo.hijoIzquierdo)
                    self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)

    def rotarIzquierda(self, rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo:
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
        rotRaiz.factorEquilibrio = 0
        nuevaRaiz.factorEquilibrio = 1

    def rotarDerecha(self, rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho:
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
        rotRaiz.factorEquilibrio = 0
        nuevaRaiz.factorEquilibrio = 1

    def borrar_temperatura(self, fecha):
        fecha_a_eliminar = datetime.strptime(fecha, "%d/%m/%Y")
        nodo_actual = self.raiz
        nodo_padre = None
        nodo_a_eliminar = None

        while nodo_actual:
            if datetime.strptime(nodo_actual.fecha, "%d/%m/%Y") == fecha_a_eliminar:
                nodo_a_eliminar = nodo_actual
                break
            elif datetime.strptime(nodo_actual.fecha, "%d/%m/%Y") > fecha_a_eliminar:
                nodo_padre = nodo_actual
                nodo_actual = nodo_actual.hijoIzquierdo
            else:
                nodo_padre = nodo_actual
                nodo_actual = nodo_actual.hijoDerecho

        if nodo_a_eliminar is None:
            print("Fecha no encontrada.")
            return
        if nodo_a_eliminar.esHoja():
            self._eliminar_hoja(nodo_a_eliminar, nodo_padre)
        elif nodo_a_eliminar.tieneUnSoloHijo():
            self._reemplazar_con_un_solo_hijo(nodo_a_eliminar, nodo_padre)
        else:
            self._reemplazar_con_dos_hijos(nodo_a_eliminar, nodo_padre)

    def _eliminar_hoja(self, nodo_a_eliminar, nodo_padre):
        if nodo_padre is None:
            self.raiz = nodo_a_eliminar.hijoIzquierdo if nodo_a_eliminar.hijoIzquierdo else nodo_a_eliminar.hijoDerecho
        else:
            if nodo_padre.esHijoIzquierdo() and nodo_padre.hijoIzquierdo == nodo_a_eliminar:
                nodo_padre.hijoIzquierdo = nodo_a_eliminar.hijoIzquierdo
            else:
                nodo_padre.hijoDerecho = nodo_a_eliminar.hijoDerecho
        self.tamaño -= 1
        self.actualizarEquilibrio(nodo_padre)

    def _reemplazar_con_un_solo_hijo(self, nodo_a_eliminar, nodo_padre):
        hijo = nodo_a_eliminar.hijoIzquierdo if nodo_a_eliminar.hijoIzquierdo else nodo_a_eliminar.hijoDerecho
        if nodo_padre is None:
            self.raiz = hijo
        else:
            if nodo_padre.esHijoIzquierdo() and nodo_padre.hijoIzquierdo == nodo_a_eliminar:
                nodo_padre.hijoIzquierdo = hijo
            else:
                nodo_padre.hijoDerecho = hijo
        self.tamaño -= 1
        self.actualizarEquilibrio(nodo_padre)

    def _reemplazar_con_dos_hijos(self, nodo_a_eliminar, nodo_padre):
        sucesor = self._encontrar_sucesor_enorden(nodo_a_eliminar)
        if nodo_padre is None:
            self.raiz = sucesor
        else:
            if nodo_padre.esHijoIzquierdo() and nodo_padre.hijoIzquierdo == nodo_a_eliminar:
                nodo_padre.hijoIzquierdo = sucesor
            else:
                nodo_padre.hijoDerecho = sucesor
        sucesor.reemplazarDatoDeNodo(nodo_a_eliminar.fecha, nodo_a_eliminar.temperatura, nodo_a_eliminar.hijoIzquierdo, nodo_a_eliminar.hijoDerecho)
        self.tamaño -= 1
        self.actualizarEquilibrio(nodo_padre)

    def _encontrar_sucesor_enorden(self, nodo):
        nodo_actual = nodo.hijoDerecho
        while nodo_actual and nodo_actual.hijoIzquierdo:
            nodo_actual = nodo_actual.hijoIzquierdo
        return nodo_actual
            
        
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
       if self.hijoDerecho and self.hijoIzquierdo:
            return True
       else:
           return False
    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def tieneUnSoloHijo(self):
        return self.tieneAlgunHijo() and not self.tieneAmbosHijos()
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


temp.borrar_temperatura("19/01/2000")
print(temp.raiz.hijoIzquierdo.hijoIzquierdo.temperatura)