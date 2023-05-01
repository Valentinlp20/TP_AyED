# -*- coding: utf-8 -*-


from ListaDobleEnlazada import ListaDobleEnlazada as LDE
import random


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



#_______________________________________________________________COLA DOBLE


class Cola_doble:
    """La cola doble, en este caso, representaría el mazo de cartas de cada jugador"""
    
    def __init__(self):
        
        self.lista=LDE()
       
    
   
    def agregar_in(self, item):
        """Para agregar cartas al inicio del mazo, que para este caso consideré que
        el mazo comiense de abajo hacia arriba, asi que agrega una carta por abajo del mazo"""
        self.lista.agregar_al_inicio(item)
        
    
    
    def agregar_fin(self,item):
        """Agrega una carta al final del mazo, que acá seria como agregar una carta en la parte
        de arriba, igual que como se agregan elementos en una pila"""
        self.lista.agregar_al_final(item)
        
    
    
    def sacar_in(self):
        """Extrae la carta de la parte baja del mazo """
        
        return self.lista.extraer(0)
    
    def sacar_fin(self):
        """Extrae un elemento del final del mazo, o la parte de arriba del mismo"""
        
        return self.lista.extraer(self.lista.tamanio -1)
    
    def __str__(self):
        return str(self.lista)
    
    def __len__(self):
        return self.lista.tamanio
    
    
    
        
    
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
        
        

#_____________________________________________________________________JUEGO 
class JuegoGuerra:
    
    def __init__(self,random_seed=None):
        
        
        #atributos auxiliares para imprimir el juego por consola
        #__________________________________________________________________
        self.actual_jugador1=''
        self.actual_jugador2=''
        self.actual_disputadas='' 
        #__________________________________________________________________
        
        
        
        
        
        
        #Creacion del Mazo
        #__________________________________________________________________
        valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        palos = ['♠', '♥', '♦', '♣']
        
        # random.shuffle(valores)
        # random.shuffle(palos)
        
        cartas=[]
        
        for palo in palos:
            for valor in valores:
                carta=Carta(palo, valor)
                # cartas.agregar_fin(carta)
                cartas.append(carta)
        #__________________________________________________________________
        
        if random_seed!=None:
            random.seed(random_seed)
            
        random.shuffle(cartas)
        mazo=Cola_doble()
        
        for carta in cartas:
            mazo.agregar_fin(carta)
        
        
        self.mazo= mazo
        
        
        
        
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
        """inicia el juego, juega partidas hasta tener un ganador o empate"""
        
        resultado=''
        
        #mientras no haya un ganador y se hayan jugado menos de 10 mil turnos,
        # se siguen sacando cartas para duelo
        while resultado=='' and self.turnos < 10000:
            
            resultado=self.duelo()
            
            
            #condicional para evitar que el ultimo turno se imprima 2 veces
            if resultado=='':
                self.mostrar()
                self.turnos+=1
            
            #comprobamos que no se hayan perdido cartas
            if len(self.jugador1) + len(self.jugador2) != 52: 
                print("TURNO: ",self.turnos)
                print('JUGADOR 1: ',len(self.jugador1))
                print('JUGADOR 2: ',len(self.jugador2))
                print(self.ultima_accion)
                raise ValueError('Se perdieron o agregaron cartas! !')
                
            
        
        if resultado==1:
            self.registrar_mazos()
            self.mostrar()
            print('***** jugador 1 gana la partida *****'.center(60))
            
        elif resultado==2:
            self.registrar_mazos()
            self.mostrar()
            print('***** jugador 2 gana la partida *****'.center(60))
        
        else:
            print('***** EMPATE *****'.center(60))
        
        
        
    def duelo(self):
        
        """Toma una carta de cada jugador para comparar, retorna el valor entero 1 o 2 dependiendo
        de si se decidio un ganador en el duelo, de lo contrario retorna un string vacío
        para indicar que el juego sigue"""
        
        
        
        #intenta sacar carta del jugador 1, si no se puede, es que se quedó sin cartas
        #y gana el jugador 2
        try:
            carta1=self.jugador1.sacar_fin()
        except:
            return 2
        
        #intento sacar carta del jugador 2
        try:
            carta2=self.jugador2.sacar_fin()
        except:
            self.jugador1.agregar_in(carta1)
            return 1
        
        
        
        self.registrar_mazos()              #Los mazos se guardan en el estado actual
        
        
        
        if carta1>carta2:
            self.jugador1.agregar_in(carta1)
            self.jugador1.agregar_in(carta2)  
            
        elif carta1<carta2:
            self.jugador2.agregar_in(carta1)
            self.jugador2.agregar_in(carta2)
        
        elif carta1==carta2:
            return self.guerra(carta1,carta2)
            
        
        #Voltea las cartas para mostrarlas
        if carta1.boca_arriba==False:
            carta1.voltear()
        if carta2.boca_arriba==False:
            carta2.voltear()
       
        
        cartas_en_duelo=str(carta1)+' '+str(carta2)
        self.actual_disputadas=cartas_en_duelo
        
        
        #volvemos a ponerlas boca abajo 
        if carta1.boca_arriba==True:
            carta1.voltear()
        if carta2.boca_arriba==True:
            carta2.voltear()
        
        if len(self.jugador1)==0:
            return 2
        elif len(self.jugador2)==0:
            return 1
        else:
            return ''
    


    def guerra(self,carta1,carta2,cartas_en_guerra=None):
        """Se ejecuta si hay un empate en el duelo"""
        
        
        
        
        if cartas_en_guerra==None:
            cartas_en_guerra=LDE()
        
        if carta1.boca_arriba==False:
            carta1.voltear()
        if carta2.boca_arriba==False:
            carta2.voltear()
        
        
        cartas_en_guerra.agregar_al_final(carta1)
        cartas_en_guerra.agregar_al_final(carta2)
        
        
        #sacamos 3 cartas de cada jugador de manera alternada        
        for i in range(3):
            
                # Si algun jugador se queda sin cartas, pierde el juego             
                try:
                    cartas_en_guerra.agregar_al_final(self.jugador1.sacar_fin())
                    self.actual_disputadas=cartas_en_guerra
                    self.registrar_mazos()
                except:
                    self.registrar_mazos()
                    self.registrar_guerra(cartas_en_guerra)
                    for carta in cartas_en_guerra:
                        self.jugador2.agregar_in(carta)
                    return 2
                
                try:
                    cartas_en_guerra.agregar_al_final(self.jugador2.sacar_fin())
                    self.registrar_mazos()
                    self.actual_disputadas=cartas_en_guerra
                except:
                    self.registrar_mazos()
                    self.registrar_guerra(cartas_en_guerra)
                    
                    for carta in cartas_en_guerra:
                        self.jugador1.agregar_in(carta)
                    return 1
        
        #Si no hubo problema al sacar las boca abajo, comprobamos que ambos tengan cartas
        #para comparar en la guerra
        
        carta_jugador1=None
        carta_jugador2=None
        
        try:
            carta_jugador1=self.jugador1.sacar_fin()
            
        except:
            self.registrar_mazos()
            self.registrar_guerra(cartas_en_guerra)
            for carta in cartas_en_guerra:
                
                self.jugador2.agregar_in(carta)
            return 2
        
        try:
            carta_jugador2=self.jugador2.sacar_fin()
            
        except:
            
            cartas_en_guerra.agregar_al_final(carta_jugador1)
            self.registrar_mazos()
            self.registrar_guerra(cartas_en_guerra)
            for carta in cartas_en_guerra:
                
                self.jugador1.agregar_in(carta)
            return 1
        
        
        #Si ambos jugadores tenian cartas suficientes, comparamos la carta del jugador 1 con la del jugador 2
        
        ganador=None
        
        
        #gana el jugador 1
        if carta_jugador1 > carta_jugador2:
            
            carta_jugador1.voltear()
            carta_jugador2.voltear()
            
            cartas_en_guerra.agregar_al_final(carta_jugador1)
            cartas_en_guerra.agregar_al_final(carta_jugador2)                    
            ganador=self.jugador1
        
        #gana el jugador 2
        elif carta_jugador2 > carta_jugador1:
            
            carta_jugador1.voltear()
            carta_jugador2.voltear()
            
            cartas_en_guerra.agregar_al_final(carta_jugador1)
            cartas_en_guerra.agregar_al_final(carta_jugador2)        
            ganador=self.jugador2
        
        #en caso de que ambas cartas sean iguales
        else:
            return self.guerra(carta_jugador1, carta_jugador2, cartas_en_guerra)
        
        
        
        
        
        self.registrar_mazos()
        self.registrar_guerra(cartas_en_guerra)
        
        
        
        
        
        # repartimos las cartas al ganador
        
        for carta in cartas_en_guerra:
            if carta.boca_arriba==True:
                carta.voltear()
            ganador.agregar_in(carta)
        
        
        #definimos si el juego continua
        if len(self.jugador1) ==0:
            return 2
        elif len(self.jugador2)==0:
            return 1
        else:
            return ''
                
        
        
        
            
       #_______________________________________________________________________
       #
       #______________________FUNCIONES PARA IMPRIMIR EN CONSOLA_______________
       #_______________________________________________________________________
        
        
    def registrar_mazos(self):
            """guardo en strings los mazos actuales de cada jugador"""
            
            
            self.actual_jugador1=str(self.jugador1)
            self.actual_jugador2=str(self.jugador2)
            
            #quitamos corchetes
            self.actual_jugador1, self.actual_jugador2= self.actual_jugador1.replace('[',''), self.actual_jugador2.replace('[','')
            self.actual_jugador1, self.actual_jugador2= self.actual_jugador1.replace(']',''), self.actual_jugador2.replace(']','')
            
            
            #quitamos comas
            self.actual_jugador1=self.actual_jugador1.replace(',','')
            self.actual_jugador2=self.actual_jugador2.replace(',','')
            
            
            
    def mostrar(self):
           print('\n') 
           print('_____________________________________________________')
           print('Turno: ',self.turnos)
           print('Jugador 1:')
           print(self.actual_jugador1)
           self.actual_disputadas=str(self.actual_disputadas).replace('[','')
           self.actual_disputadas=str(self.actual_disputadas).replace(']','')
           self.actual_disputadas=str(self.actual_disputadas).replace(',','')
           print('\n',self.actual_disputadas,'\n')
           print('Jugador 2:')
           print(self.actual_jugador2)
           print('_____________________________________________________')
        
        
        
        
        
    def registrar_guerra(self,cartas_en_guerra):
        #Guardo cartas en guerra en un string
        #_____________________________________________________________
        self.actual_disputadas=str(cartas_en_guerra)
        self.actual_disputadas=self.actual_disputadas.replace('[','')
        self.actual_disputadas=self.actual_disputadas.replace(']','')
        #_____________________________________________________________

if __name__ == '__main__':
    
    juego=JuegoGuerra()
    
    

    juego.iniciar_juego()
   
    
    
    
    
    
    
  
    
 
    
    
    

    
    
   
