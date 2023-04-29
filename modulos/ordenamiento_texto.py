# -*- coding: utf-8 -*-

import time

def ordenamiento_mezcla(lista):
    """aplica algoritmo de merge sort sobre una lista de python y retorna la lista ordenada"""
    
    #si la lista tiene mas de un elemento se divide por la mitad
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        
        #llamada recursiva para seguir dividiendo las sublistas
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)
        
        
        
        
        
        indice_actual_izquierdo = indice_actual_derecho = indice_resultado = 0
        
        
        #ordenar y reagrupar 
        
        #recorremos ambas mitades, y comparamos elementos para ordenarlos en la lista
        while indice_actual_izquierdo < len(izquierda) and indice_actual_derecho < len(derecha):
            if izquierda[indice_actual_izquierdo] < derecha[indice_actual_derecho]:
                lista[indice_resultado] = izquierda[indice_actual_izquierdo]
                indice_actual_izquierdo += 1
            else:
                lista[indice_resultado] = derecha[indice_actual_derecho]
                indice_actual_derecho += 1
            indice_resultado += 1
            
        while indice_actual_izquierdo < len(izquierda):
            lista[indice_resultado] = izquierda[indice_actual_izquierdo]
            indice_actual_izquierdo += 1
            indice_resultado += 1
            
        while indice_actual_derecho < len(derecha):
            lista[indice_resultado] = derecha[indice_actual_derecho]
            indice_actual_derecho += 1
            indice_resultado += 1
    return lista






    
def ordenamiento_previo(lista, b):
    """ordena individualmente segmentos de longitud B dentro de una lista"""
    
    #creo un bucle para recorrer la lista en saltos de tamaño B
    for i in range(0, len(lista), b):
        #selecciono el segmento a ordenar
        segmento = lista[i:i+b]
        
        #si el segmento esta completo, lo ordenamos
        if len(segmento) == b:
            segmento.sort()
            
        #reemplazo los valores en la lista original con los del segmento ordenado
        lista[i:i+b] = segmento
    
      

if __name__ == '__main__':
    
    datos=[]
    print('ordenando datos. . .')
    with open ('datos.txt','r',encoding='utf-8') as archivo:
    
        
        for dato in archivo:
            
            datos.append(int(dato))
            
    
    inicio=time.time()
    datos_ordenados=ordenamiento_mezcla(datos)
    fin=time.time()
    print('Datos ordenados! ', round(fin-inicio,2), ' segundos')
    with open('datos_ordenados.txt','w',encoding='utf-8') as archivo:
        
        for numero in datos_ordenados:
            archivo.write(str(str(numero)+'\n'))
    
    
    
    
    
        
