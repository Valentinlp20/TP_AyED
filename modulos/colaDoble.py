# -*- coding: utf-8 -*-


from ListaDobleEnlazada import ListaDobleEnlazada as LDE

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
    
    
    