# -*- coding: utf-8 -*-

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
        
        suma=self.copiar()
        suma.cola.siguiente, otro.cabeza.anterior= otro.cabeza, suma.cola
        suma.cola=otro.cola
        
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
        
    def insertar(self, posicion, item):
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
        """ Ordena la lista utilizando el algoritmo de ordenamiento burbuja"""
        
        intercambiado = True
        while intercambiado:
            intercambiado = False
            nodo_actual = self.cabeza
            
            while nodo_actual is not None and nodo_actual.siguiente is not None:
                if nodo_actual.dato > nodo_actual.siguiente.dato:
                    # Intercambia los valores de los nodos
                    nodo_actual.dato, nodo_actual.siguiente.dato = nodo_actual.siguiente.dato, nodo_actual.dato
                    intercambiado = True
                nodo_actual = nodo_actual.siguiente       
            
            
    def concatenar(self,otro):
         return self+otro
            
            
            

        
            
    def extraer(self, posicion=None ):
        """Retorna un nodo para una posicion dada, y lo elimina de la lista, si no se especifica
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
            
            return nodo
        
        
        
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
                return actual
            
            elif actual.anterior == None:
                #si el elemento a extraer es el primero de la lista, el nodo que sigue debe tener None como anterior
                # y la cabeza de la lista cambia
                
                actual.siguiente.anterior=None
                self.cabeza=actual.siguiente
                self.tamanio-=1
                return actual
                         
            else:
                #si el elemento se situa en un lugar de la lista distinto a los extremos
                
                actual.siguiente.anterior=actual.anterior
                actual.anterior.siguiente=actual.siguiente
                self.tamanio-=1
                
                return actual
        




    def copiar(self):
        """Devuelve una copia de la lista"""
        
        lista_auxiliar=ListaDobleEnlazada()
        
        for nodo in self:
            lista_auxiliar.agregar_al_final(nodo.dato)
        
        return lista_auxiliar
    
    
    def invertir(self):
        
        for i in range(self.tamanio-1):
            dato=self.extraer().dato
            self.insertar(i, dato)
        dato=self.extraer(self.tamanio-2)
        self.agregar_al_final(dato.dato)
        
        
        
            
            
    


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
        
        return valor
        
        
        
        
        
