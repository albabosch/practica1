#demanar num positiu, conta enrrere fins 0, separat per comes. Si es negatiu, informar

llista = []

num = int(input("escriu un nombre positiu: "))

if num < 0:
    print ("No es un nombre positiu. ")
else:
    while num > 0:
        num -= 1
        llista.append(num)



print(llista)