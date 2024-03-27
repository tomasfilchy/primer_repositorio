from random import randint
class mazo():
    def __init__(self) :
        self.cartas = []
    
    def agregar_carta(self,carta):
        self.cartas.append(carta)
    
    def mezclar_cartas(self):
        for c in range(len(self.cartas)-1):
            carta_random = randint(0,len(self.cartas)-1)
            self.cartas[c], self.cartas[carta_random] = self.cartas[carta_random], self.cartas[c]
        
        
    def mostrar_mazo(self):
        print(self.cartas)
    
    def repartir_carta(self,mazo1,mazo2):
        while len(self.cartas) > 0:
            mazo1.agregar_carta(self.cartas.pop(0))
            mazo2.agregar_carta(self.cartas.pop(0))
class carta():
    def __init__(self,numero) :
        self.numero = numero 
    
    def obtener_numero(self):
        return self.numero
    
mazo_de_cartas = mazo()
for palo in range (4):
    for n in range(1,13):
        mazo_de_cartas.agregar_carta(n)
        
mazo1 = mazo()
mazo2 = mazo()
mazo_de_cartas.mezclar_cartas()
mazo_de_cartas.repartir_carta(mazo1,mazo2)
mazo1.mostrar_mazo()
mazo2.mostrar_mazo()

print(len(mazo1.cartas), len(mazo2.cartas))