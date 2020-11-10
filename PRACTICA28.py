#-º- coding: utf-8 -º-
'''
Created on 30 oct. 2020

PR�CTICA28
@author: alvaro.sanchez
FechaL�mite: 2/11/2020
FechaCorreci�n: 5/11/2020
Texto:Escribir un programa que solicite del usuario una lista de edades y muestre 
en pantalla la lista de edades de menor a mayor y de mayor a menor.




'''
if __name__ == "__main__":
    try:
        # solicitar una lista
        strLista = int(input('Dame una lista de edades separada por comas'))
        # tener una lista edades
        print(strLista)
        print(strLista.split(','))
        # ordenar de menor a mayor
        strLista= ['10', ' 7', ' 90', ' 86', ' 22']
        for numero in strLista:
            strLista.append(int(numero))
        strLista.sort()
        print(strLista)
        # ordenar de mayor a menor
        strLista.sort(reverse=True)
    except Exception as e:
        print('Error: ' + str(e))