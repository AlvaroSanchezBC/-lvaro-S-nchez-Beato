#-�- coding: utf-8 -�-
'''
Created on 4 nov. 2020

@author: alvaro.sanchez
Texto:Solicitar un numero entero por teclado.

'''
if __name__ == "__main__":
    try:
       #Solicitamos un numero entero al usuario con metodo int(numero entero) 
       numero = int(input("Dame un numero entero"))
       #Printamos(numero)
       print(numero)
        
        
        
        
    except Exception as e:
        print('Error: ' + str(e))     