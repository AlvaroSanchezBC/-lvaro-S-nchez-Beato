#-�- coding: utf-8 -�-
'''
Created on 4 nov. 2020

@author: alvaro.sanchez
Texto: Solicitar dos textos por teclado, si son numericos damos por resultado la suma, 
y si son cualquier otra cosa damos solucion

'''
if __name__ == "__main__":
    try:
        #Solicitamos un caracter al usuario 2 veces
        cosa1 = input("Dame lo que quieras")
        cosa2 = input("Dame lo que quieras 2")
        numeros = True
        try:
            cosa1 = int(cosa1)
        except:
            numeros = False
        if (numeros):
            try:
                cosa2 = int(cosa2)
                print(str(cosa1 + cosa2))
            except:
                print(str(cosa1) + ' ' + cosa2)
        else:
            print(cosa1 + ' ' + cosa2)
        
    except Exception as e:    
        print('Error: ' + str(e))
        
        