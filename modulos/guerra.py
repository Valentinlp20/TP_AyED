# -*- coding: utf-8 -*-

from ListaDobleEnlazada import ListaDobleEnlazada as LDE
import random


def puntos (valor1):
    """Calcula un valor de puntos a cada carta para su comparacion"""
    
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



#_______________________________________________________________COLA DOBLE
class Cola_doble:
    
    def __init__(self):
        
        self.lista=LDE()
        self.tamanio=0
    
    def agregar_in(self, item):
        self.lista.agregar_al_inicio(item)
        self.tamanio+=1
    
    def agregar_fin(self,item):
        self.lista.agregar_al_final(item)
        self.tamanio+=1
        
    def sacar_in(self):
        self.tamanio-=1
        return self.lista.extraer(0)
    
    def sacar_fin(self):
        self.tamanio-=1
        return self.lista.extraer(self.lista.tamanio -1)
    
    def __str__(self):
        return str(self.lista)
    
    def __len__(self):
        return self.tamanio
    
    
    
        
    
#_________________________________________________________________CARTA
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
       
        return puntos(self.valor)<puntos(otro.valor)
    
    def __eq__(self, otro):
        return puntos(self.valor)==puntos(otro.valor)
        
        

#_____________________________________________________________________JUEGO 
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
            carta=self.mazo.sacar_fin()    
            jugador1.agregar_fin(carta)
            
            carta=self.mazo.sacar_fin()
            jugador2.agregar_fin(carta)
        
        #__________________________________________________________________

        self.jugador1=jugador1
        self.jugador2=jugador2
        self.turnos=0

    def duelo(self):
        
        carta1=self.jugador1.sacar_fin()
        carta2=self.jugador2.sacar_fin()
        
        
        
        if carta1>carta2:
            self.jugador1.agregar_in(carta1)
            self.jugador1.agregar_in(carta2)
            
        elif carta1<carta2:
            self.jugador2.agregar_in(carta1)
            self.jugador2.agregar_in(carta2)
            
        carta1=str(carta1)+' '+str(carta2)
        print(carta1.center(60))
            
        
        
        


if __name__ == '__main__':
    
    juego=JuegoGuerra()
    
    
    print('JUGADOR 1:')
    print(juego.jugador1)
    print('Tamaño: ',len(juego.jugador1))
    
    print('')
    print('JUGADOR 2')
    print(juego.jugador2)
    print('Tamaño: ',len(juego.jugador2))
    
    
    print('')
    
    juego.duelo()
    
    print('')
    
    print('JUGADOR 1:')
    print(juego.jugador1)
    print('Tamaño: ',len(juego.jugador1))
    
    print('')
    print('JUGADOR 2')
    print(juego.jugador2)
    print('Tamaño: ',len(juego.jugador2))
    
    
  
    
 
    
    
    

    
    
   
