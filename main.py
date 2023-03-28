# -*- coding: utf-8 -*-

from modulos.LDE import ListaDobleEnlazada as le

lista=le()

x=[i for i in range(15)]

for item in x:
    lista.agregar_al_final(item)
    


print (lista)

lista.insertar(lista.tamanio-1, 60)

lista.insertar(0, -20)


print(lista)
print(len(lista))


lista2=le()

for letra in ['a','h','o','p']:
    lista2.agregar_al_final(letra)

print(lista2)

print('')

print (lista+lista2)

lista2.invertir()

print(lista2)