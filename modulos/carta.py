# -*- coding: utf-8 -*-

def puntos (valor1):
    """Calcula los puntos a una carta para su comparacion"""
    
    if valor1 in ['A','J','Q','K']:
        if valor1 =='A':
            valor1=14
        elif valor1== 'J':
            valor1=11
        elif valor1== 'Q':
            valor1=12
        elif valor1=='K':
            valor1=13
    
    else:
        valor1=int(valor1)
    
    return valor1

    
    
#_________________________________________________________________CARTA
class Carta:
    """Modela una carta de la baraja"""
    
    
    def __init__(self,palo, valor):
        self.palo=palo
        self.valor=valor
        #por defecto la carta esta boca abajo
        self.boca_arriba=False
    
    def __str__(self):
        if self.boca_arriba:
            return self.valor + self.palo
        else:
            return "-X"
        
    def voltear(self):
        self.boca_arriba=not self.boca_arriba
        
        
    def __lt__(self, otro):     
        return puntos(self.valor)<puntos(otro.valor)
    
    def __eq__(self, otro):
        return puntos(self.valor)==puntos(otro.valor)