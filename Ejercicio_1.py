# -*- coding: utf-8 -*-

from modulos.ListaDobleEnlazada import ListaDobleEnlazada as le
import matplotlib.pyplot as plt
from random import randint
from modulos.ordenamiento_texto import ordenamiento_mezcla,ordenamiento_previo
import time



#Medimos tiempos de ejecucion del algoritmo de ordenamieno para la lista doblemente enlazada

# x_cantidad_de_elementos=[]
# y_tiempo_de_ejecucion=[]

# for i in range(100, 5000, 100 ):
#     x_cantidad_de_elementos.append(i)
    
#     #creo una lista de longitud i
#     elementos=[randint(50,15000) for x in range(i)]
#     lista=le()
#     for i in range (len(elementos)):
#         lista.agregar_al_final(elementos[i])
        
#     inicio=time.time()
    
#     lista.ordenar()
    
#     final=time.time()
    
#     y_tiempo_de_ejecucion.append(round(final-inicio,2))

# plt.plot(x_cantidad_de_elementos,y_tiempo_de_ejecucion)

# plt.xlabel('Cantidad de elementos en la lista')
# plt.ylabel('segundos')
# plt.title('tiempo de ejecucion algoritmo de ordenamiento')

# plt.show()


#Medimos tiempos para el algoritmo de merge sort, con y sin ordenamiento previo

x_cantidad_de_elementos=[]
y_tiempo_de_ejecucion=[]

for i in range(100, 50000, 100 ):
    x_cantidad_de_elementos.append(i)
    
    #creo una lista de longitud i
    elementos=[randint(50,15000) for x in range(i)]
    
    ordenamiento_previo(elementos, 100)
    inicio=time.time()
    
    ordenamiento_mezcla(elementos)
    
    final=time.time()
    y_tiempo_de_ejecucion.append(round(final-inicio,2))
    
    
plt.plot(x_cantidad_de_elementos,y_tiempo_de_ejecucion)
plt.xlabel('Cantidad de elementos en la lista')
plt.ylabel('segundos')
plt.title('tiempo de ejecucion algoritmo de ordenamiento mezcla,  con ordenamiento previo')
plt.show()
    