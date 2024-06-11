# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 16:51:54 2022

@author: Cátedra de Algoritmos y Estructura de Datos
"""

class Carta:
    
    def __init__(self, dato='', palo='', carta_arriba = None, carta_abajo = None):
        self.dato = dato
        self.palo = palo
        self.visible:bool = False
        self.carta_arriba = carta_arriba
        self.carta_abajo = carta_abajo
    def asignar_arriba(self, carta):
        self.carta_arriba = carta
    def asignar_abajo(self, carta):
        self.carta_abajo = carta
    @property
    def visible(self):
        return self._visible
        
    @visible.setter
    def visible(self, visible):
        self._visible = visible
        
    @property
    def dato(self):
        return self._dato
    
    @dato.setter
    def dato(self, dato):
        self._dato = dato
        
    @property
    def palo(self):
        return self._palo
    
    @palo.setter
    def palo(self, palo):
        self._palo = palo  
    
    def _valor_numerico(self):
        valores = ['J','Q','K','A']
        if self.dato in valores:
            idx = valores.index(self.dato)
            return (11 + idx)
        return int(self.dato)            
            
        
    def __gt__(self, otra):
        """2 cartas deben compararse por su valor numérico"""
        return self._valor_numerico() > otra._valor_numerico()
        
    def __str__(self):
        #if self.visible == False:
         #   return "-X"
        #else:
            return self
    
    def __repr__(self):
        return str(self)
    
    
#if __name__ == "__main__":
#    carta = Carta("♣", "3")
#    print(carta)
#    carta.visible = True
#    print(carta)
#    