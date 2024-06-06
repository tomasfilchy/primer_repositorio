
from random import randint

class Paciente:
    
    def __init__(self, nombre=None):
        self.nombre = nombre if nombre is not None else f"Paciente_{randint(1, 1000)}"
        riesgo = [1, 2, 3]
        self.riesgo_paciente = riesgo[randint(0, 2)]

    def __repr__(self):
        return f'{self.nombre} (Riesgo: {self.riesgo_paciente})'

    def mostrar_riesgo(self):
        return self.riesgo_paciente

class Cola_de_espera:
    def __init__(self):
        self.cola = [0]  
        self.tamanio_actual = 0
    
    def infiltArriba(self, i):
        while i // 2 > 0:
            if self.cola[i].riesgo_paciente < self.cola[i // 2].riesgo_paciente:
                self.cola[i], self.cola[i // 2] = self.cola[i // 2], self.cola[i]
            i = i // 2
    
    def infiltAbajo(self, i):
        while (i * 2) <= self.tamanio_actual:
            hm = self.hijoMin(i)
            if self.cola[i].riesgo_paciente > self.cola[hm].riesgo_paciente:
                self.cola[i], self.cola[hm] = self.cola[hm], self.cola[i]
            i = hm

    def hijoMin(self, i):
        if i * 2 + 1 > self.tamanio_actual:
            return i * 2
        else:
            if self.cola[i * 2].riesgo_paciente < self.cola[i * 2 + 1].riesgo_paciente:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMin(self):
        if self.tamanio_actual == 0:
            raise IndexError("Eliminar de una cola de prioridad vacía")
        valorSacado = self.cola[1]
        self.cola[1] = self.cola[self.tamanio_actual]
        self.tamanio_actual -= 1
        self.cola.pop()
        if self.tamanio_actual > 0:
            self.infiltAbajo(1)
        return valorSacado

    def agregar_paciente(self, paciente):
        self.cola.append(paciente)
        self.tamanio_actual += 1
        self.infiltArriba(self.tamanio_actual)

    def __repr__(self):
        return '\n'.join(str(paciente) for paciente in self.cola[1:])
    



