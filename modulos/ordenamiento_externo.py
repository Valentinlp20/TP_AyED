# -*- coding: utf-8 -*-

import os


def generar_archivos(origen, b):
    
    print('Generando archivos temporales. . .')
    with open(origen, 'r') as archivo_origen:
        total_archivos = 0
        archivo_destino = None
        
        for indice, linea in enumerate(archivo_origen):
            if indice % b == 0:
                if archivo_destino:
                    archivo_destino.close()

                nombre_archivo = f"temp_{total_archivos}.txt"
                archivo_destino = open(nombre_archivo, 'w')
                total_archivos += 1

            archivo_destino.write(linea)
            
        if archivo_destino:
            archivo_destino.close()

    print(f"Se generaron {total_archivos} archivos.")
    return total_archivos


def ordenar_archivos(num_archivos):
    print('Ordenando archivos temporales. . .')
    for i in range(num_archivos):
        nombre_archivo = f"temp_{i}.txt"
        
        # Lee el contenido del archivo
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.readlines()

        # Convierte los numeros a enteros y ordena la lista
        numeros = [int(num) for num in contenido]
        numeros.sort()

        # Escribe el archivo ordenado
        with open(nombre_archivo, 'w') as archivo:
            for num in numeros:
                archivo.write(str(num) + '\n')
    print('archivos temporales ordenados!!')
    
def mezcla_directa_archivos(archivo1, archivo2, archivo_salida):
    with open(archivo1, 'r') as archivo1, open(archivo2, 'r') as archivo2:
        linea1 = archivo1.readline().strip()
        linea2 = archivo2.readline().strip()
        resultado = []

        while linea1 and linea2:
            numero1 = int(linea1)
            numero2 = int(linea2)
            if numero1 < numero2:
                resultado.append(numero1)
                linea1 = archivo1.readline().strip()
            else:
                resultado.append(numero2)
                linea2 = archivo2.readline().strip()

        # Agregar los elementos restantes de archivo1 si quedan
        while linea1:
            resultado.append(int(linea1))
            linea1 = archivo1.readline().strip()

        # Agregar los elementos restantes de archivo2 si quedan
        while linea2:
            resultado.append(int(linea2))
            linea2 = archivo2.readline().strip()

    # Escribir el resultado ordenado en el archivo de salida
    with open(archivo_salida, 'w') as archivo_salida:
        for elemento in resultado:
            archivo_salida.write(str(elemento) + "\n")



def mezclar_todo(numero_total_temporales):
    print('Generando resultados...')
    
    conteo = numero_total_temporales
    indice = 0

    while numero_total_temporales > 1:
        
        archivo1=f'temp_{indice}.txt'
        archivo2=f'temp_{indice+1}.txt'
        archivo_salida=f'temp_{conteo}.txt'
        mezcla_directa_archivos(archivo1, archivo2, archivo_salida)
        os.remove(archivo1)
        os.remove(archivo2)
        numero_total_temporales-=1
        conteo+=1
        indice+=2
    
    os.rename(f'temp_{conteo-1}.txt', 'resultado.txt')
        

    print('Proceso de mezcla completo.')
       
if __name__ =="__main__":
    
    
    ordenar_archivos(generar_archivos('datos.txt', 1000))
    mezclar_todo(500)