# -*- coding: utf-8 -*-


from modulos.ordenamiento_texto import ordenamiento_mezcla, ordenamiento_previo
import unittest
from random import randint
import os


class Test_ordenamiento(unittest.TestCase):
    """"test para las funciones de ordenamiento por mezcla binaria"""
    
    def setUp(self):
        #Lista de valores aleatorios, agregando 2 que estan por fuera para saber de antemano el mayor y menor
        self.lista_desordenada=[randint(2**20, 2**23) for x in range(300)]+[8,2**25]
        
      
    
    
    def test_ordenamiento_previo(self):
        """probamos el ordenamiento por bloques"""
        
        ordenamiento_previo(self.lista_desordenada,5)
        
        
        lista_auxiliar=[]
        
        for i in range(0, len(self.lista_desordenada),5):
            
            
            
            lista_auxiliar=self.lista_desordenada[i:i+5]
            lista_auxiliar.sort()
            
            
            #comprobamos que cada bloque este ordenado
            self.assertEqual(self.lista_desordenada[i:i+5], lista_auxiliar,'ordenamiento en bloques no ordeno correctamente')
    
    
    def test_mayor_menor(self):
        """Comprobamos que los valores menor y mayor esten en sus respectivos extremos de la lista"""
        lista_ordenada=ordenamiento_mezcla(self.lista_desordenada)
        
        self.assertEqual(lista_ordenada[-1], 2**25)
        self.assertEqual(lista_ordenada[0], 8)
        
        
    def test_ordeamiento_mezcla(self):
        """"comprobamos que la lista este ordenada"""
        
        lista_ordenada=ordenamiento_mezcla(self.lista_desordenada)
        
        
        for i in range (len(lista_ordenada)):
            siguiente=0
            actual=lista_ordenada[i]
            try:
                siguiente=lista_ordenada[i+1]
                self.assertTrue(actual<siguiente)
            except:
                pass
        
    def test_tamaño_archivo(self):
        """Generamos un archivo de texto con la lista desordenada y ordenada para verificar que ambas tengan el mismo tamaño"""
        
        lista_ordenada=ordenamiento_mezcla(self.lista_desordenada)
       
       
        
        with open('testing_desordenado','w',encoding='utf-8') as archivo:
            
            for i in range(len(self.lista_desordenada)):
                archivo.write(str  (str(self.lista_desordenada[i])+'\n')   )
                
        tamanio_desordenado=os.path.getsize('testing_desordenado')
        
        with open('testing_ordenado','w',encoding='utf-8') as archivo:
            
            for i in range(len(lista_ordenada)):
                
                archivo.write(str(   str(lista_ordenada[i])+'\n'))
                
        tamanio_ordenado=os.path.getsize('testing_ordenado')
        
        self.assertEqual(tamanio_ordenado, tamanio_desordenado,'Los tamaños de los archivos no coinciden')        
        
            
                
                
            



if __name__ == "__main__":
    unittest.main()