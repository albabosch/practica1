import random
valor_1, valor_2, valor_3 = input("Indica valors: ").split()

llista = []

llista.append(valor_1)
llista.append(valor_2)
llista.append(valor_3)

print(llista)
random.shuffle(llista)

print(llista)