# -*- coding: utf-8 -*-

from modulos.ListaDobleEnlazada import ListaDobleEnlazada as le
from modulos.ListaDobleEnlazada import Nodo

lista=le()

x=[i for i in range(15)]

for item in x:
    lista.agregar_al_final(item)
    
print(lista)



lista2=le()

x=[6,5,8,2,1,3,0,1,0,3,5,4]
for item in x:
    lista2.agregar_al_final(item)
    
print(lista2)
print('Tamaño: ',lista2.tamanio,'\n')

lista2.insertar(99, lista2.tamanio-1)
print(lista2)
print('Tamaño: ',lista2.tamanio)

print('Cola: ',lista2.cola)
print('valor siguiente al ante ultimo nodo:', lista2.cola.anterior.siguiente,'\n')

nodo_actual=lista2.cabeza

print('RECORRIDO CON WHILE')
while nodo_actual.siguiente:
    nodo_anterior = nodo_actual
    nodo_actual = nodo_actual.siguiente
    valor = nodo_anterior.dato
    print(valor)

print('_____________________________________')
print('RECORRIDO CON FOR ')
for nodo in lista2:
    print(nodo)

