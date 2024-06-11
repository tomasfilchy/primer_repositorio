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
        return not (self.hijoDerecho or self.hijoIzquierdo)

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
        if self.hijoIzquierdo:
            self.hijoIzquierdo.padre = self
        if self.hijoDerecho:
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

            if nodo.padre.factorEquilibrio != 0:
                self.actualizarEquilibrio(nodo.padre)

    def reequilibrar(self, nodo):
        if nodo.factorEquilibrio < -1:
            if nodo.hijoDerecho and nodo.hijoDerecho.factorEquilibrio > 0:
                self.rotarDerecha(nodo.hijoDerecho)
            self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 1:
            if nodo.hijoIzquierdo and nodo.hijoIzquierdo.factorEquilibrio < 0:
                self.rotarIzquierda(nodo.hijoIzquierdo)
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

    def devolver_temperatura(self, fecha):
        if self.raiz:
            res = self._obtener(fecha, self.raiz)
            if res:
                return res.temperatura
            else:
                return None
        else:
            return None

    def _obtener(self, fecha, nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.fecha == fecha:
            return nodoActual
        elif datetime.strptime(fecha, "%d/%m/%Y") < datetime.strptime(nodoActual.fecha, "%d/%m/%Y"):
            return self._obtener(fecha, nodoActual.hijoIzquierdo)
        else:
            return self._obtener(fecha, nodoActual.hijoDerecho)

    def __getitem__(self, fecha):
        return self.devolver_temperatura(fecha)

    def __contains__(self, clave):
        return self._obtener(clave, self.raiz) is not None

    def max_temp_rango(self, fecha1, fecha2):
        return self._buscar_max_temp_rango(self.raiz, fecha1, fecha2)

    def _buscar_max_temp_rango(self, nodo, fecha1, fecha2):
        if nodo is None:
            return None

        max_temp = None
        if datetime.strptime(fecha1, "%d/%m/%Y") <= datetime.strptime(nodo.fecha, "%d/%m/%Y") <= datetime.strptime(fecha2, "%d/%m/%Y"):
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

    def min_temp_rango(self, fecha1, fecha2):
        return self._buscar_min_temp_rango(self.raiz, fecha1, fecha2)

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
        min_temp = self.min_temp_rango(fecha1, fecha2)
        max_temp = self.max_temp_rango(fecha1, fecha2)
        return min_temp, max_temp

    def borrar_temperatura(self, fecha):
        fecha_a_eliminar = datetime.strptime(fecha, "%d/%m/%Y")
        nodo_actual = self.raiz
        nodo_padre = None

        while nodo_actual and datetime.strptime(nodo_actual.fecha, "%d/%m/%Y") != fecha_a_eliminar:
            nodo_padre = nodo_actual
            if fecha_a_eliminar < datetime.strptime(nodo_actual.fecha, "%d/%m/%Y"):
                nodo_actual = nodo_actual.hijoIzquierdo
            else:
                nodo_actual = nodo_actual.hijoDerecho

        if nodo_actual is None:
            return False

        if nodo_actual.esHoja():
            if nodo_padre is None:
                self.raiz = None
            elif nodo_padre.hijoIzquierdo == nodo_actual:
                nodo_padre.hijoIzquierdo = None
            else:
                nodo_padre.hijoDerecho = None

        elif nodo_actual.tieneUnSoloHijo():
            if nodo_actual.hijoIzquierdo:
                hijo = nodo_actual.hijoIzquierdo
            else:
                hijo = nodo_actual.hijoDerecho

            if nodo_padre is None:
                self.raiz = hijo
            elif nodo_padre.hijoIzquierdo == nodo_actual:
                nodo_padre.hijoIzquierdo = hijo
            else:
                nodo_padre.hijoDerecho = hijo

            hijo.padre = nodo_padre

        else:
            sucesor = self._encontrar_sucesor(nodo_actual)
            nodo_actual.fecha = sucesor.fecha
            nodo_actual.temperatura = sucesor.temperatura

            if sucesor.padre.hijoIzquierdo == sucesor:
                sucesor.padre.hijoIzquierdo = sucesor.hijoDerecho
            else:
                sucesor.padre.hijoDerecho = sucesor.hijoDerecho

            if sucesor.hijoDerecho:
                sucesor.hijoDerecho.padre = sucesor.padre

        self.tamaño -= 1
        return True

    def _encontrar_sucesor(self, nodo):
        sucesor = nodo.hijoDerecho
        while sucesor.hijoIzquierdo:
            sucesor = sucesor.hijoIzquierdo
        return sucesor
    def devolver_temperaturas(self, fecha1, fecha2):
        result = []
        self._buscar_temperaturas_rango(self.raiz, fecha1, fecha2, result)
        result.sort(key=lambda x: x[0])  
        return [f"{fecha}: {temp} ºC" for fecha, temp in result]

    def _buscar_temperaturas_rango(self, nodo, fecha1, fecha2, result):
        if not nodo:
            return
        if fecha1 <= nodo.fecha <= fecha2:
            result.append((nodo.fecha, nodo.temperatura))
        if fecha1 < nodo.fecha:
            self._buscar_temperaturas_rango(nodo.hijoIzquierdo, fecha1, fecha2, result)
        if nodo.fecha < fecha2:
            self._buscar_temperaturas_rango(nodo.hijoDerecho, fecha1, fecha2, result)
    def cantidad_temperaturas(self):
        return self.tamaño
    
    


