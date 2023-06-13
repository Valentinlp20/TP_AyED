# -*- coding: utf-8 -*-



import unittest
import os
from modulos.generar_archivo_de_texto import crear_archivo_de_datos
from modulos.ordenamiento_externo import *



class Test_Ordenamiento_mezcla(unittest.TestCase):
    
    def setUp(self):
        self.resultados=open('resultado.txt','r')
    
    
    
    def test_tamaño(self):
        """Comprobamos que el archivo resultante tenga el mismo tamaño
        que el archivo original"""
        
        tamanio_original=os.path.getsize('datos.txt')
        tamanio_resultante=os.path.getsize('resultado.txt')
        
        self.assertEqual(tamanio_original, tamanio_resultante)
    
    def test_ordenado(self):
        """Compruebo que el archivo resultante este ordenado"""
        
        actual=int(self.resultados.readline().strip())
        siguiente=int(self.resultados.readline().strip())
        
        while siguiente:
            self.assertTrue(actual <= siguiente)
            
            actual=siguiente
            try:
                siguiente=int(self.resultados.readline().strip())
            except:
                break
            
    
    def tearDown(self):
        self.resultados.close()


if __name__ == "__main__":
    
    
        
    
    #se divide el archivo principal en bloques de tamaño B
    total_archivos= generar_archivos('datos.txt', b=1000)
    
    #se ordena individualmente cada bloque
    ordenar_archivos(total_archivos)
    
    #se mezclan en un archivo resultante
    mezclar_todo(total_archivos)
    
    unittest.main()    


