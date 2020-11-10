# -º- coding: UTF-8 -º-

"""
Practica
Autor: ASC
Texto: Solicitamos dos numeros enteros al usuario y devolvemos el cociente 
y el resto de la division entera entre ellos

"""
def my_division(numero1,numero2):
    return [numero1//numero2, numero1 -(numero1//numero2 * numero2)]

if __name__ == "__main__":
    try:
        #Solicitamos dos numeros enteros al usuario mediante un input con el metodo int
        numero1 = int(input('Dame un numero entero'))
        numero2 = int(input('Dame un numero entero'))
        resultado = my_division(numero1, numero2)
        print(resultado)
        #
        
        
        
        
        
        
    except Exception as e:
        print('Error: ' + str(e))