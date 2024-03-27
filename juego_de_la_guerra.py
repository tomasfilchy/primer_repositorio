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
    
    def repartir_cartas(self,mazo):
        carta = self.cartas.pop(0)
        mazo.agregar_carta(carta)
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
for c in mazo_de_cartas.cartas:
    mazo_de_cartas.repartir_cartas(mazo1)
    mazo_de_cartas.repartir_cartas(mazo2)
    
mazo1.mostrar_mazo()
mazo2.mostrar_mazo()