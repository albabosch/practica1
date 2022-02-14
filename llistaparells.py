#programa que donat una valors en una llista, digui quins son parells i els parells es posin en una llista nova.
llista2 = []
llista = []

for i in range (0, 20):
    llista.append(i)

for i in llista:
    if (i % 2 == 0):
        print(i)

        llista2.append(i)

print(llista2)