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
    
    
    
        
    
#_________________________________________________________________CARTA
class Carta:
    
    def __init__(self,palo, valor):
        self.palo=palo
        self.valor=valor
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
        
        

#_____________________________________________________________________JUEGO 
class JuegoGuerra:
    
    def __init__(self):
        
        
        self.cartas_en_guerra=LDE()
        
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
        self.turnos=1
    
    
    def iniciar_juego(self):
        resultado=''
        
        while resultado=='' and self.turnos < 10000:
            
            resultado=self.duelo()
            self.turnos+=1
        
        if resultado==1:
            print('gana jugador 1')
            
        elif resultado==2:
            print('gana jugador 2')
        
        else:
            print('EMPATE')
        
        
        
    def duelo(self):
        
        try:
            carta1=self.jugador1.sacar_fin()
        except:
            return 2
        
        try:
            carta2=self.jugador2.sacar_fin()
        except:
            return 1
        
        
        
        if carta1>carta2:
            self.jugador1.agregar_in(carta1)
            self.jugador1.agregar_in(carta2)
            
        elif carta1<carta2:
            self.jugador2.agregar_in(carta1)
            self.jugador2.agregar_in(carta2)
        
        elif carta1==carta2:
            return 2
            # self.cartas_en_guerra.agregar_al_final(carta2)
            # self.cartas_en_guerra.agregar_al_final(carta2)
            # self.guerra()
        
        if carta1.boca_arriba==False:
            carta1.voltear()
        if carta2.boca_arriba==False:
            carta2.voltear()
       
        
        carta1=str(carta1)+' '+str(carta2)
        print(carta1.center(60))
        
        return ''
    


    def guerra(self):
        """Se ejecuta si hay un empate en el duelo"""
        salir=False
        
        while not salir:
            
            #repartimos 3 cartas boca abajo de cada jugador
            for i in range(3):
                
                #intentamos sacar carta del jugador 1, si no tiene cartas gana el jugador 2
                try:
                    self.cartas_en_guerra.agregar_al_final(self.jugador1.sacar_fin())
                except:
                    return 2
                
                #si el jugador 2 se queda sin cartas, gana el jugador 1
                try:
                    self.cartas_en_guerra.agregar_al_final(self.jugador2.sacar_fin())
                except:
                    return 1
            
            
                #Tratamos de sacar cartas para comparar
                
                carta1=None
                carta2=None
                
                try:
                    carta1=self.jugador1.sacar_fin()
                except:
                    return 2
                
                try:
                    carta2=self.jugador2.sacar_fin()
                except:
                    return 1
                
                
                self.cartas_en_guerra.agregar_al_final(carta1)
                self.cartas_en_guerra.agregar_al_final(carta2)
                
                if carta1>carta2:
                    for carta in self.cartas_en_guerra:
                        if carta.boca_arriba == True:
                            carta.voltear()
                            self.jugador1.agregar_in(carta)
                            salir=True
                            
                            
                elif carta1<carta2:
                    for carta in self.cartas_en_guerra:
                        if carta.boca_arriba == True:
                            carta.voltear()
                            self.jugador2.agregar_in(carta)
                            salir=True
        
        print(self.cartas_en_guerra)
        self.cartas_en_guerra=LDE()
        return ''
            
                
            
        
         
    
    #def guerra(self,carta1,carta2):
        
        disputadas=Cola_doble()
        
        #boca arriba las cartas que se comparan
        carta1.voltear()
        carta2.voltear()
        
        
        disputadas.agregar_fin(carta1)
        disputadas.agregar_fin(carta2)
        
        
        
        #si algun jugador se queda sin cartas, pierde la partida (cartas boca abajo)
        for i in range(3):
            try:
                disputadas.agregar_fin(self.jugador1.sacar_fin())
            except:
                return 1
            
            try:
                disputadas.agregar_fin(self.jugador2.sacar_fin())
            except:
                return 2
        
        
        #saco cartas para comparar, si es que tienen cartas disponibles
        try:
            carta1=self.jugador1.sacar_fin()
        except:
            return 1
        
        
        try:
            carta2=self.jugador2.sacar_fin()
        except:
            return 2
        
        
        #volteo las cartas a comparar
        carta1.voltear()
        carta2.voltear()
        
        
        disputadas.agregar_fin(carta1)
        disputadas.agregar_fin(carta2)
        
        if carta1>carta2:
            pass
        
        print(disputadas)
        
        
        if carta1>carta2:
            pass
        
        
        
        
        
        
        
        
        
        


if __name__ == '__main__':
    
    juego=JuegoGuerra()
    
    
    
    
    juego.iniciar_juego()
    
    print('tamaño 1 ',len(juego.jugador1))
    print('tamaño 2 ',len(juego.jugador2))
    print('turnos: ',juego.turnos)
    
    
    
    # print('JUGADOR 1:')
    # print(juego.jugador1)
    # print('Tamaño: ',len(juego.jugador1))
    
    # print('')
    # print('JUGADOR 2')
    # print(juego.jugador2)
    # print('Tamaño: ',len(juego.jugador2))
    
    
    # print('')
    
    # juego.duelo()
    
    # print('')
    
    # print('JUGADOR 1:')
    # print(juego.jugador1)
    # print('Tamaño: ',len(juego.jugador1))
    
    # print('')
    # print('JUGADOR 2')
    # print(juego.jugador2)
    # print('Tamaño: ',len(juego.jugador2))
    
    
  
    
 
    
    
    

    
    
   
