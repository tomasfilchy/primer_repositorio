from random import randint

class Paciente():
        def __init__(self):
            riesgo = 1,2,3
            self.riesgo_paciente = riesgo[randint(0,2)]
        def mostrar_riesgo(self):
            return self.riesgo_paciente
class Cola_de_espera():
    def __init__(self):
        self.cola = [0]
        self.tamanio_actual = 0
    
    def infiltArriba(self,i):
        while i // 2 > 0:
            if self.cola[i] < self.cola[i // 2]:
                tmp = self.cola[i // 2]
                self.cola[i // 2] = self.cola[i]
                self.cola[i] = tmp
            i = i // 2
    
    def infiltAbajo(self,i):
        while (i * 2) <= self.tamanio_actual:
            hm = self.hijoMin(i)
            if self.cola[i] > self.cola[hm]:
                tmp = self.cola[i]
                self.cola[i] = self.cola[hm]
                self.cola[hm] = tmp
            i = hm
    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanio_actual:
            return i * 2
        else:
            if self.cola[i*2] < self.cola[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMin(self):
        valorSacado = self.cola[1]
        self.cola[1] = self.cola[self.tamanio_actual]
        self.tamanio_actual = self.tamanio_actual - 1
        self.cola.pop()
        self.infiltAbajo(1)
        return valorSacado

    def agregar_paciente(self,paciente):
        self.cola.append(paciente.riesgo_paciente)
        self.tamanio_actual +=1 
        self.infiltArriba(self.tamanio_actual)
    



