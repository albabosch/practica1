#programa que donat una valors en una llista, digui quins son parells i els parells es posin en una llista nova.
llista2 = []
llista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


for i in llista:
    if (i % 2 == 0):
        print(i)

        llista2.append(i)

print(llista2)