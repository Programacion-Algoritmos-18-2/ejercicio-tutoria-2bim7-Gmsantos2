"""
    Ejemplo tomado de 
    http://www.pythondiario.com/2018/08/ordenamiento-por-mezcla-merge-sort.html
"""
from combinacion import *
from paquete_miArchivo.miArchivo import *
from paquete.mimodelo import *
import json

m = MiArchivo() # objeto para leer el archivo
lista = m.obtener_informacion()
lista = [l.split(";") for l in lista] #manejo de split para cojer un elemento  donde termina en |
	

lista_edades = [] #creacion de lista vaci para las edades

for i in lista: #for que se ocupa para recorrer la lista
    
     
    elemento = int(i[2])  #a la variable se le asigna el elemento de la posicion 2 
    
    e = Persona(elemento) #creamos objeto
 
    lista_edades.append(elemento) #agregamos a la lista  la variable creada 
    

    
 
print("Lista no ordenada")   #presentacion de listas
print(lista_edades)

merge_sort_result = merge_sort(lista_edades)   #creamos una variable donde mandamos a la lista para que se ordene 
print("Lista ordenada")
print(merge_sort_result) #presentacion de lista

