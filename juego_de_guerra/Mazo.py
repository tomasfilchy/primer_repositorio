from Carta import Carta



class DequeEmptyError(Exception):
    """Un jugador se ha quedado sin cartas"""
    pass

class Mazo():
    def __init__ (self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
        
    def poner_carta_arriba(self, carta):
         
        if self.cabeza == None:
            self.cabeza = carta
            self.cola = carta
            
        else:
            
            self.cabeza.asignar_arriba(carta)
            carta.asignar_abajo(self.cabeza)
            self.cabeza = carta
    def poner_carta_abajo(self,carta):
            if self.cola == None:
                self.cabeza = carta
                self.cola = carta  
            else:
                self.cola.asignar_abajo(carta)
                carta.asignar_arriba(self.cola)
                self.cola = carta
    
    def sacar_carta_arriba(self):
        carta.visible = True
        carta_a_sacar = self.cabeza
        self.cabeza = self.cabeza.carta_abajo
        self.cabeza = None
        return carta_a_sacar
    
    def __len__ (self):
        return self.tamanio
        
        
carta = Carta('4', 'treboles')
carta2 = Carta('5', 'treboles')
carta3 = Carta('10', 'treboles')
carta4 = Carta('1', 'treboles')
mazo = Mazo()
    
mazo.poner_carta_arriba(carta)
mazo.poner_carta_arriba(carta2)
mazo.poner_carta_abajo(carta3)
mazo.poner_carta_abajo(carta4)

print(mazo.cola.dato)