# -º- coding: utf-8 -º-
'''
Pr�ctica 28
FechaL�mite:2/11/2020
FechaCorreci�n:5/11/2020

author@: alvaro.sanchez
'''
#Escribir un programa que solicite del usuario una lista de edades y muestre en pantalla la lista de edades de menor a mayor y de menor a mayor.

#Primero voy a crear una lista de edades.
#Ahora con el método sort voy a ordenar la lista de forma ascendente.
#Printamos la lista.
thislist= [91,10,7,45,22,4,38,66,18,15]
thislist.sort(key=None, reverse=False)
print (thislist)

nombre= input()
print(nombre)