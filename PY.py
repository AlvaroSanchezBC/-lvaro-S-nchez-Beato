a = str(input("Escriba una frase: "))
b= input("Escriba una letra: ")
contador= 0
i = 0
while i<=len(a)-1:
    if a[i] == b:
        contador += 1
        i+=1
    else: i+=1
print(contador)        