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
            self.tamanio +=1 
        else:
            
            self.cabeza.asignar_arriba(carta)
            carta.asignar_abajo(self.cabeza)
            self.cabeza = carta
            self.tamanio +=1 
    def poner_carta_abajo(self,carta):
            if self.cola == None:
                self.cabeza = carta
                self.cola = carta  
                self.tamanio +=1 
            else:
                self.cola.asignar_abajo(carta)
                carta.asignar_arriba(self.cola)
                self.cola = carta
                self.tamanio +=1 
    
    def sacar_carta_arriba(self):
        if self.tamanio > 0 and self.cabeza is not None:
            carta_a_sacar = self.cabeza
            carta_a_sacar.visible = True
            self.cabeza = self.cabeza.carta_abajo
            self.tamanio -= 1
            return carta_a_sacar
        else:   
            raise DequeEmptyError
        
        
    def __len__ (self):
        
        return self.tamanio

        
        
carta = Carta('4', 'treboles')
carta2 = Carta('5', 'treboles')
carta3 = Carta('10', 'treboles')
carta4 = Carta('1', 'treboles')
mazo = Mazo()
    

