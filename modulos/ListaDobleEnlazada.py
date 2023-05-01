# -*- coding: utf-8 -*-
from random import randint


class Nodo ():
    
    def __init__(self,dato=None):
        
        self.dato=dato
        self.siguiente=None
        self.anterior=None
        
        
    def __str__(self):
        dato=str(self.dato)
        return str(dato)
    
    def __lt__(self,otro):
        return self.dato < otro.dato 
   
    
    
    
#__________________________________________________________________
#__________________________________________________________________
    
    

class ListaDobleEnlazada:
    
    def __init__(self):
        self.tamanio=0
        self.cabeza= None
        self.cola=None
        
    def __len__(self):
        return self.tamanio
    
    def __str__(self):
        nodo=self.cabeza
        resultado="["   
     
        for i in range (self.tamanio):        
                resultado+=str(nodo.dato)+", "
                nodo=nodo.siguiente
        resultado+="]"    
        resultado=resultado.replace(", ]","]")
        return resultado 
        
    def __iter__(self):
        " Devuelve el iterador de la lista. "
        return IteradorListaEnlazada(self.cabeza)
            
   

    
    def __add__(self,otro):
        
        """recibe una lista y la concatena a la lista original, retorna otra lista
        doblemente enlazada como resultado, sin alterar las listas originales"""
        
        suma=self.copiar()
        suma2=otro.copiar()
        
        suma.cola.siguiente=suma2.cabeza
        suma2.cabeza.anterior=suma.cola
        suma.cola=suma2.cola
        
        suma.tamanio=suma.tamanio+otro.tamanio
        
        return suma
        
        
        
        
    
    def tamanio(self):
        return self.tamanio


    def esta_vacia(self):
        """Devuelve TRUE si la lista se encuentra vacia"""
        return self.cabeza==None

    def agregar_al_inicio(self,dato):
        """Agrega un elemento al inicio de la lista"""
        
        if self.esta_vacia():
            nodo=Nodo(dato)
            self.cabeza= nodo
            self.cola=nodo
            self.tamanio+=1
        
        else:
            nodo=Nodo(dato)
            
            #que el elemento siguiente del nuevo nodo sea el que estaba primero en la lista
            nodo.siguiente=self.cabeza
            
            # nodo.anterior=self.cabeza.anterior
            self.cabeza.anterior=nodo
            self.cabeza=nodo
            self.tamanio+=1
            
    def agregar_al_final(self,dato):
        """Agrega un elemento al final de la lista"""
        
        if self.esta_vacia():
            nodo=Nodo(dato)
            self.cabeza= nodo
            self.cola=nodo
            self.tamanio+=1
        else:
            nodo=Nodo(dato)
            nodo.anterior=self.cola
            self.cola.siguiente=nodo
            self.cola=nodo
            self.tamanio+=1
        
    def insertar(self,item, posicion):
        """inserta un item a la lista en la posicion seleccionada"""
        
        posicion=int(posicion)
        item=Nodo(item)
        
        if posicion == 0:
            self.agregar_al_inicio(item.dato)
        
        elif posicion == self.tamanio -1:
            self.agregar_al_final(item.dato)
            
        else:
            nodo_actual=self.cabeza
            for i in range (posicion):
                nodo_actual=nodo_actual.siguiente
        
            nodo_actual.anterior.siguiente=item
            item.anterior=nodo_actual.anterior
            nodo_actual.anterior=item
            item.siguiente=nodo_actual
            self.tamanio+=1
            

            
    def ordenar(self):    
        """ Ordena la lista utilizando el algoritmo de ordenamiento insercion"""
        
        
        #si la lista esta vacia entonces ya esta ordenada
        if self.esta_vacia():                                                   # O(1)
            return
        
        
        nodo_actual =self.cabeza.siguiente                                      # O(1)
        while nodo_actual is not None:                                          # O(n)
            dato = nodo_actual.dato                                             # O(n)
            nodo_comparar = nodo_actual.anterior                                # O(n)
            
            while nodo_comparar is not None and nodo_comparar.dato > dato:      # O(n**2)
                nodo_comparar.siguiente.dato = nodo_comparar.dato               # O(n**2)
                nodo_comparar = nodo_comparar.anterior                          # O(n**2)
            
            if nodo_comparar is None:                                           # O(n)
                self.cabeza.dato = dato                                         # O(n)
            else:
                nodo_comparar.siguiente.dato = dato                             # O(n)
            
            nodo_actual = nodo_actual.siguiente                                 # O(n)
            
            
                
    def concatenar(self,otro):
            
            suma=otro.copiar()
            
            self.cola.siguiente=suma.cabeza
            suma.cabeza.anterior=self.cola
            self.cola=suma.cola
            
            self.tamanio+=otro.tamanio
         
         
            
            
            

        
            
    def extraer(self, posicion=None ):
        """Retorna el dato de un nodo para una posicion dada, y lo elimina de la lista, si no se especifica
        la posicion, retorna el ultimo elemento de la lista"""
      
        
        
        if posicion== None or posicion == -1:
            # Si no se especifica una posicion o es -1 se asigna el ultimo elemento de la lista         
            posicion= self.tamanio - 1
            
            
            
        if not 0 <= posicion < self.tamanio:
            # si la posicion esta fuera del rango se lanza una excepcion
            
            raise IndexError("La posicion ingresada esta fuera del rango")
            
        
        if self.tamanio == 1:
            nodo=self.cabeza
            
            self.cabeza=None
            self.cola=None
            self.tamanio-=1
            
            return nodo.dato
        
        
        
        else:
            #Nos situamos en el nodo correspondiente a la posicion dada
            
            actual=self.cabeza
            for i in range(posicion):
                actual=actual.siguiente
            
            
            if actual.siguiente== None :
                #si el elemento es el ultimo de la lista, al nodo anterior le debe seguir None
                # y la cola de la lista cambia
                
                actual.anterior.siguiente= None
                self.cola=actual.anterior
                self.tamanio -=1
                return actual.dato
            
            elif actual.anterior == None:
                #si el elemento a extraer es el primero de la lista, el nodo que sigue debe tener None como anterior
                # y la cabeza de la lista cambia
                
                actual.siguiente.anterior=None
                self.cabeza=actual.siguiente
                self.tamanio-=1
                return actual.dato
                         
            else:
                #si el elemento se situa en un lugar de la lista distinto a los extremos
                
                actual.siguiente.anterior=actual.anterior
                actual.anterior.siguiente=actual.siguiente
                self.tamanio-=1
                
                return actual.dato
        




    def copiar(self):
        """Devuelve una copia de la lista"""
        
        lista_auxiliar=ListaDobleEnlazada()
        
        for nodo in self:
            lista_auxiliar.agregar_al_final(nodo)
        
        return lista_auxiliar
    
    
    def invertir(self):
        """invierte el orden de los elementos dentro de la lista"""
        
        ciclos=int(self.tamanio/2)
        izquierda=self.cabeza
        derecha=self.cola
        
        for i in range(ciclos):
            
            #intercambiamos los valores
            izquierda.dato, derecha.dato = derecha.dato, izquierda.dato
            izquierda=izquierda.siguiente
            derecha=derecha.anterior
        
        
        
        
        
        
            
            
    


#_____________________________________________________________________________
#_______________________ITERADOR_____________________________________________


class IteradorListaEnlazada:
    
    def __init__(self,listaDoble):
        
        self.actual=listaDoble
        
    def __next__(self):
        
        if not self.actual:
            raise StopIteration
            
        valor= self.actual
        self.actual=self.actual.siguiente
        
        return valor.dato
        
        


if __name__ =='__main__':
        
    
        lista=ListaDobleEnlazada()
        valores=[randint(0,356) for x in range(50)]
        for valor in valores:
            lista.agregar_al_final(valor)
        
        
        print(lista)
        
        lista.ordenar()
        
        print(lista)
            
        
