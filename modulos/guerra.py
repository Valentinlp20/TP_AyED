# -*- coding: utf-8 -*-

from LDE import ListaDobleEnlazada as LDE
import random

class Cola_doble:
    
    def __init__(self):
        
        self.lista=LDE()
    
    def agregar_in(self, item):
        self.lista.agregar_al_inicio(item)
    
    def agregar_fin(self,item):
        self.lista.agregar_al_final(item)
        
    def sacar_in(self):
        return self.lista.extraer(0)
    
    def sacar_fin(self):
        return self.lista.extraer(self.lista.tamanio -1)
    
    def __str__(self):
        return str(self.lista)
    
    def __len__(self):
        return self.lista.tamanio
    
    
    
        
    

class Carta:
    
    def __init__(self,palo, valor):
        self.palo=palo
        self.valor=valor
        self.boca_arriba=True
    
    def __str__(self):
        if self.boca_arriba:
            return self.valor + self.palo
        else:
            return "-X"
        
    def voltear(self):
        self.boca_arriba=not self.boca_arriba
        
        
    def __lt__(self, otro):
        
        valor1=self.valor
        valor2=otro.valor
        
        if valor1 in ['A','J','Q','K']:
            if valor1 =='A':
                valor=14
            elif valor1== 'J':
                valor1=11
            elif valor1== 'Q':
                valor1=12
            elif valor1=='K':
                valor1=13
        
        else:
            valor1=int(valor1)
                
        
        pass

class JuegoGuerra:
    
    def __init__(self):
        
        
        #Creacion del Mazo
        #__________________________________________________________________
        valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        palos = ['♠', '♥', '♦', '♣']
        
        random.shuffle(valores)
        random.shuffle(palos)
        
        cartas=Cola_doble()
        
        for palo in palos:
            for valor in valores:
                carta=Carta(palo, valor)
                cartas.agregar_fin(carta)
        #__________________________________________________________________
        
        
        self.mazo= cartas
        
        
        
        
        #Repartir cartas entre jugadores
        #__________________________________________________________________
        
        jugador1=Cola_doble()
        jugador2=Cola_doble()
        
        for i in range (26):
            carta=self.mazo.sacar_fin().dato      
            jugador1.agregar_fin(carta)
            
            carta=self.mazo.sacar_fin().dato 
            jugador2.agregar_fin(carta)
        
        #__________________________________________________________________

        self.jugador1=jugador1
        self.jugador2=jugador2
        


if __name__ == '__main__':
    
    juego=JuegoGuerra()
    
    
    print('JUGADOR 1:')
    print(juego.jugador1)
    print('Tamaño: ',len(juego.jugador1))
    
    print('')
    print('JUGADOR 2')
    print(juego.jugador2)
    print('Tamaño: ',len(juego.jugador2))
    
    

    
    
   
